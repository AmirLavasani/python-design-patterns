# Step 1: Define the State Interface
class CheckoutState:
    """Interface defining the methods for various checkout states."""

    def add_item(self, item):
        """Add an item to the cart."""
        pass

    def review_cart(self):
        """Review the cart contents."""
        pass

    def enter_shipping_info(self, info):
        """Enter shipping information."""
        pass

    def process_payment(self):
        """Process the payment."""
        pass

# Step 2: Create Concrete State Classes
class EmptyCartState(CheckoutState):
    """Concrete state representing an empty cart."""

    def add_item(self, item):
        """Add an item to the cart and transition to ItemAddedState."""
        print("Item added to the cart.")
        return ItemAddedState()

    def review_cart(self):
        """Display inability to review an empty cart."""
        print("Cannot review an empty cart.")

    def enter_shipping_info(self, info):
        """Display inability to enter shipping info with an empty cart."""
        print("Cannot enter shipping info with an empty cart.")

    def process_payment(self):
        """Display inability to process payment with an empty cart."""
        print("Cannot process payment with an empty cart.")


class ItemAddedState(CheckoutState):
    """Concrete state representing a cart with added items."""

    def add_item(self, item):
        """Add an item to the cart."""
        print("Item added to the cart.")

    def review_cart(self):
        """Review cart contents and transition to CartReviewedState."""
        print("Reviewing cart contents.")
        return CartReviewedState()

    def enter_shipping_info(self, info):
        """Display inability to enter shipping info without reviewing the cart."""
        print("Cannot enter shipping info without reviewing the cart.")

    def process_payment(self):
        """Display inability to process payment without entering shipping info."""
        print("Cannot process payment without entering shipping info.")


class CartReviewedState(CheckoutState):
    """Concrete state representing a reviewed cart."""

    def add_item(self, item):
        """Display inability to add items after reviewing the cart."""
        print("Cannot add items after reviewing the cart.")

    def review_cart(self):
        """Display that the cart has already been reviewed."""
        print("Cart already reviewed.")

    def enter_shipping_info(self, info):
        """Enter shipping information and transition to ShippingInfoEnteredState."""
        print("Entering shipping information.")
        return ShippingInfoEnteredState(info)

    def process_payment(self):
        """Display inability to process payment without entering shipping info."""
        print("Cannot process payment without entering shipping info.")


class ShippingInfoEnteredState(CheckoutState):
    """Concrete state representing the entry of shipping information."""
    def __init__(self, info):
        self.info = info

    def add_item(self, item):
        """Display inability to add items after entering shipping info."""
        print("Cannot add items after entering shipping info.")

    def review_cart(self):
        """Display inability to review cart after entering shipping info."""
        print("Cannot review cart after entering shipping info.")

    def enter_shipping_info(self, info):
        """Display that shipping information has already been entered."""
        print("Shipping information already entered.")

    def process_payment(self):
        """Process payment with the entered shipping info."""
        print("Processing payment with the entered shipping info.")

# Step 3: Create the Context Class
class CheckoutContext:
    """Context class managing the checkout states."""

    def __init__(self):
        self.current_state = EmptyCartState()

    def add_item(self, item):
        """Add an item to the cart, updating the current state."""
        self.current_state = self.current_state.add_item(item)

    def review_cart(self):
        """Review the cart, updating the current state."""
        self.current_state = self.current_state.review_cart()

    def enter_shipping_info(self, info):
        """Enter shipping information, updating the current state."""
        self.current_state = self.current_state.enter_shipping_info(info)

    def process_payment(self):
        """Process the payment, updating the current state."""
        self.current_state.process_payment()

# Step 4: Example of Usage
if __name__ == "__main__":
    cart = CheckoutContext()

    cart.add_item("Product 1")
    cart.review_cart()
    cart.enter_shipping_info("123 Main St, City")
    cart.process_payment()
