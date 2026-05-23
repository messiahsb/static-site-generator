from textnode import TextNode, TextType
import re

# thi function takes markdown formatted text, such as bolded or italic, and makes it into text nodes to be converted to html
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue


        delim_count = 0
        delim_count = node.text.count(delimiter)
        if delim_count % 2 != 0:
            raise Exception("missing delimiter, invalid markdown syntax") 
        
        split_text = node.text.split(delimiter)

        nodes = []
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i%2 == 1:
                nodes.append(TextNode(split_text[i], text_type))
            else:
                nodes.append(TextNode(split_text[i], TextType.TEXT))
        
        new_nodes.extend(nodes)

    return new_nodes
        
# this function gets the alt text and image url from markdown syntax
def extract_markdown_images(text):
    # def find_alt(text):
    alts = re.findall(r'!\[(.*?)\]\(.*?\)', text)
    url = re.findall(r'!\[.*?\]\((.*?)\)', text)
    out = zip(alts, url)
    return  list(out)

# this function gets the link text and url from markdown syntax
def extract_markdown_links(text):
    # def find_alt(text):
    alts = re.findall(r'(?<!!)\[(.*?)\]\(.*?\)', text)
    url = re.findall(r'(?<!!)\[.*?\]\((.*?)\)', text)
    out = zip(alts, url)
    return  list(out)
        
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # if delimiter not in closing_delimiters:
        #     raise
        extracted_images = extract_markdown_images(node.text)
        split_text = []
        nodes = []
        if len(extracted_images) == 0:
            new_nodes.append(node)
            continue

        for image in extracted_images:
            image_text = image[0]
            image_url = image[1]
            # spliting the text node up until the image then adding just the text to the array
            split_text = node.text.split(f"![{image_text}]({image_url})", 1) 
            if len(split_text) != 2:
                raise ValueError("images missing, invalid markdown syntax")
            text_before = split_text[0] 
            if text_before != "":
                nodes.append(TextNode(text_before, TextType.TEXT))
            # adding the image now to the array
            nodes.append(TextNode(image_text, TextType.IMAGE, image_url))
            node.text = split_text[1]

            # spliting the text node after until the image then adding just the text to the array
            # text_after = split_text[0] 
            # nodes.append(TextNode(text_after, TextType.TEXT))
        if node.text != "":
            nodes.append(TextNode(node.text, TextType.TEXT))
        

        new_nodes.extend(nodes)


    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # if delimiter not in closing_delimiters:
        #     raise
        extracted_links = extract_markdown_links(node.text)
        split_text = []
        nodes = []
        if len(extracted_links) == 0:
            new_nodes.append(node)
            continue

        for links in extracted_links:
            link_text = links[0]
            link_url = links[1]
            # spliting the text node up until the link then adding just the text to the array
            split_text = node.text.split(f"[{link_text}]({link_url})", 1) 
            if len(split_text) != 2:
                raise ValueError("images missing, invalid markdown syntax")

            text_before = split_text[0] 
            if text_before != "":
                nodes.append(TextNode(text_before, TextType.TEXT))
            # adding the link now to the array
            nodes.append(TextNode(link_text, TextType.LINK, link_url))
            node.text = split_text[1]

            # spliting the text node after until the link then adding just the text to the array
            # text_after = split_text[0] 
            # nodes.append(TextNode(text_after, TextType.TEXT))
        if node.text != "":
            nodes.append(TextNode(node.text, TextType.TEXT))
        

        new_nodes.extend(nodes)


    return new_nodes



