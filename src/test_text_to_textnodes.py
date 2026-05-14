
import unittest

from text_to_textnodes import text_to_textnodes, TextNode, TextType, split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestTextToNodes(unittest.TestCase):
    def test_with_all_thethings(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )
    def test_with_bold_andlinks(self):
        text = "This is a link [link](https://boot.dev) and this is **bold** does this work"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a link ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and this is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" does this work", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_with_code_and_images(self):
        text = "This is an image ![link](https://boot.dev) and this is `code` does this work"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is an image ", TextType.TEXT),
                TextNode("link", TextType.IMAGE, "https://boot.dev"),
                TextNode(" and this is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" does this work", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_with_all_thethings2(self):
        text = "This is `code` with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) word and a **bold** and an _italic_ and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" with an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()

