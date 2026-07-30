import unittest

from leafnode import LeafNode


class TestLeafnode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Hey, you!")
        self.assertEqual(node.to_html(), "<a>Hey, you!</a>")

    def test_leaf_to_html_props(self):
        node = LeafNode(tag="a", value="Hey, you!", props={"test": "test"})
        self.assertEqual(node.to_html(), '<a test="test">Hey, you!</a>')

    def test_lead_to_html_no_tag(self):
        node = LeafNode(tag=None, value="Hey, you!")
        self.assertEqual(node.to_html(), 'Hey, you!')

if __name__ == "__main__":
    unittest.main()
