class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes a new HTMLNode.
        Parameters:
        - tag (str): The HTML tag name (e.g., "p", "a", "h1").
        - value (str): The text content of the HTML element.
        - children (list of HTMLNode): Child HTMLNode objects nested inside this node.
        - props (dict): HTML attributes as key-value pairs (e.g., {"href": "https://example.com"}).
        """
        # Assign the tag name (e.g., "div", "p", etc.)
        self.tag = tag
        # Assign the raw string value (e.g., inner text content)
        self.value = value
        # If no children are passed, default to an empty list
        self.children = children or []
        # If no props (HTML attributes) are passed, default to an empty dictionary
        self.props = props or {}

  
    def to_html(self):
        """
        Placeholder method to convert the node to its HTML string representation.
        This should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

  
    def props_to_html(self):
        """
        Converts the props dictionary to a string of HTML attributes.

        Returns:
        A string like ' href="https://example.com" class="link"'
        If props is empty, returns an empty string.
        """
        if not self.props:
            return ""
        # Create a string of key="value" pairs separated by spaces
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        # Prepend a space so that attributes appear correctly in HTML (e.g., <a href="...">)
        return f" {props_str}"

    def __repr__(self):
        """
        Returns a string representation of the HTMLNode for debugging.
        """
        return (f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
                f"children={self.children!r}, props={self.props!r})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        Initializes a LeafNode. Unlike HTMLNode, children are not allowed,
        and a value is required.

        Parameters:
        - tag (str or None): The HTML tag name. If None, it will render as raw text.
        - value (str): The inner text content (required).
        - props (dict): Optional HTML attributes.
        """
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        """
        Renders this leaf node as an HTML string.

        - If no tag: returns raw text.
        - If tag: returns HTML tag with props and value inside.
        """
        if self.value is None:
            raise ValueError("LeafNode must have a value to render.")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
