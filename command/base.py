from abc import ABC, abstractmethod

# Step 1: Define the Command Interface

class Command(ABC):
    """
    Abstract base class for Command objects.
    Concrete commands must implement the 'process' method.
    """

    def __init__(self, receiver):
        """
        Initialize a command with a receiver.

        Args:
            receiver: The object that will perform the action when the command is executed.
        """
        self.receiver = receiver

    @abstractmethod
    def process(self):
        """
        Execute the command's action.
        """
        pass

# Step 2: Implement a Concrete Command

class ConcreteCommand(Command):
    """
    Concrete command that performs an action through the receiver.
    """

    def __init__(self, receiver):
        """
        Initialize the concrete command.

        Args:
            receiver: The object that will perform the action when the command is executed.
        """
        self.receiver = receiver

    def process(self):
        """
        Execute the command by delegating the action to the receiver.
        """
        self.receiver.perform_action()

# Step 3: Create a Receiver

class Receiver:
    """
    Receiver class that performs an action.
    """

    def perform_action(self):
        """
        Perform the action.
        """
        print('Action performed in receiver.')

# Step 4: Create a Client and an Invoker

class Invoker:
    """
    Invoker class that triggers the execution of a command.
    """

    def __init__(self):
        self.cmd = None

    def command(self, cmd):
        """
        Set the command to be executed.

        Args:
            cmd: The command to be executed.
        """
        self.cmd = cmd

    def execute(self):
        """
        Execute the command by invoking its 'process' method.
        """
        self.cmd.process()

if __name__ == "__main__":
    # Create a Receiver object
    receiver = Receiver()

    # Create a concrete command and set its receiver
    cmd = ConcreteCommand(receiver)

    # Create an Invoker
    invoker = Invoker()

    # Set the command for the Invoker
    invoker.command(cmd)

    # Execute the command
    invoker.execute()