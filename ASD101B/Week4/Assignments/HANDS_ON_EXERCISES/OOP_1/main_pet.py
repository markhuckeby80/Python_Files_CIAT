# Importing the Pet class from the pet.py file.
import pet

# Define the main function.
def main():

    # Create an object from the Pet class.
    pet_name = input("Enter the name of your pet : \n")
    pet_type = input("Enter the type of your pet : \n")
    pet_age = int(input("Enter the age of your pet : \n"))
    my_pet = pet.Pet(pet_name, pet_type, pet_age)

    # Display the data that was entered.
    print(f'Here is the data that you entered : \n'
           'Pet Name :', my_pet.get_name(), '\n'
           'Pet Type :', my_pet.get_animal_type(), '\n'
           'Pet Age :', my_pet.get_age())


# Call the main function.
if __name__ == "__main__":
    main()
