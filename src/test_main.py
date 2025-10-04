import unittest

from main import extract_title

class TestMain(unittest.TestCase):

    def test_extract_title_single_h1_header(self):
        markdown = "# My Title"
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_h1_with_leading_whitespace(self):
        markdown = "   # My Title"
        # should not match because of leading spaces before '# '
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_multiple_headers(self):
        markdown = "# Title 1\n## Subtitle\n# Title 2"
        # should return the first h1 header
        self.assertEqual(extract_title(markdown), "Title 1")

    def test_extract_title_no_h1_header(self):
        markdown = "## Subtitle\nSome text"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_h1_with_trailing_spaces(self):
        markdown = "# Title with spaces    "
        self.assertEqual(extract_title(markdown), "Title with spaces")

    def test_extract_title_empty_markdown(self):
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()