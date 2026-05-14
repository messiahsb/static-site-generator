import unittest

from block_parser import markdown_to_blocks



class TestExtractLink(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
        )   

        def test_markdown_to_blocks(self):
            md = """

# This is a heading

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


This is separated by two lines will this work
And will this line be included

- This is a list
- with items


- This is a different list
- with an item 

- This is a third list
- with an item 
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                   "# This is a heading",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "This is separated by two lines will this work\nAnd will this line be included",
                    "- This is a list\n- with items",
                    "- This is a different list\n- with an item",
                    "- This is a third list\n- with an item",
                ],
        )   



if __name__ == "__main__":
    unittest.main()
