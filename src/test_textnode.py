import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Same text", TextType.ITALIC)
        node2 = TextNode("Same text", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url_difference(self):
        node1 = TextNode("Link", TextType.LINK, url="https://example.com")
        node2 = TextNode("Link", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_equal_with_url(self):
        node1 = TextNode("Image", TextType.IMAGE, url="https://img.com/a.png")
        node2 = TextNode("Image", TextType.IMAGE, url="https://img.com/a.png")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
