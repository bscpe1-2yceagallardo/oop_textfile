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
                        targer_file = even_file
                        category = "EVEN_SQUARE"
                    else:
                        # For odd logic cube
                        transformed_result = integer_value ** 3
                        targer_file = odd_file
                        category = "ODD_CUBE"