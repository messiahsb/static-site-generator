import unittest

from main import extract_title

class GeneratePage(unittest.TestCase):
    def test_text(self):
        md = """
# Test Heading 1

This is a paragraph with a link [link](https://www.google.com).
text in a p
tag here

This is another paragraph with an image ![Description of image](url/of/image.jpg).
    """

        heading = extract_title(md)
        self.assertEqual("Test Heading 1", heading)
    def test_text2(self):
        md = """
## Test Heading 2

# Test Heading 1

text in a p
tag here

    """
        heading = extract_title(md)
        self.assertEqual("Test Heading 1", heading)

if __name__ == "__main__":
    unittest.main()