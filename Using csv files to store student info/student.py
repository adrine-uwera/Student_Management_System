import datetime  # Datetime module will help in creating date objects and manipulating them
import csv   # CSV module will allow us to work with a csv file for storing students data and to manipulate that data
import sys  # Sys module will allow us to use exit function for ending the program when needed


# creating class student
class Student:
    # Init method will be passed parameters containing information about a student, and the instance variables will be
    # initialized to the values of their corresponding parameter
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year):
        self.student_email = student_email
        self.student_name = student_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.major = ""   # initialized as empty string because students have different majors

        try:
            # strip function will remove any blank spaces left by user on the around the date of enrollment with
            # the split function will divide the string into list elements a hyphen being the separator of list items.
            # List items will be turned into integers using the int and map functions, then the list will convert the
            # value returned by map function into a list for readability
            date_of_enrollment = list(map(int, date_of_enrollment.strip().split("-")))
            # Accessing the year, month, and date by their index in date_of_enrollment list and passing them to the date
            # function of datetime module to be turned into a date object,then initialize the date to instance variable
            self.date_of_enrollment = datetime.date(date_of_enrollment[0], date_of_enrollment[1],
                                                    date_of_enrollment[2])

        #     This message will be printed if the user does not separate the date with hyphens
        except IndexError as e:
            print("Separate year, month, date with a hyphen(-). Use YYYY-MM-DD format.", e)  # e represents
            # exception-type object and it will give more clarity on the indexError which occurred
            sys.exit()  # The program will be ended to prevent errors further in the program i.e: if the program
            # continued with an incorrect date it would also raise an error in calculating the expected graduation date

        # This message will be printed if the user enters date in words ex: January or incorrect format ex:YYYYY-MM-DD
        except ValueError as e:
            print("Use digits only! And check if date is correct with YYYY-MM-DD format.", e)
            sys.exit()  # The program will be ended to prevent errors further in the program i.e: if the program
            # continued with an incorrect date it would also raise an error in calculating the expected graduation date

        self.year = year
        self.status = "Current"   # The student's status is current by default meaning that they have not graduated yet
        self.internship = []   # List in which student's internships will be appended

    # a method to display student information
    def print_student_information(self):

        return f"Student information: \n" \
               f"Student email: {self.student_email}\n" \
               f"Student name: {self.student_name}\n" \
               f"Gender: {self.gender}\n" \
               f"Date of birth: {self.date_of_birth}\n" \
               f"Address: {self.address}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"Major: {self.major}\n" \
               f"Date of enrollment: {self.date_of_enrollment}\n" \
               f"Year:{self.year}\n" \
               f"Status: {self.status}\n" \
               f"Internships:{self.internship}"

    # a method to promote student to the next year
    def promote_student(self):
        self.year += 1   # increments student year of study by 1
        return f"Student is now in year {self.year}"  # printed to indicate that student was promoted to the next year

    # a method to update student information: phone number or address
    def update_student_information(self):
        print("Choose: \n1.Update phone number\n2.Update address\n")
        choice = input("Enter your choice 1 or 2: ")  # takes user's choice between whether to update phone number or
        # address
        if choice == '1':  # specifies what will happen when user chooses 1 for updating phone number
            try:
                # Opens the file in which all students records are kept in read mode as file object student_records
                with open("student_records.csv", 'r') as student_records:
                    read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                    # read_student as a list
                    updated_student_records = []  # will contain all lines of the file after being updated
                    for student in read_student:  # Looping through all lines(students) in the file
                        # since each line is a list itself, and the student email is the first item the condition is
                        # checking for each line if the element at index [0] is equal to the email of the calling
                        # instance as we want to know on which line is the information about the calling instance kept
                        if self.student_email == student[0]:
                            new_phone_number = input("Enter student's new phone number: ")
                            self.phone_number = new_phone_number  # updating phone number instance variable
                            student[5] = self.phone_number  # Since the student phone number is kept at the 5th index of
                            # each line the new phone number replace the old one kept there on this particular line
                        updated_student_records.append(student)  # Each line under iteration is appended on the list
                        # whether updated or not
            except OSError as e:
                print("File not found", e)  # This will be printed if a file can not be accessed, e represents
                # exception-type object and it will give more clarity on the OSError which occurred
                sys.exit()  # Ends the program with exit function

            # Opens the same file with student records in write mode, and add a newline parameter to specify that no
            # blank line should be left between two lines when writing on the file
            with open("student_records.csv", 'w', newline="") as student_records:
                # Field names for each field of the line, they can also be considered as column names
                fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                              'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                              'expected_graduation_date', "internship"]
                write_student = csv.DictWriter(student_records, fieldnames=fieldnames)  # Creating a writing object
                # and using DictWriter method to record student information as values of the fieldnames keys
                for student in updated_student_records:  # Looping through lines (student records) stored in the list
                    # Writing each line on the list again as a separate row (line) and using indexes to access
                    # where information is stored on the list(line stored as a list) as it is uniform in all lines.
                    write_student.writerow(
                        {"student_email": student[0], "student_name": student[1], "gender": student[2],
                         "date_of_birth": student[3],
                         "address": student[4], "phone_number": student[5], "major": student[6],
                         "date_of_enrollment": student[7],
                         "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                         "expected_graduation_date": student[11], "internship": student[12]})

            return f"Phone number updated successfully to {self.phone_number}"  # returns message with new phone number

        elif choice == '2':  # specifies what will happen when user chooses 1 for updating phone number
            try:
                # Opens the file in which all students records are kept in read mode as file object student_records
                with open("student_records.csv", 'r') as student_records:
                    read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                    # read_student as a list
                    updated_student_records = []  # will contain all lines of the file after being updated
                    for student in read_student:  # Looping through all lines(students) in the file
                        # since each line is a list itself, and the student email is the first item the condition is
                        # checking for each line if the element at index [0] is equal to the email of the calling
                        # instance as we want to know on which line is the information about the calling instance kept
                        if self.student_email == student[0]:
                            new_address = input("Enter student's new address: ")
                            self.address = new_address  # updating address instance variable
                            student[4] = self.address  # Since the student address is kept at the 4th index of
                            # each line the address replace the old one kept there on this particular line
                        updated_student_records.append(student)  # Each line under iteration is appended on the list
                        # whether updated or not
            except OSError as e:
                print("File not found", e)  # This will be printed if a file can not be accessed, e represents
                # exception-type object and it will give more clarity on the OSError which occurred
                sys.exit()  # Ends the program with exit function

            # Opens the same file with student records in write mode, and add a newline parameter to specify that no
            # blank line should be left between two lines when writing on the file
            with open("student_records.csv", 'w', newline="") as student_records:
                # Field names for each field of the line, they can also be considered as column names
                fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                              'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                              'expected_graduation_date', "internship"]
                write_student = csv.DictWriter(student_records, fieldnames=fieldnames)  # Creating a writing object
                # and using DictWriter method to record student information as values of the fieldnames keys
                for student in updated_student_records:  # Looping through lines (student records) stored in the list
                    # Writing each line on the list again and using indexes to access where information is stored
                    # on the list(line stored as a list) as it is uniform in all lines.
                    write_student.writerow(
                        {"student_email": student[0], "student_name": student[1], "gender": student[2],
                         "date_of_birth": student[3],
                         "address": student[4], "phone_number": student[5], "major": student[6],
                         "date_of_enrollment": student[7],
                         "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                         "expected_graduation_date": student[11], "internship": student[12]})

            return f"Address updated successfully to {self.address}"  # returns message with new address
        else:
            return "Invalid input!"  # This will be returned in case the user inputs a value nor "1" or "2"

    # Method to add information about student's internships
    def add_student_internship(self):
        # Opens the file in which all students records are kept in read mode as file object student_records
        try:
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                # read_student as a list
                updated_student_records = []  # will contain all lines of the file after being updated
                for student in read_student:  # Looping through all lines(students) in the file
                    # since each line is a list itself, and the student email is the first item the condition is checking
                    # for each line if the element at index [0] is equal to the email of the calling instance as we want
                    # to know on which line is the information about the calling instance kept
                    if self.student_email == student[0]:
                        # The user enters internship details and they are kept in a dictionary
                        internship_details = {
                            "Company name": input("Enter the name of the company the student interned at: "),
                            "Start date": input("Enter the start date of the internship: "),
                            "End date": input("Enter the end date of the internship: "),
                            "Position": input("Enter the position the student had in the internship: ")}
                        if student[12] != '[]':  # checks if the students  has had internships before. This '[]' would be
                            # the value stored on index[12] if the student had zero internships as the default value for
                            # self.internship is an empty list
                            self.internship.append(student[12])  # Append past internship on file to the instance variable.
                            # The instance variable is initially empty as a student object is created once again, regardless
                            # that they are recorded on the file and the variable is initialized to empty list in the init method.
                            self.internship.append(internship_details)  # Append new internship to the instance variable.
                            student[12] = ''  # The index which holds student internship information is emptied because it
                            # will be replaced by the information in self.internship, and there would be a repetition as
                            # what the index holds was also appended to the instance variable
                            for internship in self.internship:  # Loops through all internship held in the instance variable
                                student[12] += str(internship)  # Appends the internship under iteration to the internships
                                # recorded in the previous iterations

                        else:  # This would be implemented if the student has never had internships before
                            student[12] = ""  # "[]" is removed from the index on which internships are recorded
                            self.internship.append(internship_details)  # Append new internship to the instance variable.
                            for internship in self.internship:  # Loops through all internship held in the instance variable
                                student[12] += str(internship)  # Appends the internship under iteration to the internships
                                # recorded in the previous iterations
                    updated_student_records.append(student)  # Each line under iteration is appended on the list
                    # whether updated or not
        except OSError as e:
            print("File not found", e)  # This will be printed if a file can not be accessed, e represents
            # exception-type object and it will give more clarity on the OSError which occurred
            sys.exit()  # Ends the program with exit function

        # Opens the same file with student records in write mode, and add a newline parameter to specify that no
        # blank line should be left between two lines when writing on the file
        with open("student_records.csv", 'w', newline="") as student_records:
            # Field names for each field of the line, they can also be considered as column names
            fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                          'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                          'expected_graduation_date', "internship"]
            write_student = csv.DictWriter(student_records, fieldnames=fieldnames)  # Creating a writing object
            # and using DictWriter method to record student information as values of the fieldnames keys
            for student in updated_student_records:  # Looping through lines (student records) stored in the list
                # Writing each line on the list again and using indexes to access where information is stored on
                # the list(line stored as a list) as it is uniform in all lines.
                write_student.writerow(
                    {"student_email": student[0], "student_name": student[1], "gender": student[2],
                     "date_of_birth": student[3],
                     "address": student[4], "phone_number": student[5], "major": student[6],
                     "date_of_enrollment": student[7],
                     "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                     "expected_graduation_date": student[11], "internship": student[12]})

        return "internship added successfully!"  # Method return value
