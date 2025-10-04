from textnode import TextType, TextNode
from markdown_parser import *

def main():
    markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.



- This is the first list item in a list block
- This is a list item
- This is another list item
    """

    print(markdown_to_blocks(markdown))

main()