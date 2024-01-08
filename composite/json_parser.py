from abc import ABC, abstractmethod

class JSONComponent(ABC):
    """The Component interface sets the common method for all components in the JSON parser."""

    @abstractmethod
    def parse(self):
        """The parse method needs to be implemented by Leaf and Composite classes."""
        pass


class JSONLeaf(JSONComponent):
    """Leaf represents individual elements in the JSON structure."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def parse(self):
        """Parsing method for Leaf."""
        return f"Parsing JSON Leaf: {self.key}: {self.value}"


class JSONObject(JSONComponent):
    """Object represents JSON objects that can contain other JSON elements."""

    def __init__(self):
        self.children = []

    def add(self, component):
        """Method to add elements to the JSON Object."""
        self.children.append(component)

    def remove(self, component):
        """Method to remove elements from the JSON Object."""
        self.children.remove(component)

    def parse(self):
        """Parsing method for JSON Object."""
        results = []
        for child in self.children:
            results.append(child.parse())
        return "\n".join(results)


import json

def parse_json(json_string):
    # Parse JSON string
    data = json.loads(json_string)

    # Create root JSON Object
    root = JSONObject()

    # Create nodes based on JSON structure
    for key, value in data.items():
        if isinstance(value, dict):
            obj = JSONObject()
            for k, v in value.items():
                leaf = JSONLeaf(k, v)
                obj.add(leaf)
            root.add(obj)
        else:
            leaf = JSONLeaf(key, value)
            root.add(leaf)

    return root

if __name__ == "__main__":
    # Sample JSON string
    sample_json = '{"name": "John Doe", "age": 30, "address": {"city": "New York", "zip": 10001}}'

    # Parsing JSON string and creating nodes
    json_structure = parse_json(sample_json)
    # print(json_structure)

    # Displaying the structure and executing parsing
    print(json_structure.parse())
