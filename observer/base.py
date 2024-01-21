from abc import ABC, abstractmethod


# Step 1: The Subject
class Subject(ABC):
    """
    The Subject class represents the object being observed.
    """

    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        """Adds an observer to the subject's list."""
        self._observers.add(observer)

    def detach(self, observer):
        """Removes an observer from the subject's list."""
        self._observers.remove(observer)

    def notify_observers(self):
        """Notifies all attached observers."""
        for observer in self._observers:
            observer.update()


# Step 2: The Observer Interface
class Observer(ABC):
    """
    The Observer interface declares the update method, which concrete observers must
    implement.
    """

    @abstractmethod
    def update(self):
        """Abstract method for receiving updates."""
        pass


# Step 3: Concrete Observer
class ConcreteObserver(Observer):
    """
    The ConcreteObserver class implements the update method and holds state that
    should stay consistent with the subject's state.
    """

    def __init__(self, name):
        self.name = name

    def update(self):
        """Receives notification and prints it."""
        print(f"{self.name} has been notified.")


# Step [4]: Client
if __name__ == "__main__":
    # Create a subject
    subject = Subject()

    # Create observers
    observer1 = ConcreteObserver("Observer1")
    observer2 = ConcreteObserver("Observer2")
    observer3 = ConcreteObserver("Observer3")

    # Attach observers to the subject
    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)

    # Notify observers
    subject.notify_observers()
