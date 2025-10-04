from textnode import TextType, TextNode
from markdown_parser import *

def main():
    markdown = "1. This is a quote\n2. This is another quote"

    print(block_to_block_type(markdown))

main()