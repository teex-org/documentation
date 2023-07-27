folder_path="./doc/pages/"

# Vérifier si le dossier existe
if [ -d "$folder_path" ]; then
    rm -r "$folder_path"/*
else
    echo "Can't clear $folder_path cause dit do not exist"
fi

python3 -B ./doc/source/codex.py
open ./doc/pages/home.html