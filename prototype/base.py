import copy

class Prototype:
    """
    Prototype class to demonstrate object cloning using deepcopy.

    Attributes:
        data (list): A list attribute initialized as an empty list.
    """

    def __init__(self):
        """Initialize the Prototype instance."""
        self.data = []  # Initialize data attribute as an empty list

    def clone(self):
        """
        Create a deep copy of the current Prototype instance.

        Returns:
            Prototype: A new instance identical to the original Prototype.
        """
        return copy.deepcopy(self)  # Perform deep copy to create a clone


def main():
    # Create a prototype
    prototype_instance = Prototype()  # Instantiate Prototype class
    print(f"Prototype data: {prototype_instance.data}")

    # Clone the prototype
    clone_instance = prototype_instance.clone()  # Create a cloned instance
    print(f"Clone data before modification: {clone_instance.data}")

    # Modify data in the cloned instance
    clone_instance.data.append(1)
    print(f"Clone data after modification: {clone_instance.data}")

    # Original prototype remains unaffected
    print(f"Prototype data after clone modification: {prototype_instance.data}")


if __name__ == "__main__":
    main()