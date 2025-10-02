from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
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