from abc import ABC, abstractmethod

# Step 1: Create Subsystem Classes for Payment Gateways

class PayPalGateway:
    def process_payment(self, amount):
        return f"Payment of ${amount} processed via PayPal"

class StripeGateway:
    def pay(self, amount):
        return f"Payment of ${amount} processed via Stripe"

class CryptoGateway:
    def make_payment(self, amount):
        return f"Payment of ${amount} processed via Crypto (Bitcoin)"

# Step 2: Implement Facade Class

class PaymentFacade:
    def __init__(self):
        self._paypal = PayPalGateway()
        self._stripe = StripeGateway()
        self._crypto = CryptoGateway()

    def process_payment(self, amount, gateway):
        """Processes payment through the selected gateway."""
        if gateway == 'paypal':
            return self._paypal.process_payment(amount)
        elif gateway == 'stripe':
            return self._stripe.pay(amount)
        elif gateway == 'crypto':
            return self._crypto.make_payment(amount)
        else:
            return "Invalid gateway selection"

# Step 3: Utilize Facade in Client Code

def main():
    # Creating PaymentFacade instance
    payment_facade = PaymentFacade()

    # Process payments through different gateways
    print(payment_facade.process_payment(100, 'paypal'))
    print(payment_facade.process_payment(150, 'stripe'))
    print(payment_facade.process_payment(200, 'crypto'))
    print(payment_facade.process_payment(300, 'invalid_gateway'))

if __name__ == "__main__":
    main()