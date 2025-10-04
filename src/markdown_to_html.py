import re

from markdown_parser import *
from htmlnode import HTMLNode
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = []
    for block in markdown_to_blocks(markdown):
        type = block_to_block_type(block)

        match(type):
            case BlockType.PARAGRAPH:
                blocks.append(HTMLNode("p", None, text_to_children(block.replace("\n", " "))))
            case BlockType.HEADING:
                blocks.append(HTMLNode(f"h{len(re.search(r"#{1,6}", block)[0])}", None, text_to_children(block.strip("# "))))
            case BlockType.CODE:
                blocks.append(HTMLNode("pre", None, [text_node_to_html_node(TextNode(block.strip("```").lstrip("\n"), TextType.CODE))]))
            case BlockType.QUOTE:
                blocks.append(HTMLNode("blockquote", None, text_to_children(block.replace("> ", ""))))
            case BlockType.UNORDERED_LIST:
                children = []
                for line in block.split("\n"):
                    children.append(HTMLNode("li", None, text_to_children(line.strip("- "))))
                blocks.append(HTMLNode("ul", None, children))
            case BlockType.ORDERED_LIST:
                children = []
                for line in block.split("\n"):
                    children.append(HTMLNode("li", None, text_to_children(re.sub(r"\d+\. ", "", line))))
                blocks.append(HTMLNode("ol", None, children))
            

    return HTMLNode("div", None, blocks)

def text_to_children(text):
    children = []
    for textnode in text_to_textnodes(text):
        children.append(text_node_to_html_node(textnode))
    return children