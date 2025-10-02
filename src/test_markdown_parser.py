import unittest

from textnode import TextNode, TextType
from markdown_parser import split_nodes_delimiter

class TestMarkdownParser(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])
    def test_split_nodes_delimiter_bold_invalid_markdown(self):
        node = TextNode("This is text with a **bold* word", TextType.TEXT)
        with self.assertRaises(Exception) as e:
            split_nodes_delimiter([node], "**", TextType.TEXT)
        self.assertEqual(str(e.exception), "Invalid Markdown syntax")
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])
    def test_split_nodes_delimiter_italic_invalid_markdown(self):
        node = TextNode("This is text with a _bold word", TextType.TEXT)
        with self.assertRaises(Exception) as e:
            split_nodes_delimiter([node], "_", TextType.TEXT)
        self.assertEqual(str(e.exception), "Invalid Markdown syntax")
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code` block", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" block", TextType.TEXT),
        ])
    def test_split_nodes_delimiter_code_invalid_markdown(self):
        node = TextNode("This is text with a `code block", TextType.TEXT)
        with self.assertRaises(Exception) as e:
            split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertEqual(str(e.exception), "Invalid Markdown syntax")
if __name__ == "__main__":
    unittest.main()