
from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_to_textnodes, text_node_to_html_node   

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

#takes mark down text and returns a list of text blocks
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return_blocks = []
    for block in blocks:
        if block.strip():
            return_blocks.append(block.strip())

    return return_blocks

#takes a block of markdown text and returns the type of block it is, code/italics/bold/etc..
def  block_to_block_type(block):


    headings = ('# ', '## ', '### ' '#### ', '##### ', '###### ')
    if block.startswith(headings):
        return BlockType.HEADING

    # checks for a code block
    if block[0] == "`":
        lines = block.split('\n')
        if lines[0].strip()  == "```" and lines[-1].strip()  == "```" :
            return BlockType.CODE

    # checks for a quote block
    if block[0] == ">":
        lines = block.split('\n')
        for line in lines:
            if line[0] != ">":
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    # checks for an ordered block
    if block[0] == "1":
        lines = block.split('\n')
        for idx, line in enumerate(lines):
            if len(line) < 3 or line[0:3] != f"{idx+1}. ":
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    # checks for an unordered block
    if block[0] == "-":
        lines = block.split('\n')
        for idx, line in enumerate(lines):
            if len(line) < 2 or line[0:2] != "- ":
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST


    return BlockType.PARAGRAPH


# helper function for markdown to html node
def create_new_htmlnode(block, blocktype):
    num_tags = block.count('#')
    match (blocktype):
        case (BlockType.QUOTE):
         return HTMLNode("blockquote")
        case (BlockType.CODE):
         return HTMLNode("pre",children=[HTMLNode("code", block)])
        case (BlockType.HEADING):
         return HTMLNode(f"h{num_tags}")
        case (BlockType.UNORDERED_LIST):
         return HTMLNode("ul")
        case (BlockType.ORDERED_LIST):
         return HTMLNode("ol")
        case (BlockType.PARAGRAPH):
         return HTMLNode("p")
        case _:
         raise Exception("Not Expected BlockType") 

# helper function for markdown to html node to create child nodes
def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
       children.append(text_node_to_html_node(node))


#takes blocks defined in previous functions and converts them to html nodes
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        new_node = create_new_htmlnode(block, block_type)
        new_node.children = text_to_children(block)
        
        print(new_node)


md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
markdown_to_html_node(md)