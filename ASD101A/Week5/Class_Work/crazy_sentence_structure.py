
# Create a program that takes in a sentence from the user /
# and returns a mixed-up version of the sentence.

import random

def crazy_sentence_structure(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Shuffle the words randomly
    random.shuffle(words)

    # Join the shuffled words back into a sentence
    crazy_sentence = ' '.join(words)
    return crazy_sentence


# Main program
if __name__ == "__main__":
    user_sentence = input("Enter a sentence to be crazified : \n")
    mixed_up_sentence = crazy_sentence_structure(user_sentence)
    print("Your new crazy sentence structure is :", mixed_up_sentence)