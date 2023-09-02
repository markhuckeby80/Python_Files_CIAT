# pg. 441 Program 8-3

def get_login_name(first, last, idnumber):
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = idnumber[0:3]

    login_name = set1 + set2 + set3
    return login_name

# pg. 450 Program 8-6

def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    if len(password) >= 7:
        correct_length = True

        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True

    else:
        is_valid = False

    return is_valid

if __name__ == '__main__':
    newID = get_login_name('Holly', 'Gaddis', 'CSC34899')
    print(newID)
    test = valid_password('252dsfRE#$')
    print(test)
