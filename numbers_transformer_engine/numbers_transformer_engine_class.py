class NumberTransformerEngine:
    def __init__(self, source_path="integers.txt"):
        self.source_path = source_path
        self.calculation_cap = 1_000_000 # Safety Cap

    def process_and_audit(self):
        try:
            with open(self.source_path, "r") as integer_file,\
                 open("double.txt", "w") as even_file, \
                 open("triple.txt", "w") as odd_file, \
                 open("audit_log.txt", "w") as audit_file:

                 audit_file.write("---Math Audit Log ---\n")

                 for line_number, raw_data in enumerate(integer_file, start=1):
                    clean_data = raw_data.strip()

                    # Safety Sieve
                    if not clean_data or not clean_data.lstrip('-').isdigit():
                        audit_file.write(f"Line {line_number}: REJECTED (Non-integer: '{clean_data}')\n")
                        continue

                    integer_value = int(clean_data)

                    if integer_value % 2 == 0:
                        # For even logic square
                        transformed_result = integer_value ** 2
                        target_file = even_file
                        category = "EVEN_SQUARE"
                    else:
                        # For odd logic cube
                        transformed_result = integer_value ** 3
                        target_file = odd_file
                        category = "ODD_CUBE"

                    # Applying Calculation Cap
                    if abs(transformed_result) > self.calculation_cap:
                        audit_file.write(f"Line {line_number}: {category} SKIPPED (Value exceeds safety cap)\n")
                    else:
                        target_file.write(f"{transformed_result}\n")
                        audit_file.write(f"Line {line_number}: {category} SUCCESS ({integer_value} -> {transformed_result})\n")

            print("Processing complete. Please review double.txt, triple.txt, and audit_log.txt")

        except FileNotFoundError:
            print(f"Error: Source file '{self.source_path}' not found. Please create it with 20 integers.")