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

class Adapter:
    """
    Adapter class to make the OldSystem compatible with the new system.

    >>> old_system = OldSystem()
    >>> adapter = Adapter(old_system)
    >>> adapter.new_operation()
    'Adapter: Legacy operation'
    """

    def __init__(self, old_system):
        """
        Initialize the Adapter with an instance of OldSystem.

        Args:
            old_system (OldSystem): An instance of the OldSystem class.
        """
        self.old_system = old_system

    def new_operation(self):
        """
        Perform a new operation using the OldSystem's legacy operation.

        Returns:
            str: A string representing the result of the new operation.
        """
        return f"Adapter: {self.old_system.legacy_operation()}"

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
    old_system = OldSystem()
    adapter = Adapter(old_system)
    client_code(adapter)