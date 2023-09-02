


# Creating a program to allow the user to enter \
# a file with intent to split the file into a list.

def main():
    
    # Creating a while loop to allow the user to enter a file name until the file is found.
    while True:

        # User input to enter the name of the file.
        filename = input("Enter the name of a file : \n")
        
        # Converting the user input to lowercase.
        filename = filename.lower()
        
        # Concatenating the path to the file with the user input. 
        # Also the user does not have to add the file extension.
        filepath = (
        r"C:\Users\markh\OneDrive\Documents\Mark_Python_Files\ASD101B\Week2\Assignments\Hands_on_Exercise_File_and_List"
            + f"\{filename}.txt")


        # Opening the file using the try and except statements.
        try:

            with open(filepath, 'r') as infile:
            
                # Reading the contents of the file.
                contents = infile.read()
                
                # Split the contents into lines.
                lines = contents.split('\n')

                # Create a list to hold the states.
                states = [" "]

                # Create list to hold the numbers.
                numbers = [" "]

                # Loop through the lines.
                for line in lines:
                        
                        # Split the line into words.
                        words = line.split()
    
                        # Add the state to the states list.
                        states.append(words[1])
    
                        # Add the number to the numbers list.
                        numbers.append(words[0])

                # Print an empty line.
                print()
                        
                # Print the list of states in descending order.
                states.sort(reverse=True)
                for state in states:
                    print(state)


            # Closing the file.
            infile.close()

            # Exit the loop if the file is found.
            break

        # If the file is not found the user will be prompted to enter a new file name.
        except IOError:
            print("An error occurred trying to read the file", f"{filename}.txt")
            print("Please try again.")


# Calling the main function.
if __name__ == "__main__":
    main()
