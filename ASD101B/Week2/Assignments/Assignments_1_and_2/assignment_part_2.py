


# Two predefined lists
lst1 = ['salamander','triceratops','cheetah','puma']
lst2 = ['banana','banana','banana','banana','orange you glad I didn\'t say banana?']

# Create a small program that does the following:
# determines which list is shorter
# prints the last element of the shorter list

# Determine which list is shorter
if len(lst1) < len(lst2):
    # Print the last element of the shorter list
    print(lst1[-1])
else:
    # Print the last element of the shorter list
    print(lst2[-1])
