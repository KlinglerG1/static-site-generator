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

def test_leaf_node():
    # Basic tag with value
    assert LeafNode("p", "Hello, world!").to_html() == "<p>Hello, world!</p>"

    # Tag with props
    assert LeafNode("a", "Link", props={"href": "https://example.com"}).to_html() == \
           '<a href="https://example.com">Link</a>'

    # Tag with multiple props
    assert LeafNode("img", "Image", props={"src": "image.png", "alt": "A picture"}).to_html() == \
           '<img src="image.png" alt="A picture">Image</img>'

    # Heading tag
    assert LeafNode("h1", "Title").to_html() == "<h1>Title</h1>"

    # Bold and italic
    assert LeafNode("b", "Bold text").to_html() == "<b>Bold text</b>"
    assert LeafNode("i", "Italic text").to_html() == "<i>Italic text</i>"

    # Span with class
    assert LeafNode("span", "Label", props={"class": "highlight"}).to_html() == \
           '<span class="highlight">Label</span>'

    # Raw text (no tag)
    assert LeafNode(None, "Just some text").to_html() == "Just some text"

    # HTML-escaped characters in value
    assert LeafNode("p", "<unsafe>").to_html() == "<p><unsafe></p>"  # note: this is raw, not escaped

    # Empty string as value is still valid
    assert LeafNode("p", "").to_html() == "<p></p>"

    # Value is required (should raise)
    try:
        LeafNode("p", None)
    except ValueError as e:
        assert str(e) == "LeafNode must have a value."

    # to_html() should not allow rendering if value is None
    try:
        bad_node = LeafNode("div", "something")
        bad_node.value = None  # simulate corruption
        bad_node.to_html()
    except ValueError as e:
        assert str(e) == "LeafNode must have a value to render."

    print("All LeafNode tests passed.")
