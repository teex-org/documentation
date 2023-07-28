from features import treatment
import os
import re
from config import Config
import markdown



if Config.root_dir == '':
    Config.root_dir = os.popen('pwd').read().replace('\n','') + '/docs'

Config.generate_head()


html_dir        =   './pages/'
md_dir          =   Config.root_dir + '/docs/mds/'

def sort_path(page):
    section, category, md_name =  page.replace('./docs/mds/','').split('/')
    r = 0
    nb_section=re.findall('^(.*?)-',section)
    if (nb_section != []) and (nb_section != ['']):
        r += int(nb_section[0])*200_000

    nb_category=re.findall('^(.*?)-',category)
    if (nb_category != []) and (nb_category != ['']):
        r += int(nb_category[0])*200

    nb_md_name=re.findall('^(.*?)-',md_name)
    if (nb_md_name != []) and (nb_md_name != ['']):
        r += int(nb_md_name[0])
    return r
        
def wrap(src:str,tag:str):
    return f"<{tag}>\n{src}\n</{tag}>"

def rm_prefix_number(word):
    return re.sub('^[0-9]+-','',word)

class Page:
    def __init__(self,md_path):
        self.md_path = md_path
        self.section, self.category, self.md_name =  md_path.replace('./docs/mds/','').split('/')
        self.display_name = rm_prefix_number(self.md_name.replace('.md',''))
        self.html_name = self.md_name.replace('.md','.html')
        self.html_dir = f"./pages/{self.section}/{self.category}/"
        
    def get_nav(self,active=False):
        class_active = ""
        if active:
            class_active = " class='active'"          
        return f"<a{class_active} href='../../../{self.html_dir+self.html_name}'>{self.display_name}</a>\n"
    
    def generate(self,select,nav):
        md = ''
        with open(self.md_path,'r') as md_file:
            md = md_file.read()
        
        md = treatment(md) # apply all transformation
        md = markdown.markdown(md) # fix markdown to html
        md = f"<h1 class='title'>{page.display_name}</h1>" + md # Add page title
        md = wrap(md,'article') 
        md = nav + md # adding the nav on the side
        md = md.replace(self.get_nav(),self.get_nav(True)) # add 'active' class on the nav coresponding to the page
        md = wrap(md,'main')
        select = select.replace(f">{rm_prefix_number(self.section)}</option>",f"selected>{rm_prefix_number(self.section)}</option>")
        select += """
        <script defer>
            select = document.querySelector("select")
            window.addEventListener("load", ()=>{console.log('hehe'); select.style.width = select.options[select.selectedIndex].text.length * 13 + 20 + 'px'}); 
        </script>""" #resize the width depending on content
        header = f"<header>\n<h1>{Config.doc_title}</h1>\n{select}</header>\n" # add header with select
        md = header + md 
        md = wrap(md,'body') 
        md = Config.head + md # add head from the head in config

        # create dir and create pages
        os.makedirs(Config.root_dir + self.html_dir[1:] , exist_ok=True) 
        print(Config.root_dir + self.html_dir[1:] + self.html_name )
        with open(Config.root_dir + self.html_dir[1:] + self.html_name ,'w') as html_file:
            html_file.write(md)



all_md_pages = os.popen(f"find ./docs/mds -mindepth 3 -maxdepth 3 -name '*.md'").read().split('\n')[:-1]
print(all_md_pages)
all_md_pages = sorted(all_md_pages, key=sort_path)

pages = []
tree = {}
header_section_option = []

# Create Page object, centralise all pages in same category in a "nav" string
for md_path in all_md_pages:
    page = Page(md_path)
    pages.append(page)
    section = page.section
    if not(section in header_section_option):
        header_section_option.append(section)
    if not(section in tree):
        tree[section] = {
            "first_page": page.html_dir + page.html_name,
            'categories':[],
            'nav':''
            }
    if page.category not in tree[section]['categories']:
        tree[section]['categories'].append(page.category)
        tree[section]['nav'] += f"<p>{rm_prefix_number(page.category)}</p>\n"
    tree[section]['nav'] += page.get_nav()


# creating select <header> 
select = "<select onchange='window.location.href = this.value'>\n"
select += f"<option value='{'home.html'}'>home</option>\n"
for section in header_section_option:
    
    select += f"<option value='{tree[section]['first_page']}'>{rm_prefix_number(section)}</option>\n"
select += "</select>\n"


# generate .html page 
for page in pages:
    nav = "<nav>" + tree[page.section]['nav'] + "</nav>"
    page.generate(select,nav)

# generate home.html page 
home = f"""
{Config.head.replace('../../../','')}
<body id='home'>
<header><h1>{Config.doc_title}</h1>{select}</header>
<main>
<h1 class='title'>{Config.doc_title}</h1>
<p>Chose a section (in the top right) to explore</p>
</main>
</body>
"""
os.makedirs(html_dir, exist_ok=True) 

with open(Config.root_dir + '/home.html' ,'w') as html_file:
    html_file.write(home)


print("build")
