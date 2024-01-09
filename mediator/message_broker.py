from abc import ABC, abstractmethod


class Participant:
    """
    Represents a message participant.
    """
    def __init__(self, mediator, name):
        self._mediator = mediator
        self.name = name

    def send_message(self, message):
        """
        Sends a message through the mediator.
        """
        self._mediator.send_message(message, self)

    def receive_message(self, message):
        """
        Receives and processes messages from the mediator.
        """
        print(f"{self.name} received message: {message}")


class MessageBroker(ABC):
    """
    Mediator interface (Message Broker) declares message handling methods.
    """
    @abstractmethod
    def send_message(self, message, participant):
        """
        Sends a message to a participant.
        """
        pass


class ConcreteMessageBroker(MessageBroker):
    """
    Concrete Message Broker manages message passing between participants.
    """
    def __init__(self):
        self._participants = []

    def add_participant(self, participant):
        """
        Adds a participant to the broker.
        """
        self._participants.append(participant)

    def send_message(self, message, participant):
        """
        Sends a message to all participants except the sender.
        """
        for p in self._participants:
            if p != participant:
                p.receive_message(message)


if __name__ == "__main__":
    # Create message broker
    message_broker = ConcreteMessageBroker()

    # Create participants and link them to the broker
    participant1 = Participant(message_broker, "Participant 1")
    participant2 = Participant(message_broker, "Participant 2")

    # Add participants to the broker
    message_broker.add_participant(participant1)
    message_broker.add_participant(participant2)

    # Send messages through participants
    participant1.send_message("Hello from Participant 1")
    participant2.send_message("Hi from Participant 2")
