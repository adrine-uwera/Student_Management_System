# Importing child classes from their files
from computer_science_student import ComputerScienceStudent
from global_challenges_student import GlobalChallengesStudent
from international_business_and_trade_student_class import InternationalBusinessAndTradeStudent
from entrepreneurship_student_class import EntrepreneurshipStudent
import sys  # Sys module will allow us to use exit function for ending the program when needed
import csv  # CSV module will allow us to work with a csv file for storing students data and to manipulate that data

print("\nALU STUDENT MANAGEMENT SYSTEM")
print("-----------------------------")


# a function to rerun the program to allow user to perform different operations in a row
def re_run():
    # This loop will keep asking the user whether they want to do any other operation until they enter either 'Y' or 'N'
    while True:
        operation2 = str(input("\nEnter 'Y' if you would like to do any other operation and 'N' if you do not want to: "))
        if operation2.upper() in ('Y', 'N'):
            break  # The loop will only break if the user enter either 'Y' or 'N'
        print("\nInvalid input. Choose 'Y' or 'N'.\n")  # Whenever a user enter something which is not 'Y' or 'N',this
        # message will be printed
    if operation2.upper() == 'Y':
        main()  # If the user enter 'Y', the main function will be called
    else:
        sys.exit("Thank you!!")  # If the user enter 'N', function sys.exit() will be called to end the program


# This function will retrieve student information from the file
def retrieve_student(email):
    try:
        # Opens the file in which all students records are kept in read mode as file object student_records
        with open("student_records.csv", 'r') as student_records:
            read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
            # read_student as a list
            for student in read_student:   # Looping through all lines(students) in the file
                # since each line is a list itself, and the student email is the first item the condition is checking
                # for each line if the element at index [0] is equal to the email specified by the program needs to
                # locate the line on which information about that student is kept
                if email == student[0]:
                    if student[6] == "Computer Science":    # If the above condition is met and the student's major
                        # located on index 6 on line (since a line is represented as a list) is computer science a
                        # ComputerScienceStudent instance will be created and information to be passed to the init
                        # method will be extracted from the file as the student is already recorded
                        student1 = ComputerScienceStudent(
                            student_email=student[0],
                            student_name=student[1],
                            gender=student[2],
                            date_of_birth=student[3],
                            address=student[4],
                            phone_number=student[5],
                            date_of_enrollment=student[7],
                            year=int(student[8]),
                            github_username=student[10])
                        return student1  # The function will return the instance created

                    elif student[6] == "International Business And Trade":  # If the above condition is met and the
                        # student's major located on index 6 on line (since a line is represented as a list) is
                        # International Business And Trade an InternationalBusinessAndTradeStudent instance will be
                        # created and information to be passed to the init method will be extracted from the file as the
                        # student is already recorded
                        student1 = InternationalBusinessAndTradeStudent(
                            student_email=student[0],
                            student_name=student[1],
                            gender=student[2],
                            date_of_birth=student[3],
                            address=student[4],
                            phone_number=student[5],
                            date_of_enrollment=student[7],
                            year=int(student[8]))
                        return student1  # The function will return the instance created

                    elif student[6] == "Global Challenges":  # If the above condition is met and the student's major
                        # located on index 6 on line (since a line is represented as a list) is  Global Challenges a
                        # GlobalChallengesStudent instance will be created and information to be passed to the init
                        # method will be extracted from the file as the student is already recorded
                        student1 = GlobalChallengesStudent(
                            student_email=student[0],
                            student_name=student[1],
                            gender=student[2],
                            date_of_birth=student[3],
                            address=student[4],
                            phone_number=student[5],
                            date_of_enrollment=student[7],
                            year=int(student[8]),
                            mission=student[10])
                        return student1  # The function will return the instance created

                    elif student[6] == "Entrepreneurship":  # If the above condition is met and the student's major
                        # located on index 6 on line (since a line is represented as a list) is Entrepreneurship a
                        # EntrepreneurshipStudent instance will be created and information to be passed to the init
                        # method will be extracted from the file as the student is already recorded
                        student1 = EntrepreneurshipStudent(
                            student_email=student[0],
                            student_name=student[1],
                            gender=student[2],
                            date_of_birth=student[3],
                            address=student[4],
                            phone_number=student[5],
                            date_of_enrollment=student[7],
                            year=int(student[8]))
                        return student1   # The function will return the instance created

            else:  # Specifies what the function will return if no line has the email specified by the user
                return "Couldn't find the student with email provided! Check the email and try again.\n"

    except OSError as e:
        print("File not found", e)  # This will be printed if a file can not be accessed, e represents exception-type
        # object and it will give more clarity on the OSError which occurred
        sys.exit()  # Ends the program with exit function as the user will not be able to do any operation without an
        # instance


# Main function which allow the user to choose and perform an operation
def main():
    # Asking user their category as they have differences in operations they can access
    print("\nUser categories:\n"
          "1. Registrar Office\n"
          "2. Student\n")
    while True:  # This loop will keep asking the user their category until they enter either '1' or '2'
        user = input("Enter choice '1' or '2': ")
        if user in ('1', '2'):
            break  # The loop will only break if the user enter either '1' or '2'
        print("\nInvalid input. Choose '1' or '2'.\n")  # Whenever a user enter something which is not '1' or '2',this
        # message will be printed
    if user == '1':    # This condition specifies what follows if the user category is registrar office
        # displays a menu to choose from, registrar office must access to performing any operation
        print("\nChoose \n"
              "1. Register student\n"
              "2. View student information\n"
              "3. Promote student\n"
              "4. Change student status\n"
              "5. Update student information\n"
              "6. View degree program outline\n"
              "7. Add student internship\n"
              "8. Add student venture\n"
              "or other key to exit\n")
        action = input("Enter your choice: ")
        if action == '1':   # when user from registrar office choose to register a student
            print("\nRegister student")
            print("----------------")
            print("Choose major the student will be taking:\n"
                  "1. Computer science\n"
                  "2. International Business and Trade\n"
                  "3. Global challenges\n"
                  "4. Entrepreneurship\n")  # displays menu to choose from the major of the student they want to create
            student_major = input("Enter choice: ")
            if student_major == '1':   # When the student's major is computer science
                try:
                    # creates an object of ComputerScienceStudent class i.e a computer science student
                    ComputerScienceStudent(
                        student_email=input("Enter student's email: "),
                        student_name=input("Enter student's name: "),
                        gender=input("Enter student's gender: "),
                        date_of_birth=input("Enter student's date of birth (YYYY-MM-DD) and use digit: "),
                        address=input("Enter student's address: "),
                        phone_number=input("Enter student's phone number: "),
                        date_of_enrollment=input("Enter student's date of enrollment (YYYY-MM-DD) "
                                                 "separated by space and use digit: "),
                        year=input("Enter student's year of study in digit: "),
                        github_username=input("Enter student's Github username: "))

                except ValueError:  # handles the exception when user enters a non-numerical character for student's year
                    print("The student year should be an integer.")   # message displayed when the ValueError occurs

            elif student_major == '2':  # when student major is International business and trade
                try:
                    # creates an object of InternationalBusinessAndTradeStudent class i.e a International Business and
                    # Trade student
                    InternationalBusinessAndTradeStudent(
                        student_email=input("Enter student's email: "),
                        student_name=input("Enter student's name: "),
                        gender=input("Enter student's gender: "),
                        date_of_birth=input("Enter student's date of birth (YYYY-MM-DD): "),
                        address=input("Enter student's address: "),
                        phone_number=input("Enter student's phone number: "),
                        date_of_enrollment=input("Enter student's date of enrollment (YYYY-MM-DD) "
                                                 "separated by space and use digit: "),
                        year=input("Enter student's year of study in digit: "))

                except ValueError:  # handles the exception when user enters a non-numerical character for student's year
                    print("The student year should be an integer.")  # message displayed when the ValueError occurs

            elif student_major == '3':   # when student major is Global challenges
                try:
                    # creates an object of GlobalChallengesStudent class i.e a Global Challenges student
                    GlobalChallengesStudent(
                        student_email=input("Enter student's email: "),
                        student_name=input("Enter student's name: "),
                        gender=input("Enter student's gender: "),
                        date_of_birth=input("Enter student's date of birth: "),
                        address=input("Enter student's address: "),
                        phone_number=input("Enter student's phone number: "),
                        date_of_enrollment=input("Enter student's date of enrollment (YYYY-MM-DD) "
                                                 "separated by space and use digit: "),
                        year=input("Enter student's year of study in digit: "),
                        mission=input("Enter student's mission: "))
                except ValueError:  # handles the exception when user enters a non-numerical character for student's year
                    print("The student year should be an integer.")   # message displayed when the ValueError occurs

            elif student_major == '4':  # when student major is entrepreneurship
                try:
                    # creates an object of EntrepreneurshipStudent class i.e a Entrepreneurship student
                    EntrepreneurshipStudent(
                        student_email=input("Enter student's email: "),
                        student_name=input("Enter student's name: "),
                        gender=input("Enter student's gender: "),
                        date_of_birth=input("Enter student's date of birth (YYYY-MM-DD): "),
                        address=input("Enter student's address: "),
                        phone_number=input("Enter student's phone number: "),
                        date_of_enrollment=input("Enter student's date of enrollment (YYYY-MM-DD) "
                                                 "separated by space and use digit: "),
                        year=input("Enter student's year of study in digit: "))
                except ValueError:  # handles the exception when user enters a non-numerical character for student's year
                    print("The student year should be an integer.")  # message displayed when the ValueError occurs

        elif action == '2':   # when user from registrar office choose to view student information
            print("\nStudent information")
            print("-------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to view information
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":  #
                print(student2)  # if the email was not found in any students records meaning that there is no student
                # registered with such an email as all students are recorded on file upon instance creation the
                # program will print a message returned by the function which retrieves student data
            else:
                print(student2.print_student_information())  # If the student information was retrieved successfully
                # the object returned by the function will call the print_student_information method in its class.

        elif action == '3':   # when user from registrar office choose to promote a student
            print("\nPromote student")
            print("---------------")
            email = input("Enter student email: ")  # takes user input of student's email to promote
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                print(student2.promote_student())  # If the student information was retrieved successfully
                # the object returned by the function will call the promote_student method in its class.

        elif action == '4':  # when user from registrar office choose to change student's status
            print("\nChange student's status")
            print("-----------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to change status
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                print(student2.change_student_status())  # If the student information was retrieved successfully
                # the object returned by the function will call the change_student_status method in its class.

        elif action == '5':   # when user from registrar office choose to update student information
            print("\nUpdate student information")
            print("--------------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to update information
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                print(student2.update_student_information())  # If the student information was retrieved successfully
                # the object returned by the function will call the update_student_information method in its class.

        elif action == '6':  # when user from registrar office choose to view degree program of a certain course
            print("\nView degree program outline")
            print("---------------------------")
            print("Choose degree program you want to view outline for:\n"
                  "1. Computer science\n"
                  "2. International Business and Trade\n"
                  "3. Global challenges\n"
                  "4. Entrepreneurship\n")  # displays menu to choose from the degree program they want to view outline for
            degree_program = input("Enter choice 1,2,3, or 4: ")
            if degree_program == "1":  # If they choose to view for computer science degree program
                ComputerScienceStudent.view_degree_program_outline()
            elif degree_program == "2":  # If they choose to view for International Business And Trade degree program
                InternationalBusinessAndTradeStudent.view_degree_program_outline()
            elif degree_program == "3":  # If they choose to view for global challenges degree program
                GlobalChallengesStudent.view_degree_program_outline()
            elif degree_program == "4":  # If they choose to view for Entrepreneurship degree program
                EntrepreneurshipStudent.view_degree_program_outline()
            else:  # If the user enters choice which is not in 1,2,3, or 4
                print("Invalid input!!")

        elif action == '7':  # when user from registrar office choose to add student's internship.
            print("\nAdd student internship")
            print("----------------------")
            email = input("Enter student email: ")  # takes user input of student's email to add internship to
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                print(student2.add_student_internship())  # If the student information was retrieved successfully
                # the object returned by the function will call the add_student_internship method in its class.

        elif action == '8':  # when user from registrar office choose to add student's internship
            print("\nAdd student's venture")
            print("---------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to add venture to
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                if student2.major == "International Business And Trade" or student2.major == "Entrepreneurship":
                    print(student2.add_venture_details())  # If the student information was retrieved successfully and
                    # their major is "International Business And Trade" or "Entrepreneurship" the object returned
                    # by the function will call the add_student_venture_details method in its class.

                else:
                    # displayed when the student major is not "International Business And Trade" or "Entrepreneurship"
                    print("Student's major must be IBT or ENT to add venture.")

    elif user == '2':  # This condition specifies what follows if the user category is student
        # Displays menu for students
        print("\nChoose \n"
              "1. Update information\n"
              "2. View degree program outline\n"
              "3. Add internship\n"
              "4. Add venture")
        action = input("Enter choice: ")
        if action == '1':  # when student chooses to update their information
            print("\nUpdate student information")
            print("--------------------------")
            email = input("Enter your email: ")  # email of student who wants to update their information
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                print(student2.update_student_information())  # If the student information was retrieved successfully
                # the object returned by the function will call the update_student_information method in its class.

        elif action == '2':  # when student chooses to view their degree program outline
            print("\nView degree program outline")
            print("---------------------------")
            email = input("Enter your email: ")  # email of student who wants to view their degree program outline
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                student2.view_degree_program_outline()  # If the student information was retrieved successfully
                # the object returned by the function will call the view_degree_program_outline method in its class.

        elif action == '3':  # when student chooses to add an internship to their record
            print("\nAdd internship")
            print("----------------")
            email = input("Enter your email: ")  # email of student who wants to add internship
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                print(student2.add_student_internship())  # If the student information was retrieved successfully
                # the object returned by the function will call the add_student_internship method in its class.

        elif action == '4':  # when student chooses to add a venture
            print("\nAdd venture")
            print("-----------")
            email = input("Enter your email: ")  # email of student who wants to add venture
            student2 = retrieve_student(email)  # Calls the method which retrieves data from the students records and
            # creates an instance of that student, the email provided is passed to it and the instance returned by
            # the method is initialized to variable "student2"
            if student2 == "Couldn't find the student with email provided! Check the email and try again.\n":
                print(student2)  # if the email was not found in any students records the program will print a
                # message returned by the function which retrieves student data
            else:
                if student2.major == "International Business And Trade" or student2.major == "Entrepreneurship":
                    print(student2.add_venture_details())  # If the student information was retrieved successfully and
                    # their major is "International Business And Trade" or "Entrepreneurship" the object returned
                    # by the function will call the add_student_venture_details method in its class.

                else:
                    # displayed when the student major is not "International Business And Trade" or "Entrepreneurship"
                    print("Student's major must be IBT or ENT to add venture.")

    re_run()  # After the user has finished any operation the function which asks them if they want to do another
    # operation will be called


# This code calls the 'main' function
if __name__ == '__main__':
    main()
