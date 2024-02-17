from abc import ABC, abstractmethod

# Step 1: Define the Flyweight interface
class Flyweight(ABC):
    """
    The Flyweight interface declares a method for accepting extrinsic state
    and performing operations based on it.
    """

    @abstractmethod
    def operation(self, extrinsic_state):
        """
        Operation method accepting extrinsic state as input.
        """
        pass

# Step 2: Create concrete flyweight classes
class ConcreteFlyweight(Flyweight):
    """
    ConcreteFlyweight implements the Flyweight interface and stores intrinsic state.
    """

    def __init__(self, intrinsic_state):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        return f"ConcreteFlyweight: Intrinsic State - {self._intrinsic_state}, Extrinsic State - {extrinsic_state}"

# Step 3: Implement the Flyweight Factory
class FlyweightFactory:
    """
    FlyweightFactory manages flyweight objects and ensures their uniqueness.
    """

    _flyweights = {}

    @staticmethod
    def get_flyweight(key):
        """
        Retrieve or create a flyweight object based on the provided key.
        """
        if key not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[key] = ConcreteFlyweight(key)
        return FlyweightFactory._flyweights[key]

# Step 4: Define the client class
class Client:
    """
    Client class represents objects that use flyweight objects.
    """

    def __init__(self, key):
        self._flyweight = FlyweightFactory.get_flyweight(key)

    def operation(self, extrinsic_state):
        """
        Perform an operation using the flyweight object and extrinsic state.
        """
        return self._flyweight.operation(extrinsic_state)

# Example usage
if __name__ == "__main__":
    client1 = Client("shared")
    client2 = Client("shared")
    client3 = Client("unique")

    print(client1.operation("state 1"))  # Output: ConcreteFlyweight: Intrinsic State - shared, Extrinsic State - state 1
    print(client2.operation("state 2"))  # Output: ConcreteFlyweight: Intrinsic State - shared, Extrinsic State - state 2
    print(client3.operation("state 3"))  # Output: ConcreteFlyweight: Intrinsic State - unique, Extrinsic State - state 3
