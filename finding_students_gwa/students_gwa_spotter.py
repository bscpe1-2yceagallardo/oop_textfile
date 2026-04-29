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

    def get_honor_status(self, gwa):
        if 1.0 <= gwa <= 1.25:
            return "President's Lister 🏆"
        elif 1.26 <= gwa <= 1.50:
            return "Dean's Lister ⭐"
        elif 1.51 <= gwa <= 1.75:
            return "Honor Roll 🎖️"
        else:
            return "Passing"

    def finding_highest_gwa(self):
        best_student = min(self.students_records, key=lambda student: student[1])
        status = self.get_honor_status(best_student[1])
        return best_student[0], best_student[1], status

    def top_three(self):
        sorted_list= sorted(self.students_records, key=lambda student: student[1])
        return [(name, gwa, self.get_honor_status(gwa) for name, gwa in sorted_list[:3])]

    def get_class_analytics(self):
        if not self.students_records:
            return 0, 0
        total_gwa = sum(student[1] for student in self.students_records)
        average = total_gwa / len(self.students_records)
        highest = min(student[1] for student in self.students_records)
        lowest = max(student[1] for student in self.students_records)
        return round (average, 2), highest, lowest

