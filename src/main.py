from textnode import TextType, TextNode
from markdown_parser import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code``block` word", TextType.TEXT)
    print(split_nodes_delimiter([node], "`", TextType.CODE))

main()