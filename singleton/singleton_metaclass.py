class SingletonMeta(type):
    """
    A metaclass for implementing the Singleton design pattern.

    This metaclass ensures that only one instance of a class exists
    throughout the lifetime of the application.

    Usage:
    >>> class MySingleton(metaclass=SingletonMeta):
    ...     def __init__(self, value):
    ...         self.value = value
    ...
    >>> instance1 = MySingleton(42)
    >>> instance2 = MySingleton(100)
    >>> instance1.value
    42
    >>> instance2.value  # Both references point to the same instance
    42

    Attributes:
        _instances (dict): A dictionary to store instances of Singleton classes.

    Methods:
        __call__(cls, *args, **kwargs): Creates a new instance only if one does not already exist.

    Note:
        This metaclass allows for creating Singleton classes without explicitly implementing the Singleton pattern
        logic in each class.

    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Create a new instance of the Singleton class if one does not already exist.

        Args:
            *args: Positional arguments for class initialization.
            **kwargs: Keyword arguments for class initialization.

        Returns:
            Singleton: The unique instance of the Singleton class.

        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    A class using the Singleton design pattern via metaclass.

    Here goes our class's business logic without concerning about
    handling the intricacies of the singleton pattern.

    Example:
    >>> instance1 = Singleton()
    >>> instance2 = Singleton()
    >>> instance1 is instance2  # Both references point to the same instance
    True

    """

    pass


def main():
    # Create two Singleton instances
    instance1 = Singleton()
    instance2 = Singleton()

    # Check if both references point to the same instance
    print("Is instance1 the same instance as instance2?", instance1 is instance2)


if __name__ == "__main__":   
    main()
    