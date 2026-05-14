
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return_blocks = []
    for block in blocks:
        if block.strip():
            return_blocks.append(block.strip())

    return return_blocks

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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        