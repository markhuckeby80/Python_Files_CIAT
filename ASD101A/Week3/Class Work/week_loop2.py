# Creating a student loop

student_list = []
answer = "y"


while answer == "y" or answer == "Y":
    
    student_name = input("Enter the student name: \n")

    student_list.append(student_name)

    answer = input ("You want to add more students ?")