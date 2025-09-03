import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "hello world", None, {"href": "https://www.google.com", "target": "_blank"})        
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def test_props_to_html(self):
        node = HTMLNode("i", None, None, {"src": "https://www.boot.dev/img/bootdev-logo-full-small.webp"})        
        self.assertEqual(node.props_to_html(), ' src="https://www.boot.dev/img/bootdev-logo-full-small.webp"')
    def test_props_to_html(self):
        node = HTMLNode("i")        
        self.assertEqual(node.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()