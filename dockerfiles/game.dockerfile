FROM --platform=x86_64 python:3.8.5 AS BUILDER

ENV DEBIAN_FRONTEND="noninteractive"

WORKDIR /build

RUN apt update; apt install -y patchelf

# Pip requirements
COPY requirements.txt .
COPY requirements-dev.txt .
RUN python3 -m pip install setuptools staticx ;\
python3 -m pip install -r requirements.txt;\
python3 -m pip install -r requirements-dev.txt

# Resources
COPY assets ./assets/
COPY src ./src/
COPY dockerfiles/aiplatformer.spec dockerfiles/aiplatformer.spec

RUN pyinstaller -F  -no-pie -n aiplatformer dockerfiles/aiplatformer.spec ;\
staticx ./dist/aiplatformer /build/aiplatformer.static

FROM --platform=x86_64 alpine:latest As FINAL

LABEL github.JonathanJakobsson.name="aiplatformer"
LABEL github.JonathanJakobsson.description="Game"
LABEL github.JonathanJakobsson.url="github.com/JonathanJakobsson/aiplatformer"
LABEL github.JonathanJakobsson.vendor="SiB Solutions AB"
LABEL github.JonathanJakobsson.version="beta"
LABEL github.JonathanJakobsson.maintainer="github.com/JonathanJakobsson/aiplatformer"
LABEL github.JonathanJakobsson.docker.env="DISPLAY"
LABEL github.JonathanJakobsson.docker.cmd.='\
xhost +si:localuser:root; \
docker run -it --net=host -e DISPLAY \
 -e XAUTHORITY=/root/.Xauthority -v /tmp/.X11-unix aiplatformer'

WORKDIR /app

COPY --from=BUILDER /build/aiplatformer.static .

ENTRYPOINT ["./aiplatformer.static"]