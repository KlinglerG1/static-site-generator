import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_extract_single_image(self):
        from inline_markdown import extract_markdown_images
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_multiple_images(self):
        from inline_markdown import extract_markdown_images
        text = "![first](http://a.com/1.png) and ![second](http://a.com/2.jpg)"
        expected = [("first", "http://a.com/1.png"), ("second", "http://a.com/2.jpg")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_no_images(self):
        from inline_markdown import extract_markdown_images
        text = "No images here!"
        self.assertListEqual(extract_markdown_images(text), [])

    def test_extract_single_link(self):
        from inline_markdown import extract_markdown_links
        text = "Here is a [link](https://example.com)"
        expected = [("link", "https://example.com")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_extract_multiple_links(self):
        from inline_markdown import extract_markdown_links
        text = "[Google](https://google.com) and [Bing](https://bing.com)"
        expected = [("Google", "https://google.com"), ("Bing", "https://bing.com")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_extract_no_links(self):
        from inline_markdown import extract_markdown_links
        text = "No links here!"
        self.assertListEqual(extract_markdown_links(text), [])

    def test_image_and_link_together(self):
        from inline_markdown import extract_markdown_links, extract_markdown_images
        text = "Check this ![img](http://img.com/pic.png) and [link](http://site.com)"
        self.assertListEqual(extract_markdown_images(text), [("img", "http://img.com/pic.png")])
        self.assertListEqual(extract_markdown_links(text), [("link", "http://site.com")])


if __name__ == "__main__":
    unittest.main()
