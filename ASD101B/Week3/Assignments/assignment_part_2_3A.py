# 3. Assume that variable dct references a dictionary. Write and if statement that \
# determines whether the key 'James' exists in the dictionary. If so, display the value \
# that is associated with that key. If the key is not in the dictionary, display \
# a message indicating so.

# I wanted to modify this example by creating this dictionary with 12 key-value pairs, \
# however, I will just import the phoneLst dictionary from the assignment_part_2_3B.py file.\
# With this phone list, I can import this to the main program and use the same code.

from assignment_part_2_3B import phoneLst

def main():

    dct = phoneLst
    
    if 'James' in dct:
        print(dct['James'])
    else:
        print('James is not in the dictionary.')


if __name__ == '__main__':
    main()