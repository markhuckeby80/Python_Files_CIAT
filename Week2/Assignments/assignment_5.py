# Nested descision structure using if and else statements

# Defining variables

amount1=int(input('Enter amount1:'))
amount2=int(input('Enter amount2:'))

# Performing the if and else statements and displaying the results

if amount1> 10 and amount2< 100:
    if amount1>amount2:
       print('amount1 is greater')
    elif amount2>amount1:
       print('amount2 is greater')
    else:
       print('Amounts not in valid range')