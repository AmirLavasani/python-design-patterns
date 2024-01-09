from abc import ABC, abstractmethod


class Component:
    """
    Represents a component with business logic.
    """
    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, message):
        """
        Sends a message to the mediator.
        """
        self._mediator.notify(message)

    def receive(self, message):
        """
        Receives and processes messages from the mediator.
        """
        print(f"Component received message: {message}")


class Mediator(ABC):
    """
    Mediator interface declares communication methods.
    """
    @abstractmethod
    def notify(self, message):
        """
        Notify method for sending messages to components.
        """
        pass


class ConcreteMediator(Mediator):
    """
    Concrete Mediator manages communication between components.
    """
    def __init__(self):
        self._components = []

    def add_component(self, component):
        """
        Adds a component to the mediator.
        """
        self._components.append(component)

    def notify(self, message):
        """
        Notifies all components with the message.
        """
        for component in self._components:
            component.receive(message)


if __name__ == "__main__":
    # Create mediator
    mediator = ConcreteMediator()

    # Create components and link them to the mediator
    component1 = Component(mediator)
    component2 = Component(mediator)

    # Add components to the mediator
    mediator.add_component(component1)
    mediator.add_component(component2)

    # Send messages through components
    component1.send("Hello from Component 1")
    component2.send("Hi from Component 2")