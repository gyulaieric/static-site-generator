from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.tag:
            if not self.value:
                raise ValueError(f"{self}LeafNode does not have a value")
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"