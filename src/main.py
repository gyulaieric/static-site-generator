from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    node = HTMLNode("a", "hello world", None, {"href": "https://www.google.com", "target": "_blank"})
    print(node.props_to_html())
main()