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
