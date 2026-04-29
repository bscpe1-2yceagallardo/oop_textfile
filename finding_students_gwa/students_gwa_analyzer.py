from students_gwa_spotter import StudentGwaSpotter

def main():
    finder= StudentGwaSpotter("students_gwa.txt")
    finder.load_students()

    while True:
        print("\n" + "=" * 30)
        print("ACADEMIC RECORD SYSTEM")
        print("1. Show the Top Student")
        print("2. Show the Top 3 Performers")
        print("3. View Class Analytics")
        print("4. Search specific student by name")
        print("5. Exit")

        user_choice = input("\nSelect an option: ")