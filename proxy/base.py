class RealSubject:
    """The Real Subject represents the actual object that the Proxy will control access to."""

    def perform_operation(self):
        """Perform a time-consuming operation.

        Returns:
            str: A message indicating the operation.
        """
        return "RealSubject: Performing the operation"


class Proxy:
    """The Proxy represents the Proxy object. It controls access to the RealSubject."""

    def __init__(self):
        self._real_subject = None

    def perform_operation(self):
        """The Proxy delegates the 'perform_operation' call to the RealSubject, but it only creates the
        RealSubject instance when called for the first time.

        Returns:
            str: A message indicating the operation being controlled by the Proxy.
        """
        if self._real_subject is None:
            print("Proxy: Creating a RealSubject for the first time.")
            self._real_subject = RealSubject()
        return (
            f"Proxy: Controlling access to ({self._real_subject.perform_operation()})"
        )


def main():
    # Create a Proxy object
    proxy = Proxy()

    # Call perform_operation on the Proxy
    print(proxy.perform_operation())
    # Output: 
    # Proxy: Creating a RealSubject for the first time.
    # Proxy: Controlling access to (RealSubject: Performing the operation)

    # The RealSubject is created only when perform_operation is called for the first time
    # Subsequent calls to perform_operation will use the existing RealSubject instance
    print(proxy.perform_operation()) 
    # Output: 
    # Proxy: Controlling access to (RealSubject: Performing the operation)


if __name__ == "__main__":
    main()
