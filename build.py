import os
import shutil
from posixpath import join
from os import listdir
from os.path import isfile

build_dir = "dist/"
pages_dir = "pages"
shutil.rmtree(build_dir,ignore_errors=True)
os.makedirs(build_dir,exist_ok=True)
shutil.copytree("assets", join(build_dir,"assets")) 
pages = [f for f in listdir(pages_dir) if isfile(join(pages_dir, f))]

print(pages)

with open("templates/template.html", "r") as fp:
    template_data = fp.read()

for page in pages:
    print(f"Building {page}")
    with open(join(pages_dir,page), "r") as inp:
        data = inp.read()
    
    out_data = template_data.replace("{{ body-content }}",data)

    with open(join(build_dir,page), "w") as out:
        out.write(out_data)
    
    