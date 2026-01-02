from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        self.value = value
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        self.tag = tag
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to render HTML")
        if self.tag is None:
            return self.value
        if self.props:
            props = self.props_to_html()
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

