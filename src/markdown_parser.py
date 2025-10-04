import re
from textnode import TextNode, TextType

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or delimiter not in old_node.text:
            new_nodes.append(old_node)
        else:
            node = old_node.text.split(delimiter)
            if len(node) < 3 or len(node) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            for i in range(len(node)):
                if i % 2 == 0:
                    if node[i] == "":
                        continue
                    new_nodes.append(TextNode(node[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(node[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            images = extract_markdown_images(old_node.text)
            remaining = old_node.text
            for alt, url in images:
                before, after = remaining.split(f"![{alt}]({url})", 1)
                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                remaining = after
            if remaining != "":
                    new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            links = extract_markdown_links(old_node.text)
            remaining = old_node.text
            for anchor, url in links:
                before, after = remaining.split(f"[{anchor}]({url})", 1)
                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(anchor, TextType.LINK, url))
                remaining = after
            if remaining != "":
                    new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    result = [TextNode(text, TextType.TEXT)]
    delimiters = {
        "**": TextType.BOLD,
        "_": TextType.ITALIC,
        "`": TextType.CODE
        }
    for delimiter, text_type in delimiters.items():
        result = split_nodes_delimiter(result, delimiter, text_type)
    
    result = split_nodes_image(result)
    result = split_nodes_link(result)

    return result


def markdown_to_blocks(markdown):
    return list(filter(None, map(str.strip, markdown.split("\n\n"))))

def block_to_block_type(block):
    if re.search(r"#{1,6} ", block[:7]):
        return BlockType.HEADING
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    if block[0] == ">":
        if "\n" in block:
            for line in block.split("\n"):
                if line[0] != ">":
                    return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block[0:2] == "- ":
        if "\n" in block:
            for line in block.split("\n"):
                if line[0:2] != "- ":
                    return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block[0:3] == "1. ":
        if "\n" in block:
            lines = block.split("\n")
            for i in range(1, len(lines)):
                if lines[i][0:3] != f"{i + 1}. ":
                    return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH