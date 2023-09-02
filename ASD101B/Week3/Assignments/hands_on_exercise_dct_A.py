# I wanted to again use to call the contents of the dictionary from a separate file. \
# So, if I wanted to update the dictionary, I could do so in the other file and it would \
# not affect the main program.

from hands_on_exercise_dct_B import courseNum

# Created a function to call the dictionary and print the values
def main():

    # calling the dictionary from the other file
    dct = courseNum
    
    # Prompt user for course number
    course = input('Enter a course number : \n').upper()

    print()

    # Validate input
    while course not in dct:
        print('Invalid Entry.')
        course = input('Enter a course number : \n').upper()

    # Print the values       
    if course in dct:
        print('Room number: ', dct[course][0] + '\n'
              'Instructor: ', dct[course][1] + '\n'
              'Meeting time: ', dct[course][2])

    print()

    # Ask the user if they would like to look up another course
    again = input('Would you like to look up another course? (y/n) : \n').lower()

    print()

    # Validate input
    while again != 'y' and again != 'n':
        print('Invalid Entry.')
        again = input('Would you like to look up another course? (y/n) : \n').lower()

    # If the user wants to look up another course, call the main function again
    if again == 'y':
        main()

if __name__ == '__main__':
    main()
