from typing import List, Optional
import re
from config import Config

# ALL TREATMENT
def treatment(page):
    page = image(page)
    page = big_warnings(page)
    page = warnings(page)
    page = big_info(page)
    page = info(page)
    page = code_bloc(page)
    page = single_code_bloc(page)
    page = hr(page)
    page = small_hr(page)
    page = syntax_highlite_shiki_script(page)
    return page






def hr(page:str):
    pattern = r"---\n"
    replacement = r"<hr>\n"
    return re.sub(pattern, replacement, page)

def small_hr(page:str):
    pattern = r"-\n"
    replacement = r"<hr class='small'>\n"
    return re.sub(pattern, replacement, page,flags=re.DOTALL)
# custom markdown syntaxt : !- ... -! => warning block
def warnings(page:str):
    pattern = r"!-(.*?)-!"
    replacement = r"<span class='warn'>⚠️  \1</span>\n"
    return re.sub(pattern, replacement, page,flags=re.DOTALL)
def big_warnings(page:str):
    pattern = r"!!-(.*?)-!!"
    replacement = r"<div class='warn'>⚠️  \1</div>\n"
    return re.sub(pattern, replacement, page,flags=re.DOTALL)


# custom markdown syntaxt : n- ... -n => note block
def info(page:str):
    pattern = r"i-(.*?)-i"
    replacement = r"<span class='info'>ℹ️  \1</span>\n"
    return re.sub(pattern, replacement, page)
def big_info(page:str):
    pattern = r"ii-(.*?)-ii"
    replacement = r"<div class='info'>⚠️  \1</div>\n"
    return re.sub(pattern, replacement, page,flags=re.DOTALL)




def image(page):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    replacement = fr"<div class='img-cont'><img src='{Config.root_dir}/doc/\2'><p>\1<p></div>\n"
    return re.sub(pattern, replacement, page)


def syntax_highlite_shiki_script(page):
    shiki = """shiki
    .getHighlighter({
        theme: 'dracula'
    })
    .then(highlighter =>{
        document.querySelectorAll('pre').forEach(element => {
        const language = element.dataset.lang || 'plaintext';
        const code = highlighter.codeToHtml(element.innerText, language);
        element.innerHTML = code
        })
    })"""

    return page + f"<script>\n{shiki}\n</script>"


# tag must be like "body" not "<body>"
def warp(src:str,tag:str):
    return f"<{tag}>\n{src}\n</{tag}>"



def code_bloc(page):
    pattern = r"```([a-zA-Z]*)\s*([\s\S]+?)\s```"
    replacement = r"<pre data-lang='\1'>\2</pre>\n"
    return re.sub(pattern, replacement, page).replace("data-lang=''","data-lang='plaintext'")

def single_code_bloc(page):
    pattern = r"`\s*([\s\S]+?)`"
    replacement = r"<span class='one'>\1</span>\n"
    return re.sub(pattern, replacement, page)




