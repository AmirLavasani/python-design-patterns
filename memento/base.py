class Originator:
    """Originator creates and restores object states."""
    def __init__(self, state):
        """
        Initialize Originator with a state.

        Args:
        state (any): Initial state of the object.
        """
        self._state = state

    def create_memento(self):
        """
        Create a memento (snapshot) of the current state.

        Returns:
        Memento: A memento object storing the current state.
        """
        return Memento(self._state)

    def restore(self, memento):
        """
        Restore object's state from a memento.

        Args:
        memento (Memento): Memento object containing a saved state.
        """
        self._state = memento.get_state()

    def set_state(self, state):
        """
        Set the state of the object.

        Args:
        state (any): New state of the object.
        """
        self._state = state

    def get_state(self):
        """
        Retrieve the current state of the object.

        Returns:
        any: Current state of the object.
        """
        return self._state


class Memento:
    """Memento stores the state of an Originator object."""
    def __init__(self, state):
        """
        Initialize Memento with a state.

        Args:
        state (any): State to be stored in the memento.
        """
        self._state = state

    def get_state(self):
        """
        Retrieve the stored state from the memento.

        Returns:
        any: Stored state in the memento.
        """
        return self._state
    

class Caretaker:
    """Caretaker manages mementos and provides them upon request."""
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        """
        Add a memento to the caretaker's collection.

        Args:
        memento (Memento): Memento object to be stored.
        """
        self._mementos.append(memento)

    def get_memento(self, index):
        """
        Retrieve a memento from the caretaker's collection by index.

        Args:
        index (int): Index of the memento to be retrieved.

        Returns:
        Memento: Memento object retrieved based on the index.
        """
        return self._mementos[index]


if __name__ == "__main__":
    # Instantiate classes
    originator = Originator("Initial state")
    caretaker = Caretaker()

    # Store object state
    caretaker.add_memento(originator.create_memento())

    # Modify object state
    originator.set_state("Modified state")

    # Print current state
    print("Current state:", originator.get_state())

    # Restore object state
    originator.restore(caretaker.get_memento(0))

    # Print restored state
    print("Restored state:", originator.get_state())