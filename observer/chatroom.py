from abc import ABC, abstractmethod

# Step 1: The ChatRoom - Publisher
class ChatRoom:
    def __init__(self):
        self._participants = set()

    def join(self, participant):
        """Adds a new participant to the chat room."""
        self._participants.add(participant)

    def leave(self, participant):
        """Removes a participant from the chat room."""
        self._participants.remove(participant)

    def broadcast(self, message):
        """Sends a message to all participants in the chat room."""
        for participant in self._participants:
            participant.receive(message)


# Step 2: Participant - Subscriber Interface
class Participant(ABC):
    @abstractmethod
    def receive(self, message):
        """Abstract method for receiving messages."""
        pass


# Step [3]: ChatMember - Concrete Subscribers
class ChatMember(Participant):
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        """Receives and displays the message."""
        print(f"{self.name} received: {message}")


# Step [4]: Client
if __name__ == "__main__":
    # Create a chat room
    general_chat = ChatRoom()

    # Create participants
    user1 = ChatMember("User1")
    user2 = ChatMember("User2")
    user3 = ChatMember("User3")

    # Participants join the chat room
    general_chat.join(user1)
    general_chat.join(user2)
    general_chat.join(user3)

    # Send a message to the chat room
    general_chat.broadcast("Welcome to the chat!")
