class NumberDistinguisher:
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_numbers_collection = []
        self.odd_numbers_collection = []
        self.invalid_entries = [] # For the non-integer values