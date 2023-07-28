


config = {
    'doc_title' : 'Teex Documentation',
    'css' : ['style.css'], #all css file in /docs/rsc/
    'local_sript' : ['shiki.js'], #all script in /docs/rsc/
    'sript' : [''], #all absolute script (when get from internet)

    # the root_dir is the root path where ACCESS the dir /docs
    # if you generate local doc in /absolute/path/to/docs/, root_dit will be : /absolute/path/to/
    # for a docs ni a serveur, the root dir will be http://your.domaine.com/.../ from where you can acces /docs (dont put .../docs at the end)
    # its not the root dir for building the doc. codex find all data from itself, with relative path
    # so do not change the strutur or name of dirs, weather codex will be lost
    'root_dir' : "https://teex-org.github.io/documentation"
}