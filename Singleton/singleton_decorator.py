def singleton(cls):
    """
    A decorator to implement the Singleton design pattern.

    This decorator ensures that only one instance of a class exists
    throughout the lifetime of the application.

    Args:
        cls (class): The class to which the decorator is applied.

    Returns:
        function: A closure function that handles class instantiation and instance retrieval.

    Usage:
    >>> @singleton
    ... class SingletonClass:
    ...     def __init__(self, data):
    ...         self.data = data
    ...     def display(self):
    ...         print(f"Singleton instance with data: {self.data}")
    >>> instance1 = SingletonClass("Instance 1")
    >>> instance2 = SingletonClass("Instance 2")
    >>> instance1.display()
    Singleton instance with data: Instance 1
    >>> instance2.display()  # Both references point to the same instance
    Singleton instance with data: Instance 1

    """

    instances = {}  # Dictionary to store instances of different classes

    def get_instance(*args, **kwargs):
        """
        Create a new instance if it doesn't exist, or return the existing one.

        Args:
            *args: Positional arguments for class initialization.
            **kwargs: Keyword arguments for class initialization.

        Returns:
            cls: The unique instance of the class.

        """
        if cls not in instances:
            # Create a new instance and store it
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]  # Return the existing instance
    
    # Return the closure function for class instantiation
    return get_instance  


@singleton  # Applying the singleton decorator
class SingletonClass:
    """
    A class using the Singleton design pattern via decorator.

    Here goes our class's business logic without concerning about
    handling the intricacies of the singleton pattern.

    Example:
    >>> instance1 = SingletonClass("Instance 1")
    >>> instance2 = SingletonClass("Instance 2")
    >>> instance1.display()
    Singleton instance with data: Instance 1
    >>> instance2.display()  # Both references point to the same instance
    Singleton instance with data: Instance 1

    """

    def __init__(self, data):
        """
        Initialize the SingletonClass with data.

        Args:
            data (str): Data to be stored in the instance.

        """
        self.data = data

    def display(self):
        """
        Display the data stored in the Singleton instance.

        """
        print(f"Singleton instance with data: {self.data}")


def main():
    # Creating instances of SingletonClass using the decorator
    instance1 = SingletonClass("Instance 1")
    instance2 = SingletonClass("Instance 2")

    # Check if both references point to the same instance
    print("Is instance1 the same instance as instance2?", instance1 is instance2)


if __name__ == "__main__":
    main()