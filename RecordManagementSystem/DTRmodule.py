from records import PersonalRecords
import csv
import os

class StudentDTR:

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

    def deletedate():
        temp = PersonalRecords.records()

        id = input("Enter Student ID: ")

        if id in temp:
            name = temp[id]['Name']
            filename = f'[{id}] {name} DTR.csv'
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