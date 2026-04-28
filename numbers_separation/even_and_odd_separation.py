class NumberDistinguisher:
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_numbers_collection = []
        self.odd_numbers_collection = []
        self.invalid_entries = [] # For the non-integer values

    def scan_and_distinguish(self):
        with open(self.numbers, 'r') as number_file:
            for line_entry in number_file:
                cleaned_entry = line_entry.strip()
                try:
                    numeric_entry = int(cleaned_entry)
                    if numeric_entry % 2 == 0:
                        self.even_numbers_collection.append(numeric_entry)
                    else:
                        self.odd_numbers_collection.append(numeric_entry)
                except ValueError:
                    self.invalid_entries.append(cleaned_entry)