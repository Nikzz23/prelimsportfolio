import csv
import os

class PersonalRecords:

    # returns the content of the csv file into a dictionary
    def records():
        personal = {}
        with open('StudentRecords.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                personal[row[0]] = {'Name': row[1], 'Age': row[2], 'Sex': row[3], 'Course': row[4], 'Year': row[5]}
        return personal

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
                

    def add():
        temp = PersonalRecords.records()
        
        print("Register Information")
        id_number = input("ID number: ")
        if id_number in temp:
            name = input("Name: ")
            age = input("Age: ")
            sex = input("Sex: ")
            course = input("Course/Program: ")
            year = input("Year: ")
    
            temp = PersonalRecords.records()
            temp[id_number] = {"Name": name, "Age": age, "Sex": sex, "Course": course, "Year": year}
    
            with open('StudentRecords.csv', mode='w', newline='') as csv_file:
                fieldnames = ['ID Number', 'Name', 'Age', 'Sex', 'Course/Program', 'Year']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
                writer.writeheader()
                for num in temp:
                    writer.writerow({'ID Number': num, 'Name': temp[num]['Name'], 'Age': temp[num]['Age'],
                                     'Sex': temp[num]['Sex'], 'Course/Program': temp[num]['Course'],
                                     'Year': temp[num]['Year']})
            
    
            # to create a dtr file for the new student
            with open(f'[{id_number}] {name} DTR.csv', mode='w', newline='') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow(
                    ['Date', 'In (AM)', 'Out (AM)', 'In (PM)', 'Out (PM)', 'Overtime (In)', 'Overtime (Out)'])
                
            print('Student added successfully and have created a DTR file')
        else:
            print('Student ID number is already taken')
    

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