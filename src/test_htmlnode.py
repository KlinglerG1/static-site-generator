# src/test_htmlnode.py
from htmlnode import HTMLNode

def test_props_to_html_single_attr():
    node = HTMLNode(tag="a", props={"href": "https://example.com"})
    assert node.props_to_html() == ' href="https://example.com"', "Single attribute test failed"

def test_props_to_html_multiple_attrs():
    node = HTMLNode(tag="img", props={"src": "image.jpg", "alt": "An image", "class": "thumbnail"})
    html = node.props_to_html()
    # Order is not guaranteed in a dictionary, so we check for substrings
    assert 'src="image.jpg"' in html
    assert 'alt="An image"' in html
    assert 'class="thumbnail"' in html
    assert html.startswith(" ")  # Should start with a space

def test_repr_output():
    child = HTMLNode(tag="span", value="child")
    node = HTMLNode(tag="div", value="parent", children=[child], props={"id": "main"})
    repr_str = repr(node)
    assert "HTMLNode" in repr_str
    assert "tag='div'" in repr_str
    assert "value='parent'" in repr_str
    assert "children=[HTMLNode" in repr_str
    assert "props={'id': 'main'}" in repr_str
