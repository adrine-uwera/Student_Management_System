from computer_science_student import ComputerScienceStudent     # imports ComputerScienceStudent class from computer_science_student file
from global_challenges_student import GlobalChallengesStudent   # imports GlobalChallengesStudent class from global_challenges_student file
from international_business_and_trade_student_class import InternationalBusinessAndTradeStudent  # imports InternationalBusinessAndTradeStudent class from international_business_and_trade_student_class file
from entrepreneurship_student_class import EntrepreneurshipStudent  # imports EntrepreneurshipStudent from entrepreneurship_student_class file
from student import student_records     # imports student_records array from student file
import sys  # imports sys library

print("\nALU STUDENT MANAGEMENT SYSTEM")
print("-----------------------------")


# a function to rerun the program to allow user to perform different operations in a row
def re_run():
    # creates a loop to allow user to perform different operations in a row until he/she decides to exit
    while True:  # This loop will keep asking the user whether they want do any other operation until they enter 'Y' or 'N'
        operation2 = str(
            input("\nEnter 'Y' if you would like to do any other operation and 'N' if you do not want to: "))  # allows user to specify if he/she wants to do another operation
        if operation2.upper() in ('Y', 'N'):
            break       # the loop will only break when the user enters 'Y' or 'N'
        print("\nInvalid input. Choose 'Y' or 'N'.\n")  # Whenever a user enter something which is not 'Y' or 'N', this message will be printed
    if operation2.upper() == 'Y':   # when user enters 'Y', the main function will be called
        main()
    else:
        sys.exit("Thank you!!")   # If the user enter 'N', function sys.exit() will be called to end the program


# a function for flow control among operations
def main():
    print("\nUser categories:\n"
          "1. Registrar Office\n"
          "2. Student\n")       # displays a menu to choose from
    while True:  # This loop will keep asking the user their category until they enter either '1' or '2'
        user = input("Enter choice: ")
        if user in ('1', '2'):
            break    # The loop will only break if the user enter either '1' or '2'
        print("\nInvalid input. Choose '1' or '2'.\n") # Whenever a user enter something which is not '1' or '2', this message will be printed
    if user == '1':     # when user is from the registrar office
        print("\nChoose \n"
              "1. Register student\n"
              "2. View student information\n"
              "3. Promote student\n"
              "4. Change student status\n"
              "5. Update student information\n"
              "6. View degree program outline\n"
              "7. Add student internship\n"
              "8. Add student venture\n"
              "or other key to exit\n")     # displays a menu to choose from
        action = input("Enter your choice: ")   # takes user input about the operation to be performed
        if action == '1':   # when user from registrar office choose to register a student
            print("\nRegister student")
            print("----------------")
            print("Choose major the student will be taking:\n"
                  "1. Computer science\n"
                  "2. International Business and Trade\n"
                  "3. Global challenges\n"
                  "4. Entrepreneurship\n")  # displays a menu to choose from
            student_major = input("Enter choice: ")     # takes user input to specify the major of the student to be registered
            if student_major == '1':    # when student major is computer science
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
                        year=int(input("Enter student's year of study in digit: ")),
                        github_username=input("Enter student's Github username: "))
                except ValueError:  # handles the exception when user enters a string for student's year
                    print("The student year should be an integer.")     # message displayed when the ValueError occurs

            elif student_major == '2':  # when student major is International business and trade
                try:
                    # creates an object of InternationalBusinessAndTradeStudent class i.e a International Business and Trade student
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
                except ValueError:  # handles the exception when user enters a string for student's year
                    print("The student year should be an integer.")     # message displayed when the ValueError occurs

            elif student_major == '3':  # when student major is Global challenges
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
                except ValueError:  # handles the exception when user enters a string for student's year
                    print("The student year should be an integer.")  # message displayed when the ValueError occurs
                    
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
                except ValueError:  # handles the exception when user enters a string for student's year
                    print("The student year should be an integer.")  # message displayed when the ValueError occurs

        elif action == '2':     # when user from registrar office choose to view student information
            print("\nStudent information")
            print("-------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to view information
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    print(student.print_student_information())  # calls the print_student_information() method and display student's information
                    break
            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '3':     # when user from registrar office choose to promote a student
            print("\nPromote student")
            print("---------------")
            email = input("Enter student email: ")   # takes user input of student's email for whom to promote
            for student in student_records:  # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    print(student.promote_student())    # calls the print_student_information() method and display student's information
                    break
            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '4':     # when user from registrar office choose to change student's status
            print("\nChange student's status")
            print("-----------------------")
            email = input("Enter student email: ")   # takes user input of student's email for whom to change status
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    print(student.change_student_status())  # calls the change_student_status() method
                    break
            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '5':  # when user from registrar office choose to update student information
            print("\nUpdate student information")
            print("--------------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to update information
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    print(student.update_student_information())     # calls update_student_information() method
                    break

            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        # Registrar office must access to performing any operation
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

        elif action == '7':  # when user from registrar office choose to add student's internship. can be in case a student had issues with the system.
            print("\nAdd student internship")
            print("----------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to add internship
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    print(student.add_student_internship())  # calls the add_student_internship() method
                    break

            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '8':     # when user from registrar office choose to add student's internship
            print("\nAdd student's venture")
            print("----------------------")
            email = input("Enter student email: ")  # takes user input of student's email for whom to add venture
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    if student.major == "International Business And Trade" or student.major == "Entrepreneurship":
                        print(student.add_venture_details())    # calls the add_venture_details() method
                        break
                    else:
                        # displayed when the student major is not "International Business And Trade" or "Entrepreneurship"
                        print("Student's major must be IBT or ENT to add venture.")

            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

    elif user == '2':
        print("\nChoose \n"
              "1. Update information\n"
              "2. View degree program outline\n"
              "3. Add internship\n"
              "4. Add venture")     # displays a menu to choose from
        action = input("Enter choice: ")
        if action == '1':
            print("\nUpdate student information")
            print("--------------------------")
            email = input("Enter your email: ")     # takes user input of student's email for whom to update student information
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    print(student.update_student_information())     # calls the update_student_information() method
                    break

            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '2':
            print("\nView degree program outline")
            print("---------------------------")
            email = input("Enter your email: ")  # takes user input of student's email for whom to view degree program outline
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    student.view_degree_program_outline()   # calls the view_degree_program_outline() method
                    break

            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '3':
            print("\nAdd internship")
            print("---------------")
            email = input("Enter your email: ")     # takes user input of student's email for whom to add internship
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    print(student.add_student_internship())  # calls the add_student_internship() method
                    break

            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '4':
            print("\nAdd venture")
            print("----------------")
            email = input("Enter your email: ")     # takes user input of student's email for whom to add venture
            for student in student_records:     # loops through the student_records array
                if student.student_email == email:  # checks if the email provided matches any in the student records
                    if student.major == "International Business And Trade" or student.major == "Entrepreneurship":  # checks if the student major is IBT or entrepreneurship
                        print(student.add_venture_details())    # calls the add_venture_details() method
                        break
                    else:
                        # displayed when the student major is not "International Business And Trade" or "Entrepreneurship"
                        print("You must be an IBT or ENT major to add venture.")
            else:
                # displayed when the email provided doesn't match any email in the student records
                print("Couldn't find the student with email provided! Check the email and try again.\n")

    re_run()    # calls the re_run() function


# This code calls the 'main' function
if __name__ == '__main__':
    main()
