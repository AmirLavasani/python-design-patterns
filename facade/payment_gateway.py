from abc import ABC, abstractmethod


# Step 1: Create an interface for payment gateways


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Step 1: Create Subsystem Classes for Payment Gateways


class PayPalGateway:
    def process_payment(self, amount):
        return f"Payment of ${amount} processed via PayPal"


class StripeGateway:
    def process_payment(self, amount):
        return f"Payment of ${amount} processed via Stripe"


class CryptoGateway:
    def process_payment(self, amount):
        return f"Payment of ${amount} processed via Crypto (Bitcoin)"


# Step 2: Implement Facade Class


class PaymentFacade:
    def __init__(self):
        self._gateways = {
            "paypal": PayPalGateway(),
            "stripe": StripeGateway(),
            "crypto": CryptoGateway(),
        }

    def process_payment(self, amount, gateway):
        """Processes payment through the selected gateway."""
        if gateway in self._gateways:
            return self._gateways[gateway].process_payment(amount)
        else:
            return "Invalid gateway selection"


# Step 3: Utilize Facade in Client Code


def main():
    # Creating PaymentFacade instance
    payment_facade = PaymentFacade()

    # Process payments through different gateways
    print(payment_facade.process_payment(100, "paypal"))
    print(payment_facade.process_payment(150, "stripe"))
    print(payment_facade.process_payment(200, "crypto"))
    print(payment_facade.process_payment(300, "invalid_gateway"))


if __name__ == "__main__":
    main()
