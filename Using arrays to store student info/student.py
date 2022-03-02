import datetime  # imports datetime library
import sys  # imports sys library

student_records = []  # an array to store student information


# class for Student
class Student:
    # init method to initialize the properties of student
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year):
        # instance variables for student
        self.student_email = student_email
        self.student_name = student_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.major = ""  # initialized as empty string because students have different majors
        # and will be updated as we create child classes.
        self.year = year
        try:
            # converts the date of enrollment (YYYY-MM-DD) to a list containing year, month, day as elements of the list
            date_of_enrollment = list(map(int, date_of_enrollment.strip().split("-")))
            # creates real date from elements the date of enrollment list
            self.date_of_enrollment = datetime.date(date_of_enrollment[0], date_of_enrollment[1],
                                                    date_of_enrollment[2])
        except IndexError as e:  # in case a user enters the date in incorrect format
            print("Separate year, month, date with a hyphen(-). Use YYYY-MM-DD format.", e)
            sys.exit()  # exits the program when the above Index error occurs
        except ValueError as e:  # in case a user enters the date containing strings
            print("Use digits only! And check if date is correct with YYYY-MM-DD format.", e)
            sys.exit()  # exits the program when the above Index error occurs

        # initialize as Current because the student will be a current student until he/she graduates
        self.status = "Current"
        self.internship = []  # a list that will be storing internship information of the student
        student_records.append(self)  # appends all the student's information into the student_records array

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

    # a method to promote student
    def promote_student(self):
        self.year += 1  # increments student year of study by 1
        return f"Student is now in year {self.year}"  # displayed to indicate that the student was promoted

    # a method to update student information: phone number or address
    def update_student_information(self):
        print("Choose: \n1. Update phone number\n2. Update address\n")  # displays a menu to choose from
        choice = input("Enter your choice: ")  # takes user's choice between whether to update phone number or address
        if choice == '1':  # when user chooses 1 for updating phone number
            new_phone_number = input("Enter student's new phone number: ")  # takes user input for new phone number
            self.phone_number = new_phone_number  # updates the student's recorded phone number to the new phone number
            return f"Phone number updated successfully to {self.phone_number}."  # displays to indicate that the phone number was updated
        elif choice == '2':  # when user chooses 2 updating address
            new_address = input("Enter student's new address: ")  # takes user input for new address 
            self.address = new_address  # updates the student's recorded address to a new address
            return f"Address updated successfully to {self.address}."  # displays to indicate that the address was updated
        else:
            return "Invalid input!"  # displays when user enters input that is not 1 or 2

    # a method to add student's internships
    def add_student_internship(self):
        # takes user input for student's internship details
        internship_details = {"Company name": input("Enter the name of the company the student interned at: "),
                              "Start date": input("Enter the start date of the internship (YYYY-MM-DD): "),
                              "End date": input("Enter the end date of the internship (YYYY-MM-DD): "),
                              "Position": input("Enter the position the student had in the internship: ")}

        self.internship.append(internship_details)  # appends student's internship details in the internship list
        return "Internship added successfully!"  # displays to indicate that the internship was recorded
