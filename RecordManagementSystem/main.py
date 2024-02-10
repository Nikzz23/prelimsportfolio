from records import PersonalRecords
from DTRmodule import StudentDTR


class MainDisplay:

    def display():
        print("""
┌─────────────────────────────────────────────────────┐
╰─────────────────────────────────────────────────────╯
        Student Assistant Information System
  ───────────────────────────────────────────────────

        Students Assistants Personal Records

            [1] Add Student
            [2] Update Information
            [3] Search Student
            [4] Display All Records
            [5] Delete Student

  ───────────────────────────────────────────────────

        Student Assistants Daily Time Records

            [6] Display Student DTR
            [7] Time In
            [8] Time Out
            [9] Overtime
            [10] Modify Student DTR
            [11] Delete Date
            [12] Delete DTR File

            [13] Exit

  ───────────────────────────────────────────────────
        Select Command [1-11] """)

    def main():
        while True:
            MainDisplay.display()
            command = input(">>> ")

            if command == '1':
                PersonalRecords.add()
            elif command == '2':
                PersonalRecords.update()
            elif command == '3':
                PersonalRecords.search()
            elif command == '4':
                PersonalRecords.display()
            elif command == '5':
                PersonalRecords.delete()
            elif command == '6':
                StudentDTR.display()
            elif command == '7':
                StudentDTR.In()
            elif command == '8':
                StudentDTR.Out()
            elif command == '9':
                StudentDTR.overtime()
            elif command == '10':
                StudentDTR.modify()
            elif command == '11':
                StudentDTR.deletedate()
            elif command == '12':
                StudentDTR.deletefile()
            elif command == '13':
                break


if __name__ == "__main__":
    MainDisplay.main()
