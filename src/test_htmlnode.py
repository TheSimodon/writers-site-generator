import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # Tests eq and not eqal types as well as types in general
    def test_eq(self):
        node = HTMLNode("a", "This is a text", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "This is a text", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("a", "This is a text", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "This is a text", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("a", "This is a text", None, {"href": "https://www.google.com"})
        self.assertEqual(f"HTMLNode(a, This is a text, children: None, {{'href': 'https://www.google.com'}})", repr(node))
