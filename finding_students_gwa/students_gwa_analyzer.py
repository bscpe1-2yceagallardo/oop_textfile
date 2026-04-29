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

        if user_choice == "1":
            name, gwa, status = finder.finding_highest_gwa()
            print(f"\nTOP STUDENT:\n{name} - {gwa:.2f} ({status})")

        elif user_choice == "2":
            top_performers = finder.top_three()
            print("\n--- TOP 3 ACADEMIC ACHIEVERS---")
            for rank, (name, gwa, status) in enumerate(top_performers, start=1):
                print(f"{rank}. {name} | GWA: {gwa:.2f} | {status}")

        elif user_choice == "3":
            avg, high, low = finder.get_class_analytics()
            print("\n--- CLASS ANALYTICS ---")
            print(f"Class Average: {avg}")
            print(f"Best Grade: {high}")
            print(f"Lowest Grade: {low}")

        elif user_choice == "4":
            search_query = input("Enter student name: ")
            result = finder.searching_student(search_query)
            if result:
                print(f"\n Match Found: {result['name']}")
                print(f"Rank: #{result['rank']} | GWA: {result['gwa']} | {result['status']}")
            else:
                print("\nNo student found with that name.")

        elif user_choice == "5":
            print("\nShutting down system. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()


