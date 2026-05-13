import re

def extract_markdown_images(text):
    # def find_alt(text):
    alts = re.findall(r'!\[(.*?)\]\(.*?\)', text)
    url = re.findall(r'!\[.*?\]\((.*?)\)', text)
    out = zip(alts, url)
    return  list(out)

def extract_markdown_links(text):
    # def find_alt(text):
    alts = re.findall(r'(?<!!)\[(.*?)\]\(.*?\)', text)
    url = re.findall(r'(?<!!)\[.*?\]\((.*?)\)', text)
    out = zip(alts, url)
    return  list(out)
        
