from abc import ABC, abstractmethod


# 1. Abstract Factory Interface
class NotificationFactory(ABC):
    """Abstract Factory Interface

    This abstract class defines the interface for creating notification objects.

    Attributes:
        None

    Methods:
        create_email_notification(): Abstract method for creating an EmailNotification.
        create_sms_notification(): Abstract method for creating an SMSNotification.
        create_push_notification(): Abstract method for creating a PushNotification.
    """

    @abstractmethod
    def create_email_notification(self):
        pass

    @abstractmethod
    def create_sms_notification(self):
        pass

    @abstractmethod
    def create_push_notification(self):
        pass


# 2. Concrete Factories
class FastNotifFactory(NotificationFactory):
    """Concrete Factory for FastNotif

    This concrete factory class implements the NotificationFactory interface to create
    notification objects for the FastNotif provider.

    Methods:
        create_email_notification(): Creates a FastNotif email notification object.
        create_sms_notification(): Creates a FastNotif SMS notification object.
        create_push_notification(): Creates a FastNotif push notification object.
    """

    def create_email_notification(self):
        return FastNotifEmailNotification()

    def create_sms_notification(self):
        return FastNotifSMSNotification()

    def create_push_notification(self):
        return FastNotifPushNotification()


class SendBlueFactory(NotificationFactory):
    """Concrete Factory for SendBlue

    This concrete factory class implements the NotificationFactory interface to create
    notification objects for the SendBlue provider.

    Attributes:
        None

    Methods:
        create_email_notification(): Creates a SendBlue email notification object.
        create_sms_notification(): Creates a SendBlue SMS notification object.
        create_push_notification(): Creates a SendBlue push notification object.
    """

    def create_email_notification(self):
        return SendBlueEmailNotification()

    def create_sms_notification(self):
        return SendBlueSMSNotification()

    def create_push_notification(self):
        return SendBluePushNotification()


# 3. Abstract Products
class AbstractEmailNotification(ABC):
    """Abstract Product for Email Notifications

    This abstract class defines the interface for creating email notifications.

    Methods:
        send(): Abstract method for sending the email notification.
        format_content(): Abstract method for formatting the email content.
    """

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_content(self):
        pass


class AbstractSMSNotification(ABC):
    """Abstract Product for SMS Notifications

    This abstract class defines the interface for creating SMS notifications.

    Methods:
        send(): Abstract method for sending the SMS notification.
        encode_message(): Abstract method for encoding the SMS message.
    """

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def encode_message(self):
        pass


class AbstractPushNotification(ABC):
    """Abstract Product for Push Notifications

    This abstract class defines the interface for creating push notifications.

    Methods:
        send(): Abstract method for sending the push notification.
        format_payload(): Abstract method for formatting the push notification payload.
    """

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_payload(self):
        pass


# 4. Concrete Products
class FastNotifEmailNotification(AbstractEmailNotification):
    """Concrete Product for Email Notifications via FastNotif"""

    def send(self):
        print("Sending Email via FastNotif")

    def format_content(self):
        print("Formatting Email content")


class FastNotifSMSNotification(AbstractSMSNotification):
    """Concrete Product for SMS Notifications via FastNotif"""

    def send(self):
        print("Sending SMS via FastNotif")

    def encode_message(self):
        print("Encoding SMS message")


class FastNotifPushNotification(AbstractPushNotification):
    """Concrete Product for Push Notifications via FastNotif"""

    def send(self):
        print("Sending Push Notification via FastNotif")

    def format_payload(self):
        print("Formatting Push Notification payload")


class SendBlueEmailNotification(AbstractEmailNotification):
    """Concrete Product for Email Notifications via SendBlue"""

    def send(self):
        print("Sending Email via SendBlue")

    def format_content(self):
        print("Formatting Email content")


class SendBlueSMSNotification(AbstractSMSNotification):
    """Concrete Product for SMS Notifications via SendBlue"""

    def send(self):
        print("Sending SMS via SendBlue")

    def encode_message(self):
        print("Encoding SMS message")


class SendBluePushNotification(AbstractPushNotification):
    """Concrete Product for Push Notifications via SendBlue"""

    def send(self):
        print("Sending Push Notification via SendBlue")

    def format_payload(self):
        print("Formatting Push Notification payload")


# Client Code
def send_notification(factory):
    """Send Notifications using the specified factory.

    This function demonstrates how to use the selected factory to create and send
    email, SMS, and push notifications.

    Args:
        factory (NotificationFactory): The factory object to create notifications.

    Returns:
        None
    """
    email_notification = factory.create_email_notification()
    sms_notification = factory.create_sms_notification()
    push_notification = factory.create_push_notification()

    email_notification.send()
    sms_notification.send()
    push_notification.send()


# Dictionary to map provider names to factory classes
factory_mapping = {
    "FastNotif": FastNotifFactory(),
    "SendBlue": SendBlueFactory(),
}


# Main Function to select Notification Factory
def select_notification_factory(provider):
    """Select and return the Notification Factory based on the provider.

    This function takes a provider name as input and returns the corresponding
    factory object.

    Args:
        provider (str): The name of the notification provider.

    Returns:
        NotificationFactory: The factory object for the selected provider.

    Raises:
        ValueError: If an invalid provider name is provided.
    """
    factory = factory_mapping.get(provider)
    if factory is None:
        raise ValueError("Invalid provider")
    return factory


# Example Usage
if __name__ == "__main__":
    provider = input("Enter the provider (FastNotif or SendBlue): ")
    notification_factory = select_notification_factory(provider)
    send_notification(notification_factory)