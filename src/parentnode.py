from typing import override
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if self.tag is None:
            raise ValueError("There must be a tag for ParentNode")
        if self.children is None:
            raise ValueError("There must be children in ParentNode")
        self.tag = tag
        self.children = children
        self.props = props

        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        pass
