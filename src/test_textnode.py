import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    
    # Tests eq and not eqal types as well as types in general
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        for type in TextType:
            node2 = TextNode("This is a text node", type)
            if type != TextType.BOLD:
                self.assertNotEqual(node, node2)
            else:
                self.assertEqual(node, node2)

    def test_is_type(self):
        for type in TextType:
            node = TextNode(f"This is a *{type}* text node", type)
            self.assertIn(node.text_type, TextType)

    # Test eq and not equal URL and if None is given if no url is set
    def test_is_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_is_url_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.your_mom.de")
        self.assertNotEqual(node.url, None)

    def test_is_url_eq_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertEqual(node.url, node2.url)
    
    def test_is_url_eq_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.your_mom.de") 
        node2 = TextNode("This is another text node", TextType.ITALIC, "www.your_mom.de")
        self.assertEqual(node.url, node2.url)

    def test_is_url_not_eq_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.your_mom.de") 
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node.url, node2.url)

    def test_is_url_not_eq_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.your_mom.de") 
        node2 = TextNode("This is another text node", TextType.ITALIC, "www.your_dad.de")
        self.assertNotEqual(node.url, node2.url)

    # Test for repr function
    def test_repr(self):
        for type in TextType:
            node = TextNode(f"This is a {type.value} node", type.value, f"https://www.{type.value}.com")
            self.assertEqual(f"TextNode(This is a {type.value} node, {type.value}, https://www.{type.value}.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
