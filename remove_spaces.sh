
remove_spaces () {
    local f="${1}"
    if [[ -f "${f}" ]]; then
        local newname=`echo "${f}" | sed -e 's/ /_/g'` 
        if [[ "${f}" != $newname ]]; then
            echo "${f}" " -> " $newname
            git mv "${f}" $newname
        fi
    elif [[ -d "${f}" ]]; then
        for file in "${f}"/*
        do
            local newname=`echo "${f}" | sed -e 's/ /_/g'` 
            if [[ "${f}" != $newname ]]; then
                echo "${f}" " -> " $newname
                git mv "${f}" $newname
            fi
            remove_spaces "${file}"
        done
    else
        echo "What? ${f}"
    fi
}

for file in $(pwd)/assets/*
do
    remove_spaces "${file}"
done


