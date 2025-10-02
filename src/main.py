from textnode import TextType, TextNode
from markdown_parser import split_nodes_image, split_nodes_link

def main():
    text = TextNode("This is text with a", TextType.TEXT)
    print(split_nodes_link([text]))

main()