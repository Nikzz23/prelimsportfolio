## Student Assistants Information Management System 
* a record management system that adds and modifies records to a CSV file. It can display the student's personal information and their daily time record. It can also also add a new student assistant and create their own separate CVS DTR file. Furthermore, they can modify or delete their data.

## Source Code
```
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
```



