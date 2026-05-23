
from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node   
from inline_parser import split_nodes_delimiter, text_to_textnodes

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


#takes blocks defined in previous functions and converts them to html nodes
def markdown_to_html_node(markdown):
    indiv = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        new_node = create_new_htmlnode(block, block_type)
        # code blocks need to be left unaltered by inline parsing
        if block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            list_children = text_to_list_children(block, block_type)
            new_node.children.extend(list_children)

        elif block_type == BlockType.CODE:   
            cleaned_text = clean_text_for_html(block, block_type)
            code_node = TextNode(cleaned_text, TextType.CODE)
            new_node.children.append(text_node_to_html_node(code_node))
        else:
            cleaned_text = clean_text_for_html(block, block_type)
            new_node.children.extend(text_to_children(cleaned_text))


        indiv.append(new_node)
    div = ParentNode("div", children=indiv)
    return div
        
# helper function for markdown to html node
def create_new_htmlnode(block, blocktype):
    match (blocktype):
        case (BlockType.QUOTE):
         return ParentNode("blockquote", [])
        case (BlockType.CODE):
         return ParentNode("pre", [])
        case (BlockType.HEADING):
            # block.count('#')
            num_tags = 0
            for  n in  block:
                if n == "#":
                  num_tags+=1 
                else:
                  break
            return ParentNode(f"h{num_tags}", [])
        case (BlockType.UNORDERED_LIST):
         return ParentNode("ul", [])
        case (BlockType.ORDERED_LIST):
         return ParentNode("ol", [])
        case (BlockType.PARAGRAPH):
         return ParentNode("p",[])
        case _:
          raise Exception("Not Expected BlockType")

def clean_text_for_html(block, blocktype):
     match (blocktype):
        case (BlockType.QUOTE):
            lines = block.split('\n')
            cleaned_text = " ".join(line.strip('>').strip() for line in lines)
            return cleaned_text
        case (BlockType.HEADING):
            num_tags = 0
            for n in block:
                if n == "#":
                  num_tags+=1 
                else:
                  break
            # +1 to clean the space after the #
            cleaned_text = block[num_tags+1:]
            return cleaned_text
        case (BlockType.CODE):
            cleaned_text = block[4:-3]
            return cleaned_text
        case (BlockType.PARAGRAPH):
            lines = block.split('\n')
            cleaned_text = " ".join(line.strip() for line in lines)
            return cleaned_text
        case _:
         raise Exception("Not Expected BlockType")      
        # case (BlockType.UNORDERED_LIST):
        #     lines = block.split('\n')
        #     cleaned_text = ""
        #     for idx, line in enumerate(lines):
        #          line = line[2:]
        #     return cleaned_text
        # case (BlockType.ORDERED_LIST):
        #     lines = block.split('\n')
        #     cleaned_text = ""
        #     for idx, line in enumerate(lines):
        #          line = line.split(". ", 1)[1]
        #     return cleaned_text

# helper function for markdown to html node to create child nodes
def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
           children.append(text_node_to_html_node(node))
    return children
# helper function for markdown to html node to create child nodes
def text_to_list_children(text, blocktype):
    children = []
    lines = text.split('\n')
    for line in lines:
        # strip leading markers
        if blocktype == (BlockType.UNORDERED_LIST):
            line = line[2:]
        elif blocktype ==  (BlockType.ORDERED_LIST):
                line = line.split(". ", 1)[1]

        # each line in a list should be built with li for each line
        listparent  = ParentNode("li", children=[])
        text_nodes = text_to_textnodes(line)
        for node in text_nodes:
            listparent.children.append(text_node_to_html_node(node))
        children.append(listparent)
    return children