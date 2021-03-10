"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    count = self.start
    def __init__(self, start):
        self.start = start

    def generate():
        self.count = self.count + 1
        return self.count

    def reset():
        self.count = self.start