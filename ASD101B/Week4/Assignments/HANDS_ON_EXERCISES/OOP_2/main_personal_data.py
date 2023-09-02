# Import PersonalData class from personal_data.py file.
import personal_data as pd

# Define main function.
def main():

    # Ask the user to enter their name, address, age, and phone number.
    name = input('\nEnter your name : \n')
    address = input('Enter your address : \n')
    age = int(input('Enter your age : \n'))
    phone_number = input('Enter your phone number : \n')

    # Create an instance of the PersonalData class.
    my_data = pd.PersonalData(name, address, age, phone_number)

    # Ask the user to enter friend # 1 name, address, age, and phone number.
    name = input('\nEnter your friend # 1 name : \n')
    address = input('Enter your friend # 1 address : \n')
    age = int(input('Enter your friend # 1 age : \n'))
    phone_number = input('Enter your friend # 1 phone number : \n')

    # Create an instance of the PersonalData class.
    friend1_data = pd.PersonalData(name, address, age, phone_number)

    # Ask the user to enter friend # 2 name, address, age, and phone number.
    name = input('\nEnter your friend # 2 name : \n')
    address = input('Enter your friend # 2 address : \n')
    age = int(input('Enter your friend # 2 age : \n'))
    phone_number = input('Enter your friend # 2 phone number : \n')

    # Create an instance of the PersonalData class.
    friend2_data = pd.PersonalData(name, address, age, phone_number)


    # Display the data entered by the user.
    print(f'\nMy personal data : \n'
           'Name :', my_data.get_name(), '\n'
           'Address :', my_data.get_address(), '\n'
           'Age :', my_data.get_age(), '\n'
           'Phone number :', my_data.get_phone_number())

    print('\nFriend # 1 personal data : \n'
          'Name :', friend1_data.get_name(), '\n'
          'Address :', friend1_data.get_address(), '\n'
          'Age :', friend1_data.get_age(), '\n'
          'Phone number :', friend1_data.get_phone_number())

    print('\nFriend # 2 personal data : \n'
          'Name :', friend2_data.get_name(), '\n'
          'Address :', friend2_data.get_address(), '\n'
          'Age :', friend2_data.get_age(), '\n'
          'Phone number :', friend2_data.get_phone_number())

# Call the main function.
if __name__ == '__main__':
    main()
