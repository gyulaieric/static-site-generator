from textnode import TextType, TextNode
from markdown_to_html import *

def main():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """


    print(markdown_to_html_node(md).to_html())

main()