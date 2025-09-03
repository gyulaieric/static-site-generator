import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node1)
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com/")
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.test.com/")
        self.assertEqual(node, node1)
    def test_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node1)
    def test_eq_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node1)
    def test_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com/")
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.differenttest.com/")
        self.assertNotEqual(node, node1)
    def test_eq_url_none_and_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a different text node", TextType.BOLD, "https://www.test.com/")
        self.assertNotEqual(node, node1)

if __name__ == "__main__":
    unittest.main()