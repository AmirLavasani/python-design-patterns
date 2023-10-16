from abc import ABC, abstractmethod
from datetime import datetime
import time
import random


# Define an interface for the Real Subject
class Subject(ABC):
    @abstractmethod
    def perform_operation(self):
        pass


# Define the Real Subject that we want to monitor
class RealSubject(Subject):
    def perform_operation(self):
        """
        The Real Subject's method representing a costly operation.
        """
        print("RealSubject: Performing a costly operation...")
        time.sleep(random.random()*5)  # Sleep for a random (0-5) seconds


# Define the Monitoring Proxy that will lazily instantiate the Real Subject
class MonitoringProxy(Subject):
    def __init__(self):
        self._real_subject = None

    def perform_operation(self):
        """
        The Proxy's method, which monitors and adds performance metrics.
        Lazily instantiates the Real Subject on the first call.
        """
        if self._real_subject is None:
            print("MonitoringProxy: Lazy loading the RealSubject...")
            self._real_subject = RealSubject()

        start_time = datetime.now()
        print(f"MonitoringProxy: Recording operation start time - {start_time}")

        # Delegate the operation to the Real Subject
        self._real_subject.perform_operation()

        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"MonitoringProxy: Recording operation end time - {end_time}")
        print(f"MonitoringProxy: Operation executed in {execution_time} seconds")


# Client code
if __name__ == "__main__":
    # Create the Monitoring Proxy (lazy loading of Real Subject)
    monitoring_proxy = MonitoringProxy()

    # Client interacts with the Proxy
    monitoring_proxy.perform_operation()
