


# BMI Calculator Function that will be imported to the main function.

def bmi_calculator():

    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    BMI = weight / (height ** 2)
    return BMI