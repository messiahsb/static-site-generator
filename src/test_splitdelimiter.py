import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_parser import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD) 
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(new_nodes, test_nodes)

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)    
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, test_nodes)

    def test_italics(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)    
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, test_nodes)

    def test_text(self):
        node = TextNode("This is text with a `code block` word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)    
        test_nodes = [
         TextNode("This is text with a `code block` word", TextType.BOLD)
        ]
        self.assertListEqual(new_nodes, test_nodes)

    def multi_split(self):
        bold_node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        code_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([bold_node, node, code_node], "_", TextType.ITALIC)    

        test_nodes = [
            TextNode("This is text with a **bold block** word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, test_nodes)

    def multi_bold_split(self):
        bold_node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        bold_node_two = TextNode("This is text with a different **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([bold_node, bold_node_two], "**", TextType.BOLD)    

        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a different ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, test_nodes)
    
    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
