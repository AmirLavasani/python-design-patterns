from abc import ABC, abstractmethod

# Section 1: Abstract Middleware Base

class Middleware(ABC):
    """
    Abstract Middleware class serving as the base of the chain.
    """

    @abstractmethod
    def handle_request(self, request):
        """
        Handle the request; must be implemented by concrete classes.

        Args:
            request (dict): The HTTP request.

        Returns:
            dict or None: The updated HTTP request or None if processing is stopped.
        """
        pass

# Section 2: Concrete Middleware Implementations

class AuthenticationMiddleware(Middleware):
    """
    Middleware responsible for user authentication.

    >>> auth_middleware = AuthenticationMiddleware()
    >>> auth_middleware.handle_request({"user": "authentic_user"})
    Authentication middleware: Authenticated successfully

    >>> auth_middleware.handle_request({"user": "invalid_user"})
    Authentication middleware: Authentication failed
    """

    def handle_request(self, request):
        """
        Handle authentication or pass to the next middleware in the chain.

        Args:
            request (dict): The HTTP request.

        Returns:
            dict or None: The updated HTTP request or None if authentication fails.
        """
        if self.authenticate(request):
            print("Authentication middleware: Authenticated successfully")
            # Pass the request to the next middleware or handler in the chain.
            return request
        else:
            print("Authentication middleware: Authentication failed")
            # Stop the chain if authentication fails.
            return None

    def authenticate(self, request):
        """
        Implement authentication logic here.

        Args:
            request (dict): The HTTP request.

        Returns:
            bool: True if authentication is successful, else False.
        """
        # Authentication logic goes here.
        if request['user'] == 'authentic_user':
            return True
        return False

class LoggingMiddleware(Middleware):
    """
    Middleware responsible for logging requests.

    >>> logging_middleware = LoggingMiddleware()
    >>> logging_middleware.handle_request({"user": "username", "data": "valid_data"})
    Logging middleware: Logging request
    """

    def handle_request(self, request):
        """
        Handle request logging and pass to the next middleware in the chain.

        Args:
            request (dict): The HTTP request.

        Returns:
            dict: The HTTP request after logging.
        """
        print("Logging middleware: Logging request")
        # Pass the request to the next middleware or handler in the chain.
        return request

class DataValidationMiddleware(Middleware):
    """
    Middleware responsible for data validation.

    >>> data_validation_middleware = DataValidationMiddleware()
    >>> data_validation_middleware.handle_request({"data": "valid_data"})
    Data Validation middleware: Data is valid

    >>> data_validation_middleware.handle_request({"data": "invalid_data"})
    Data Validation middleware: Invalid data
    """

    def handle_request(self, request):
        """
        Handle data validation or pass to the next middleware in the chain.

        Args:
            request (dict): The HTTP request.

        Returns:
            dict or None: The updated HTTP request or None if data validation fails.
        """
        if self.validate_data(request):
            print("Data Validation middleware: Data is valid")
            # Pass the request to the next middleware or handler in the chain.
            return request
        else:
            print("Data Validation middleware: Invalid data")
            # Stop the chain if data validation fails.
            return None

    def validate_data(self, request):
        """
        Implement data validation logic here.

        Args:
            request (dict): The HTTP request.

        Returns:
            bool: True if data is valid, else False.
        """
        # Data validation logic goes here.
        if request['data'] == 'valid_data':
            return True
        return False


# Section 3: Request Handling Class and Client Code

class Chain:
    """Manages a chain of middleware for request processing."""

    def __init__(self):
        self.middlewares = []

    def add_middleware(self, middleware):
        """Add a middleware to the chain."""
        self.middlewares.append(middleware)

    def handle_request(self, request):
        """Handle the request by processing it through the middleware chain.

        Args:
            request (dict): The HTTP request.

        Returns:
            dict or None: The updated HTTP request or None if processing is stopped.
        """
        request_handled = True
        for middleware in self.middlewares:
            request = middleware.handle_request(request)
            if request is None:
                print("Request processing stopped.")
                request_handled = False
                break
        if request_handled:
            print("Request processing finished successfully.")

if __name__ == "__main__":
    # Create middleware instances.
    auth_middleware = AuthenticationMiddleware()
    logging_middleware = LoggingMiddleware()
    data_validation_middleware = DataValidationMiddleware()

    # Create the chain and add middleware.
    chain = Chain()
    chain.add_middleware(auth_middleware)
    chain.add_middleware(logging_middleware)
    chain.add_middleware(data_validation_middleware)

    print(f"{'*'*50}")
    print("Processing a valid request:")
    print(f"{'*'*50}")
    # Simulate an HTTP request.
    http_request = {"user": "authentic_user", "data": "valid_data"}
    chain.handle_request(http_request)

    print(f"{'*'*50}")
    print("Processing an invalid request:")
    print(f"{'*'*50}")
    # Simulate an HTTP request with invalid data.
    http_request = {"user": "authentic_user", "data": "invalid_data"}
    chain.handle_request(http_request)
