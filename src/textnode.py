from enum import Enum
from htmlnode import LeafNode
from inline_parser import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TextType(Enum):
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    TEXT = "Text"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (True if self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url 
                else False)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', None, {'src': text_node.url, 'alt':text_node.text})
        case _:
            raise Exception("Not a valid text type")

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes