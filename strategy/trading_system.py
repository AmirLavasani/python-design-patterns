from abc import ABC, abstractmethod

# Step 1: Create the Strategy Interface
class TradingStrategy(ABC):
    @abstractmethod
    def execute_trade(self, data):
        pass

# Step 2: Create Concrete Strategies
class MovingAverageStrategy(TradingStrategy):
    def execute_trade(self, data):
        # Calculate Moving Average (Simple example for illustration)
        window_size = 3  # Adjust as needed
        moving_average = sum(data[-window_size:]) / window_size
        return f"Executing Moving Average Trading Strategy. Moving Average: {moving_average:.2f}"

class MeanReversionStrategy(TradingStrategy):
    def execute_trade(self, data):
        # Calculate Mean Reversion (Simple example for illustration)
        mean_value = sum(data) / len(data)
        deviation = data[-1] - mean_value
        return f"Executing Mean Reversion Trading Strategy. Deviation from Mean: {deviation:.2f}"

# Step 3: Create the Context
class TradingContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_trade(self, data):
        return self._strategy.execute_trade(data)

# Main Section to Showcase Usage
if __name__ == "__main__":
    # Sample data for trading
    trading_data = [50, 55, 45, 60, 50]

    # Create concrete strategy objects
    moving_average_strategy = MovingAverageStrategy()
    mean_reversion_strategy = MeanReversionStrategy()

    # Create context with a default strategy
    trading_context = TradingContext(moving_average_strategy)

    # Execute the default strategy
    result = trading_context.execute_trade(trading_data)
    print(result)  # Output: Executing Moving Average Trading Strategy. Moving Average: 51.67

    # Switch to a different strategy at runtime
    trading_context.set_strategy(mean_reversion_strategy)
    
    # Execute the updated strategy
    result = trading_context.execute_trade(trading_data)
    print(result)  # Output: Executing Mean Reversion Trading Strategy. Deviation from Mean: -1.00
