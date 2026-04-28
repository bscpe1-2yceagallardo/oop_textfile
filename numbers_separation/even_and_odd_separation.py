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

    def saving_results(self, even_file="even.txt", odd_file="odd.txt", invalid_file="invalid.txt"):
        with open(even_file, 'w') as evens_file:
            for even_value in self.even_numbers_collection:
                evens_file.write(str(even_value) + "\n")

        with open(odd_file, 'w') as odds_file:
            for odd_value in self.odd_numbers_collection:
                odds_file.write(str(odd_value) + "\n")

        with open(invalid_file, 'w') as invalids_file:
            for bad_value in self.invalid_entries:
                invalids_file.write(str(bad_value) + "\n")