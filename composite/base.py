from abc import ABC, abstractmethod

# Step 1: Define the Component Interface
class Component(ABC):
    """The Component interface sets the common method for all components."""

    @abstractmethod
    def operation(self):
        """The operation method needs to be implemented by Leaf and Composite classes."""
        pass


# Step 2: Create Leaf Class
class Leaf(Component):
    """Leaf represents individual objects that don’t contain other elements."""

    def __init__(self, name):
        self.name = name

    def operation(self):
        """Operation method for Leaf."""
        return f"Leaf: {self.name}"


# Step 3: Create Composite Class
class Composite(Component):
    """Composite acts as a container that can hold both Leaf and other Composite instances."""

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        """Method to add elements to the Composite."""
        self.children.append(component)

    def remove(self, component):
        """Method to remove elements from the Composite."""
        self.children.remove(component)

    def operation(self):
        """Operation method for Composite."""
        results = [f"Composite: {self.name}"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)
    

# Step 3: Demonstrate the Usage in Main
if __name__ == "__main__":
    # Creating Leaf objects
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")
    leaf3 = Leaf("Leaf 3")

    # Creating Composite objects
    composite1 = Composite("Composite 1")
    composite2 = Composite("Composite 2")

    # Adding Leaf elements to Composite 1
    composite1.add(leaf1)
    composite1.add(leaf2)

    # Adding Composite 1 and Leaf 3 to Composite 2
    composite2.add(composite1)
    composite2.add(leaf3)

    # Displaying the structure and executing operations
    print(composite2.operation())
