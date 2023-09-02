# Pg. 434 Program 8-1

def main():
    count = 0

    myString = input("Enter a sentence : \n")

    for ch in myString:
        # if ch == 'T' or ch == 't':
        if ch.lower() == 't':
            count += 1
    
    print(f'The letter T appears {count} times.')

if __name__ == "__main__":
    main()
