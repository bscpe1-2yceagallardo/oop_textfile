class StudentGwaSpotter:
    def __init__(self, students_gwa):
        self.students_gwa = students_gwa
        self.students_records = []

    def load_students(self):
        try:
            with open(self.students_gwa, 'r') as file_link:
                for line in file_link:
                    if "," in line:
                        full_name, gwa_value = line.strip().split(",")
                        self.students_records.append((full_name.strip(), float(gwa_value)))
        except FileNotFoundError:
            print("Error:  The data file was not found.")

    def get_honor_student(self, gwa):
        if 1.0 <= gwa <= 1.25:
            return "President's Lister 🏆"
        elif 1.26 <= gwa <= 1.50:
            return "Dean's Lister ⭐"
        elif 1.51 <= gwa <= 1.75:
            return "Honor Roll 🎖️"
        else:
            return "Passing"