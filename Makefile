# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = sphinx
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Published documentation to gh-pages
gh-pages: singlehtml
	@cp -r -a -T build/singlehtml docs/

# Makes a docker image
game-image: 
	docker build -f dockerfiles/game.dockerfile -t aiplatformer:latest .

# Makes an exec in dist/
game:
	pyinstaller -F  -no-pie -n aiplatformer dockerfiles/aiplatformer.spec

test:
	python3 -m unittest discover test

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)