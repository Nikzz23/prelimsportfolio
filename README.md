## Nikolas Jon T. Peña  | M001 - CP102

## Student Assistants Information Management System
* A preliminary project output for CP102. It's a record management system that reads and manipulates a CSV file. It can display the student's personal information and their daily time record. It can also add a new student assistant personal information and it will automatically create their own separate CVS DTR file. Furthermore, they can modify or delete their personal pieces of information or DTR. Because the code is long, I decided to use OOP to make my code more readable and clean.

## Source Code
* https://github.com/Nikzz23/prelimsportfolio/blob/96c0886993b94656f92fc668d6123092f98db374/RecordManagementSystem/main.py

## Explanation of code
* to run the program, we need to run the program in the 'main' file. There we can call the other functions from their respective files.

### main.py

```diff
+> we need to import the class form the other file so that we can use their functions
from records import PersonalRecords
from DTRmodule import StudentDTR

+> i used a class to store the display and the code for the command of the user input. 
class MainDisplay:

+> the function display is only for printing the menu
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

+> The function main accepts the user's input command and then executes that command and the function inside it.
+> It will loop forever unless the user inputs '13' to exit the program.
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
```

* so that this program runs smoothly, we need the 3 files that contain our codes. The first one is the file "main.py" with the code above, the second is the file "records.py", where we keep the functions that manipulate the student assistant's records, and lastly is the file "DTRmodule.py", where it stores the functions that manipulate the DTR of the student assistants.

### records.py
```diff
+> we need to import csv so that we can open and write the csv files
import csv
# import os

+> i use a class to store the functions that manipulates the records.
class PersonalRecords:

+> returns the content of the csv file into a dictionary
    def records():
        personal = {}
        with open('StudentRecords.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                personal[row[0]] = {'Name': row[1], 'Age': row[2], 'Sex': row[3], 'Course': row[4], 'Year': row[5]}
        return personal

+> It displays all the student assistants' records from the file "StudentRecords.csv"
+> We used an open to open the file and a csv.reader so that it could read the contents of the file and then print it.    
    def display():
        with open('StudentRecords.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            print("""
┌─────────────────────────────────────────────────────┐
╰─────────────────────────────────────────────────────╯
             Students Personal Information
  ───────────────────────────────────────────────────
""")
            for row in csv_reader:
                print('◉ Student Number:',row[0])
                print('\tName:',row[1])
                print('\tAge:',row[2])
                print('\tSex:',row[3])
                print('\tCourse/Program:',row[4])
                print('\tYear:',row[5])
                
+> The function add, adds your inputted information in the temp (where it stores the records from the csv file).
+> After all the required information is inputted it then writes the new dictionary to the file "StudentRecords.csv".
+> After a new student is added, a file will be created for that student's DTR. 
    def add():
        temp = PersonalRecords.records()
        
        print("Register Information")
        id_number = input("ID number: ")
        if id_number not in temp:
            name = input("Name: ")
            age = input("Age: ")
            sex = input("Sex: ")
            course = input("Course/Program: ")
            year = input("Year: ")
    
            # temp = PersonalRecords.records()
            temp[id_number] = {"Name": name, "Age": age, "Sex": sex, "Course": course, "Year": year}
    
            with open('StudentRecords.csv', mode='w', newline='') as csv_file:
                fieldnames = ['ID Number', 'Name', 'Age', 'Sex', 'Course/Program', 'Year']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
                writer.writeheader()
                for num in temp:
                    writer.writerow({'ID Number': num, 'Name': temp[num]['Name'], 'Age': temp[num]['Age'],
                                     'Sex': temp[num]['Sex'], 'Course/Program': temp[num]['Course'],
                                     'Year': temp[num]['Year']})
            
    
+> to create a dtr file for the new student
            with open(f'[{id_number}] {name} DTR.csv', mode='w', newline='') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow(
                    ['Date', 'In (AM)', 'Out (AM)', 'In (PM)', 'Out (PM)', 'Overtime (In)', 'Overtime (Out)'])
                
            print('Student added successfully and have created a DTR file')

        else:
            print('Student ID number is already taken')
    
+> The function delete, as its names suggest, it deletes the student's data in the file records.
+> we used a temp variable to store the contents of the records into a dictionary.
+> then we used a pop method to remove the students records from the dictionary.
+> after removing, it then writes the new dictionary into the records file. 
    def delete():
        print("Deleting Data")
        id_number = input("Enter Student ID: ")

        temp = PersonalRecords.records()

        if id_number in temp:
            confirmation = input('Confirm Deletion [y/n]: ')
            if confirmation.lower() == 'y':
                temp.pop(id_number)
                print("Student Deleted")
            elif confirmation.lower() == 'n':
                print('Delete Cancelled')
            else:
                print('Invalid')
        else:
            print("Student not in records")

        with open('StudentRecords.csv', mode='w', newline='') as csv_file:
            fieldnames = ['ID Number', 'Name', 'Age', 'Sex', 'Course/Program', 'Year']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for num in temp:
                writer.writerow({'ID Number': num, 'Name': temp[num]['Name'], 'Age': temp[num]['Age'],
                                 'Sex': temp[num]['Sex'], 'Course/Program': temp[num]['Course'],
                                 'Year': temp[num]['Year']})
+> The update function, modifies the student information.
+> again we used the temp variable to store the contents of the records file into a dictionary.
+> Because we turn it into a dictionary we can access the key and value pair to update the student's information.
+> after the user chooses and inputs new information, it will then update the contents of the dictionary.
+> The updated dictionary will then be written into the file records.
    def update():
        print("Modifying Data")
        id_number = input("Enter Student ID: ")

        temp = PersonalRecords.records()

        if id_number in temp:
            print("""
┌──────────────────────────────────────────────┐
╰──────────────────────────────────────────────╯
          Modify Students Information
  ────────────────────────────────────────────
        [1] Name
        [2] Age
        [3] Sex
        [4] Course/Program
        [5] Year
  ────────────────────────────────────────────
          Enter Command [1-5]
             """)
            choice = input(">>> ")
            if choice == '1':
                newName = input("Enter new name: ")
                temp[id_number]['Name'] = newName
            elif choice == '2':
                newAge = input("Enter new age: ")
                temp[id_number]['Age'] = newAge
            elif choice == '3':
                newSex = input("Enter new sex: ")
                temp[id_number]['Sex'] = newSex
            elif choice == '4':
                newCourse = input("Enter new course/program: ")
                temp[id_number]['Course'] = newCourse
            elif choice == '5':
                newYear = input("Enter new year: ")
                temp[id_number]['Year'] = newYear
            else:
                print("Invalid")
        else:
            print("Student not in records")

        with open('StudentRecords.csv', mode='w', newline='') as csv_file:
            fieldnames = ['ID Number', 'Name', 'Age', 'Sex', 'Course/Program', 'Year']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for num in temp:
                writer.writerow({'ID Number': num, 'Name': temp[num]['Name'], 'Age': temp[num]['Age'],
                                 'Sex': temp[num]['Sex'], 'Course/Program': temp[num]['Course'],
                                 'Year': temp[num]['Year']})
+> The function search, displays if a student is in the records or not.
+> We used a temp variable to store the dictionary content of the records.
+> We can then access what is inside the dictionary and see if that student is in the records.
    def search():
        print("Search Student")
        id_number = input("Enter Student ID: ")

        temp = PersonalRecords.records()

        if id_number in temp:
            print('Name: ', temp[id_number]['Name'])
            print('Age: ', temp[id_number]['Age'])
            print('Sex: ', temp[id_number]['Sex'])
            print('Course/Program: ', temp[id_number]['Course'])
            print('Year: ', temp[id_number]['Year'])
        else:
            print("Student not found")
```

### DTRmodule.py
```diff
+> I imported the PersonalRecords so that i can use some of the fucntions
+> Second I imported the module csv for reading and writing the csv file
+> I also imported the os module so that i can check if the file exists or not, and to delete a file
from records import PersonalRecords
import csv
import os

+> I used a class so that i can call this class and its functions in the main file
class StudentDTR:

+> This function returns the contents of the student DTR CSV file into a dictionary.
+> so that we can easily manipulate the content inside. 
    def DTRrecords(id, name):
        dtr = {}
        filename = f'[{id}] {name} DTR.csv'

        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                dtr[row[0]] = {'inam': row[1], 'outam': row[2], 'inpm': row[3], 'outpm': row[4], 'in': row[5],
                               'out': row[6]}
        return dtr

+> This function converts the new dictionary into the CSV file.
    def CSVconverter(id, name, date, dtr):
        tempdtr = dtr

        filename = f'[{id}] {name} DTR.csv'

        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['Date', 'In (AM)', 'Out (AM)', 'In (PM)', 'Out (PM)', 'Overtime (In)', 'Overtime (Out)']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for date in dtr:
                writer.writerow({'Date': date, 'In (AM)': tempdtr[date]['inam'], 'Out (AM)': tempdtr[date]['outam'],
                                 'In (PM)': tempdtr[date]['inpm'], 'Out (PM)': tempdtr[date]['outpm'],
                                 'Overtime (In)': tempdtr[date]['in'], 'Overtime (Out)': tempdtr[date]['out']})

+> this function adds the arrival time (AM or PM) in the dtr 
    def addIn(id, name, date, time, ampm):

        dtr = StudentDTR.DTRrecords(id, name)

        if date not in dtr:
            if ampm == '1':
                dtr[date] = {'inam': time, 'outam': '', 'inpm': '', 'outpm': '', 'in': '', 'out': ''}
            elif ampm == '2':
                dtr[date] = {'inam': '', 'outam': '', 'inpm': time, 'outpm': '', 'in': '', 'out': ''}
        else:
            if ampm == '1':
                for x in dtr[date]:
                    dtr[date] = {'inam': time, 'outam': dtr[date]['outam'],
                                 'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                                 'in': dtr[date]['in'], 'out': dtr[date]['out']}
            elif ampm == '2':
                for x in dtr[date]:
                    dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                                 'inpm': time, 'outpm': dtr[date]['outpm'],
                                 'in': dtr[date]['in'], 'out': dtr[date]['out']}

        StudentDTR.CSVconverter(id, name, date, dtr)

+> the function addout, adds the departure time in the dtr
    def addOut(id, name, date, time, ampm):

        dtr = StudentDTR.DTRrecords(id, name)

        if ampm == '1':
            for x in dtr[date]:
                dtr[date] = {'inam': dtr[date]['inam'], 'outam': time,
                             'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                             'in': dtr[date]['in'], 'out': dtr[date]['out']}
        elif ampm == '2':
            for x in dtr[date]:
                dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                             'inpm': dtr[date]['inpm'], 'outpm': time,
                             'in': dtr[date]['in'], 'out': dtr[date]['out']}

        StudentDTR.CSVconverter(id, name, date, dtr)

+> overtimeAdd, adds the overtime in the dtr
    def overtimeAdd(id, name, date, time, inout):
        dtr = StudentDTR.DTRrecords(id, name)

        if date not in dtr:
            if inout == '1':
                dtr[date] = {'inam': '', 'outam': '', 'inpm': '', 'outpm': '', 'in': time, 'out': ''}
            elif inout == '2':
                dtr[date] = {'inam': '', 'outam': '', 'inpm': '', 'outpm': '', 'in': '', 'out': time}
        else:
            if inout == '1':
                for x in dtr[date]:
                    dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                                 'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                                 'in': time, 'out': dtr[date]['out']}
            elif inout == '2':
                for x in dtr[date]:
                    dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                                 'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                                 'in': dtr[date]['in'], 'out': time}

        StudentDTR.CSVconverter(id, name, date, dtr)

+> This function allows the user to modify the time in the student's DTR.
    def modifyAdd(id, name, date, choice, time):
        dtr = StudentDTR.DTRrecords(id, name)

        if choice == '1':
            for x in dtr[date]:
                dtr[date] = {'inam': time, 'outam': dtr[date]['outam'],
                             'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                             'in': dtr[date]['in'], 'out': dtr[date]['out']}
        elif choice == '2':
            for x in dtr[date]:
                dtr[date] = {'inam': dtr[date]['inam'], 'outam': time,
                             'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                             'in': dtr[date]['in'], 'out': dtr[date]['out']}
        elif choice == '3':
            for x in dtr[date]:
                dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                             'inpm': time, 'outpm': dtr[date]['outpm'],
                             'in': dtr[date]['in'], 'out': dtr[date]['out']}
        elif choice == '4':
            for x in dtr[date]:
                dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                             'inpm': dtr[date]['inpm'], 'outpm': time,
                             'in': dtr[date]['in'], 'out': dtr[date]['out']}
        elif choice == '5':
            for x in dtr[date]:
                dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                             'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                             'in': time, 'out': dtr[date]['out']}
        elif choice == '6':
            for x in dtr[date]:
                dtr[date] = {'inam': dtr[date]['inam'], 'outam': dtr[date]['outam'],
                             'inpm': dtr[date]['inpm'], 'outpm': dtr[date]['outpm'],
                             'in': dtr[date]['in'], 'out': time}

        StudentDTR.CSVconverter(id, name, date, dtr)
        
+> As the function name suggest, it displays the student's DTR
    def display():
        temp = PersonalRecords.records()
        id = input('Enter ID: ')
        
        if id in temp:
            name = temp[id]['Name']
            filename = f'[{id}] {name} DTR.csv'
            result = os.path.exists(filename)
            if result == True:
                with open(filename, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    print(f"""
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
    {name} DTR | ID:{id}                     filename:{filename}
  ─────────────────────────────────────────────────────────────────────────────────────────────────        """)
                    for row in csv_reader:
                        print(f"\t{row[0]:10}|{row[1]:10}|{row[2]:10}|{row[3]:10}|{row[4]:10}|{row[5]:15}|{row[6]:15}")
                    print()
            else:
                print('File not found')
        else:
            print('ID not in records')

+> this is a function that calls out the addIn function if all the conditions are met. 
    def In():

        temp = PersonalRecords.records()

        id = input("Enter Student ID: ")

        if id in temp:
            name = temp[id]['Name']
            date = input('Enter Date (ex. 1-29-24): ')
            time = input('Enter Time (ex. 9:00): ')
            ampm = input('AM [1] or PM [2]')

            StudentDTR.addIn(id, name, date, time, ampm)
            print('Arrival added')

        else:
            print("ID not in records")

+> this is a function that calls out the addOut function if all the conditions are met. 
    def Out():
        temp = PersonalRecords.records()

        id = input("Enter Student ID: ")

        if id in temp:
            name = temp[id]['Name']
            dtr = StudentDTR.DTRrecords(id, name)
            date = input('Enter Date (ex. 1-29-24): ')
            if date in dtr:
                time = input('Enter Time (ex. 9:00): ')
                ampm = input('AM [1] or PM [2]')
                StudentDTR.addOut(id, name, date, time, ampm)
                print('Departure added')
            else:
                print('You cant out, without having to in first')
        else:
            print("ID not in records")

+> this is also a function that calls out the overtimeAdd function if all the conditions are met. 
    def overtime():
        temp = PersonalRecords.records()

        id = input("Enter Student ID: ")

        if id in temp:
            name = temp[id]['Name']
            inout = input('In [1] or Out [2]: ')
            date = input('Enter Date (ex. 1-29-24): ')
            time = input('Enter Time (ex. 9:00 AM): ')

            StudentDTR.overtimeAdd(id, name, date, time, inout)
            print('Overtime Added')
        else:
            print("ID not in records")

+> This is the function where the user can choose what time they can modify in the dtr
    def modify():

        temp = PersonalRecords.records()

        id = input("Enter Student ID: ")

        if id in temp:
            name = temp[id]['Name']
            dtr = StudentDTR.DTRrecords(id, name)
            date = input('Enter Date (ex. 1-29-24): ')
            if date in dtr:
                print('''
┌──────────────────────────────────────────────┐
╰──────────────────────────────────────────────╯
             Modify Students DTR
  ────────────────────────────────────────────
        [1] In (AM)
        [2] Out (AM)
        [3] In (PM)
        [4] Out (PM)
        [5] Overtime (In)
        [6] Overtime (Out)
  ────────────────────────────────────────────
        Enter Command [1-6]
            ''')
                choice = input('>>> ')
                time = input('Enter time (to delete time, just press "Enter"): ')
                StudentDTR.modifyAdd(id, name, date, choice, time)
                print('Successfully Modified')
            else:
                print('Date not in DTR')
        else:
            print("ID not in records")

+> a function where we can delete the studet's DTR and use the function:
+> os.path.exists, if the file exist and os.remove, to delete the student's DTR file.
    def deletefile():
        # temp = PersonalRecords.records()

        id = input("Enter Student ID: ")
        # name = temp[id]['Name']
        name = input('Enter name: ')
        filename = f'[{id}] {name} DTR.csv'
        result = os.path.exists(filename)
        if result == True:
            print('File Found')
            confirm = input(f'Do you still want to delete the file {filename}? [y/n] ')
            if confirm == 'y':
                print('File Deleted')
                os.remove(filename)      
            elif confirm == 'n':
                print('Delete Cancelled')
        else:
            print('File not found')

+> the deletedate, removes the date in the DTR.
    def deletedate():
        temp = PersonalRecords.records()

        id = input("Enter Student ID: ")

        if id in temp:
            name = temp[id]['Name']
            #filename = f'[{id}] {name} DTR.csv'
            dtr = StudentDTR.DTRrecords(id, name)
            date = input('Enter Date to delete (ex.1-9-24):')
            if date in dtr:
                print('Date found!')
                confirm = input(f'Confirm to delete the date: {date}? [y/n] ')
                if confirm.lower() == 'y':
                    dtr.pop(date)
                    print("Date Deleted")
                elif confirm.lower() == 'n':
                    print('Delete Cancelled')
            else:
                print('Date not in DTR')

        else:
            print('ID not in records')

        StudentDTR.CSVconverter(id, name, date, dtr)
```






