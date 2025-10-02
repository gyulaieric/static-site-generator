import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    # text_node_to_html_node
    def test_invalid_texttype(self):
        node = TextNode("This is a text node", "invalid")
        with self.assertRaises(Exception) as e:
            text_node_to_html_node(node)
        self.assertEqual(str(e.exception), "TextNode has invalid TextType")
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": node.url})
        self.assertEqual(html_node.value, "This is a link node")
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://cdn.7tv.app/emote/01EZTD6KQ800012PTN006Q50PV/4x.avif")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": node.url, "alt": node.text})

if __name__ == "__main__":
    unittest.main()