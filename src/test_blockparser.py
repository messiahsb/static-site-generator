import unittest

from block_parser import markdown_to_blocks, BlockType, block_to_block_type



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

        def test_code_block(self):
            block = "```\nThis is a code block test by two lines will this work\nAnd will this line be included\n```"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.CODE
        )   
        def test_bad_code_block(self):
            block = "```\nThis is a code block test by two lines will this work\nAnd will this line be included\n``"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.PARAGRAPH
        )   

        def test_quote_block(self):
            block = "> This is a quote block test by two lines will this work\n> And will this line be included"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.QUOTE
        )   
        def test_bad_quote_block(self):
            block = "> This is a quote block test by two lines will this work\nAnd will this line be included"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.PARAGRAPH
        )   

        def test_ordered_block(self):
            block = "1. This is a quote block test by two lines will this work\n2. And will this line be included"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.ORDERED_LIST
        )   
        def test_bad_ordered_block(self):
            block = "1. This is a quote block test by two lines will this work\n2.And will this line be included"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.PARAGRAPH
        )   

        def test_bad_ordered_block_p2(self):
            block = "1. This is a quote block test by two lines will this work\n2. And will this line be included\n3."
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.PARAGRAPH
        )   

        def test_unordered_block(self):
            block = "- This is a quote block test by two lines will this work\n- And will this line be included"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.UNORDERED_LIST
        )   

        def test_bad_unordered_block(self):
            block = "- This is a quote block test by two lines will this work\n-And will this line be included"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.PARAGRAPH
        )   

        def test_bad_unordered_block_p2(self):
            block = "- This is a quote block test by two lines will this work\n- And will this line be included\n-"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.PARAGRAPH
        )   

        def test_heading_block(self):
            block = "# This is a quote block test by two lines will this work\n## And will this line be included"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.HEADING
        )   

        def test_bad_heading_block(self):
            block = "#This is a quote block test by two lines will this work\n#And will this line be included\n-"
            block_type =  block_to_block_type(block)
            self.assertEqual(
                 block_type,
                 BlockType.PARAGRAPH
        )   


if __name__ == "__main__":
    unittest.main()
