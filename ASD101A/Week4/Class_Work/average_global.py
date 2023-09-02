# write a function to accept grades three subjects, calculate the average 


average = 0
grade = ""


def calculate_grade () :

    philosophy = float(input("Enter the final grade percentage for philosophy : "))
    calculus = float(input("Enter the final grade percentage for calculas : "))
    python_coding = float(input("Enter the final grade percentage for python coding : "))


    global average
    average = (philosophy + calculus + python_coding) // 3        
    global grade

    if average >= 85 : 
        grade = "A"
    elif average >= 75 and average < 85 : 
        grade = "B"
    elif average < 75 and average > 60 : 
        grade = "C"

    else:
        grade = "Not Attending"




calculate_grade ()



print(average, grade)




    


