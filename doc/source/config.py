class Config :
    doc_title = "Teex Docs"
    root_dir = "" # path to the doc/ dir, default value $ pwd
    css = ['/doc/rsc/style.css'] # path of css stylsheat FROM the root_dir
    script = [root_dir + "/doc/rsc/shiki.js"] # path of importing script
    head = ""

    def generate_head():
        head = f'<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>{Config.doc_title}</title>\n'
        for css in Config.css:
            print(Config.root_dir)
            print(css)
            head += f"<link rel='stylesheet' href='{Config.root_dir + css}'>\n"
        for script in Config.script:
            head += f'<script src="{script}"></script>'
        Config.head = "<head>\n" + head + "\n</head>"


