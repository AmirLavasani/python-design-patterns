class Singleton:
    """
    Singleton design pattern implementation in Python.

    This class ensures that only one instance of the Singleton class exists
    throughout the lifetime of the application.

    Usage:
    >>> s1 = Singleton()
    >>> s2 = Singleton()
    >>> s1 is s2  # Both references point to the same instance
    True

    Attributes:
        _instance (Singleton): The unique instance of the Singleton class.

    Methods:
        __new__(cls): Creates a new instance only if one does not already exist.

    Note:
        This implementation uses the "lazy initialization" approach to create
        the Singleton instance when it is first requested.

    """

    _instance = None

    def __new__(cls):
        """
        Create a new instance of the Singleton class if one does not already exist.

        Returns:
            Singleton: The unique instance of the Singleton class.

        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

def main():
    # Create two Singleton instances
    s1 = Singleton()
    s2 = Singleton()

    # Check if both references point to the same instance
    print("Is s1 the same instance as s2?", s1 is s2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()