from textnode import TextNode, TextType
import re
import unittest


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    """
    Extracts markdown images from the given text.
    Returns a list of tuples: (alt text, image URL)
    """
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)


def extract_markdown_links(text):
    """
    Extracts markdown links from the given text.
    Returns a list of tuples: (anchor text, URL)
    """
    pattern = r'(?<!!)\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)
