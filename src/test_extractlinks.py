import unittest

from markdown_parsers import extract_markdown_links, extract_markdown_images

class TestExtractLink(unittest.TestCase):
    def test_bold(self):
        pass

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches) 
    
    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches) 

    def test_extract_markdown_link_many(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [link number 2](https://boot.dev) "
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png"), ("link number 2", "https://boot.dev")], matches) 

    def test_extract_markdown_images_many(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image number 2](https://boot.dev) "
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image number 2", "https://boot.dev")], matches) 

    def test_extract_markdown_images_not_link(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [link number 2](https://boot.dev) "
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches) 
    def test_extract_markdown_link_not_images(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another ![link number 2](https://boot.dev) "
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches) 


    def test_extract_markdown_images(self):
            matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://wikipedia.org"),
            ],
            matches,
        )
if __name__ == "__main__":
    unittest.main()
