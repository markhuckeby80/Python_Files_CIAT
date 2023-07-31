# Three shcool subjects averages

Math = float(input("Enter Math Score: "))
Coding = float(input("Enter Coding Score: "))
English = float(input("Enter English Score: "))


Average = (Math + Coding + English) / 3

result = ""

if Average >= 85 : 
    result = "Excellent"
elif Average >= 65 : 
    result = "Passed"
elif Average <= 40 : 
    result = "Failed"

else:
    result = "Not Attending"

    

print(result)

