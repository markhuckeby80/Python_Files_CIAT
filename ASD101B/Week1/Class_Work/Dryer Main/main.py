# This program displays step-by-step instructions
# for disassembling an Acme dryer.
# The main function performs the program's main logic.
from startup import *
from steps import *

def main():
    startup_message()                   # Display the start-up message.
    input('Press Enter to see Step 1.')
    step1()
    input('Press Enter to see Step 2.')
    step2()
    input('Press Enter to see Step 3.')
    step3()
    input('Press Enter to see Step 4.')
    step4()


if __name__ == '__main__':
    main()
