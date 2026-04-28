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