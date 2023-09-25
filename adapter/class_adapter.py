class OldSystem:
    """
    Represents an old legacy system with a legacy operation.

    >>> old_system = OldSystem()
    >>> old_system.legacy_operation()
    'Legacy operation'
    """

    def legacy_operation(self):
        """
        Perform the legacy operation.

        Returns:
            str: A string representing the result of the legacy operation.
        """
        return "Legacy operation"

class Adapter(OldSystem):
    """
    Adapter class to make the OldSystem compatible with the new system using inheritance.

    >>> adapter = Adapter()
    >>> adapter.new_operation()
    'Adapter: Legacy operation'
    """

    def new_operation(self):
        """
        Perform a new operation using the OldSystem's legacy operation.

        Returns:
            str: A string representing the result of the new operation.
        """
        return f"Adapter: {self.legacy_operation()}"

    def legacy_operation(self):
        """
        Override the legacy_operation method to provide compatibility.

        Returns:
            str: A string representing the result of the legacy operation.
        """
        return super().legacy_operation()

# Client code
def client_code(adapter):
    """
    Execute client code that uses the Adapter to perform a new operation.

    Args:
        adapter (Adapter): An instance of the Adapter class.
    """
    result = adapter.new_operation()
    print(result)

if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)