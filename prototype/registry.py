import copy

class Prototype:
    """Abstract prototype class defining the clone method."""

    def clone(self):
        """
        Create a deep copy of the prototype instance.

        Returns:
            Prototype: A new instance identical to the original Prototype.
        """
        return copy.deepcopy(self)

class ConcretePrototypeA(Prototype):
    """Concrete implementation of Prototype A."""

    def __init__(self, data):
        """Initialize ConcretePrototypeA instance with data."""
        self.data = data

class ConcretePrototypeB(Prototype):
    """Concrete implementation of Prototype B."""

    def __init__(self, data):
        """Initialize ConcretePrototypeB instance with data."""
        self.data = data

class PrototypeRegistry:
    """Registry to store and retrieve prototype instances."""

    def __init__(self):
        """Initialize PrototypeRegistry with an empty dictionary."""
        self.prototypes = {}

    def add_prototype(self, name, prototype):
        """
        Add a prototype instance to the registry.

        Args:
            name (str): Name/key to identify the prototype.
            prototype (Prototype): Prototype instance to add.
        """
        self.prototypes[name] = prototype

    def get_prototype(self, name):
        """
        Get a cloned instance of a prototype from the registry.

        Args:
            name (str): Name/key of the prototype to retrieve.

        Returns:
            Prototype: Cloned instance of the specified prototype.

        Raises:
            ValueError: If the specified prototype is not found in the registry.
        """
        if name in self.prototypes:
            return self.prototypes[name].clone()
        else:
            raise ValueError(f"Prototype '{name}' not found.")

# Create prototype instances
prototype_a = ConcretePrototypeA("Prototype A Data")
prototype_b = ConcretePrototypeB("Prototype B Data")

# Create and populate the Prototype Registry
registry = PrototypeRegistry()
registry.add_prototype("PrototypeA", prototype_a)
registry.add_prototype("PrototypeB", prototype_b)

# Clone prototypes from the registry
cloned_prototype_a = registry.get_prototype("PrototypeA")
cloned_prototype_b = registry.get_prototype("PrototypeB")

# Verify cloned data
print(cloned_prototype_a.data)  # Output: Prototype A Data
print(cloned_prototype_b.data)  # Output: Prototype B Data
