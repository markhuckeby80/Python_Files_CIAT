


# BMI result function that will be imported to the main function.

def bmi_result(BMI):
    
    if BMI < 16:
        print(f'Your BMI is {BMI:.2f} which means you are severely underweight.')
    elif BMI >= 16 and BMI < 16.9:
        print(f'Your BMI is {BMI:.2f} which means you are underweight.')
    elif BMI >= 17 and BMI < 18.4:
        print(f'Your BMI is {BMI:.2f} which means you are mildly underweight.')
    elif BMI >= 18.5 and BMI < 24.9:
        print(f'Your BMI is {BMI:.2f} which means you are normal weight.')
    elif BMI >= 25 and BMI < 29.9:
        print(f'Your BMI is {BMI:.2f} which means you are overweight.')
    elif BMI >= 30 and BMI < 34.9:
        print(f'Your BMI is {BMI:.2f} which means you are class 1 (moderately obese).')
    elif BMI >= 35 and BMI < 39.9:
        print(f'Your BMI is {BMI:.2f} which means you are class 2 (severely obese).')
    elif BMI >= 40:
        print(f'Your BMI is {BMI:.2f} which means you are class 3 (morbidly obese).')
    else:
        print(f'There is an error with your input.')
