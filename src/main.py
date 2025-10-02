from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    text_node = TextNode("test", TextType.BOLD)
    print(text_node_to_html_node(text_node))

main()