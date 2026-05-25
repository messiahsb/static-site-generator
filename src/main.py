import os
from pathlib import Path
import shutil
import sys

from block_parser import markdown_to_html_node

def main():
    args = sys.argv
    print(args)
    if len(args) == 1:
        basepath = '/'
    else:
        basepath = args[1]
    
    get_files_from('static', "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

def get_files_from(src, dest):
    # check if both src and dest exist
    if not os.path.exists(src):
        raise Exception("src directory not found")
    if not os.path.exists(dest):
        os.mkdir(dest)

    # delet all contents of destination directory
    print("deleting public directory")
    shutil.rmtree(dest)
    os.mkdir(dest)

    # copy files sub directories and nested files
    move_files(src, dest)

def move_files(src, dest):
    # loop through files and directories of src to copy into public
    for idx in os.listdir(src):
        src_path = os.path.join(src, idx)
        dest_path = os.path.join(dest, idx)
        if os.path.isfile(src_path):
            print(f"copying file {src_path} to {dest_path}")
            shutil.copy(src_path, dest)
        if os.path.isdir(src_path):
            print(f"copying directory {src_path} to {dest_path}")
            os.mkdir(dest_path)
            move_files(src_path, dest_path)
        # log path of each file copies
    
    return os.path.exists(src)
# grabs the title of the markdown file to format to the html page
def extract_title(markdown):
    lines = markdown.split("\n")
    heading = ""
    for line in lines:
        if line.startswith("# "):
            heading = line.split("# ")[1]
            break
    
    if heading == "":
        raise Exception("No header found")
    return heading

# generates html content using our function written markdown_to_html to make the page in the requested directory
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_content = file.read()

    with open(template_path) as file:
        template_content = file.read()

    html_from_md = markdown_to_html_node(from_content).to_html()
    title_from_md = extract_title(from_content)

    template_content = template_content.replace("{{ Content }}", html_from_md)
    template_content = template_content.replace("{{ Title }}", title_from_md)
    template_content = template_content.replace('href="/', 'href="{basepath}')
    template_content = template_content.replace('src="/', 'src="{basepath}')

   

    with open(dest_path, "w") as file:
        file.write(template_content)

# generates all the pages in a directory to html files 
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    for idx in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, idx)
        dest_path = os.path.join(dest_dir_path, idx)
        if os.path.isfile(content_path):
            dest_path = Path(dest_path).with_suffix(".html")
            print(f"generating file {content_path} to {dest_path}")
            generate_page(content_path, template_path, dest_path, basepath)
        if os.path.isdir(content_path):
            print(f"moving into dir directory {content_path} to {dest_path}")
            os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path, basepath)
    
main()
