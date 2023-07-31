# Calculating the percentages of Females and Males

females = float(input('Enter the number of females: '))
males = float(input('Enter the number of males: '))

total = females + males

# Performing the Calculations

percentFemale = females / total
percentMale = males / total

# Displaying the output

print(f'Total number of students: {total}')
print(f'Percentage of Females: {percentFemale:.0%}')
print(f'Percentage of Males: {percentMale:.0%}')
      
