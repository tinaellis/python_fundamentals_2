# This program takes a sentence inputted by the user
# and then takes that sentence and turns it into
# Pig Latin.

# Define the main function.

def main():

    print('Hello')
    print()
    print('Please enter a sentence to see what it would look like')
    print('in basic Pig Latin.')
    print()
    
    # Get the sentence:
    
    original_sentence = input('Enter the sentence you would like to translate: ')
    
    # Split the sentence, that way there isn't anything weird going on.
    original_sentence = original_sentence.split()
    
    # Try and create an empty list.
    pig_latin_sentence = []
    
    # Get the first letter of the word and put it to the back of the
    # word itself, then add the 'ay to that word.
    for word in original_sentence:
        if word[-1].isalpha():
            pig_latin_sentence = pig_latin_sentence.append(word[1:] + word[0] + 'ay')
            

        
            print()
            print(pig_latin_sentence)

main()