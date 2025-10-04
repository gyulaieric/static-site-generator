class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        if not self.tag:
            return self.value
        result = ""
        if self.children:
            for child in self.children:
                result += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"

    def props_to_html(self):
        if not self.props:
            return ""
        html = ""
        for prop, value in self.props.items():
            html += f' {prop}="{value}"'
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"