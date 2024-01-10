class Iterator:
    """Step 1: Create the Iterator interface."""
    
    def __iter__(self):
        """Defines the __iter__() method to return self as an iterator."""
        raise NotImplementedError

    def __next__(self):
        """Defines the __next__() method to retrieve elements sequentially."""
        raise NotImplementedError
    

class MyIterator(Iterator):
    """Step 2: Implement a Concrete Iterator."""
    
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # Returning self as an iterator

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
    
class Collection:
    """Step 3: Create the Collection interface."""
    
    def create_iterator(self):
        """Method to create an Iterator compatible with the collection."""
        raise NotImplementedError


class MyCollection(Collection):
    """Step 4: Implement a Concrete Collection."""
    
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def create_iterator(self):
        return MyIterator(self.data)


def main():
    """Demonstrate the usage of the implemented Iterator Pattern."""
    
    # Creating a collection
    my_collection = MyCollection()
    my_collection.add(1)
    my_collection.add(2)
    my_collection.add(3)

    # Creating an iterator for the collection
    my_iterator = my_collection.create_iterator()

    # Using the iterator to traverse through the elements
    for element in my_iterator:
        print(element)


if __name__ == "__main__":
    main()