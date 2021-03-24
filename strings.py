# STRING NOTES FROM STRING TUTORIAL VIDEO & TEXTBOOK CHAPTER 8.
# https://youtu.be/k9TUPpGqYTo

#### STRING BASICS ####
    # prints each letter separately.
        name = 'Juliet'
        for ch in name:
            print(ch)

    # string indexes
        string_name = 'Roses are red'
        print(string_name[0], string_name[6], string_name[10])
        # returns R a r

    # string length
    message = 'Hello world'
    print(len(message)) # find length of string, this returns 11

    # prevent loop from iterating beyond end of string
    city = 'Boston'
    index = 0
    while index < len(city):
        print(city[index])
        index += 1

#### SLICING ####
    message = 'Hello world'
    print(message[0:5]) # find range | 0 is starting point, and 5 is ending point minus one.
    print(message[:5]) # same as above
    print(message[6:]) # prints value at index position 6 through the end.

#### TEST, SEARCH AND MANIPULATE STRINGS ####
    
    # in and not in operators
    text = 'Four score and seven years ago'
    if 'seven' in text:
        print('the string seven was found.')
    if 'blanket' not in text:
        print('the string blanket was not found.')

#### STRING METHODS ####
    # general format: stringvariable.method(arguments) 
    
    #### STRING TESTING METHODS ####
    # RETURNS TRUE IF STRING IS....
        isalnum() # only alphabetic letters or digits
        isalpha() # only alphabetic letters
        isdigit() # only numeric digits
        islower() # all of the letters are lowercase 
        isspace() # only whitespace characters (\n) (\t)
        isupper() # all of the letters are uppercase

    #### STRING MODIFICATION METHODS ####
        lower()         # convert to lowercase
        lstrip()        # leading whitespace characters removed, spaces, (\n) (\t) at beginning
        lstrip(char)    # all instances of char that appear at beginning removed 
        rstrip()        # all whitespace characters removed, spaces, (\n) (\t) at end
        rstrip(char)    # all instances of char that appear at end removed
        strip()         # all leading and trailing whitespace characters removed
        strip(char)     # all instances of char that appear at the beginning and end removed.
        upper()         # convert to uppercase

    #### SEARCH AND REPLACE METHODS ####
        # Substring arguments below are any string
        endswith(substring)   # returns true if string ends with substring
        find(substring)       # returns the lowers index in the string where substring is found. 
                                # If substring is not found returns -1
        replace(old, new)     # replaces old with new
        startswith(substring) # returns true if string starts with substring

    #### STRING METHODS IN USE ####
        message = 'Hello world'
        print(message.lower()) # running lowercase method on string
        print(message.upper()) # runs uppercase

        print(message.count('Hello')) # must pass in an argument for this method. Returns 1.
        print(message.count('l')) # can also isolate single letters. Returns 3.

        print(message.find('world') # finds world, returns 6 because that's where it starts.

        # You cannot edit an existing string so this is how you make changes:
        message = message.replace('world', 'universe') # replaces world with universe.

        # Use split method to break a string into a list or to replace values.
        date_string = '11/26/2018'
        date_list = date_string.split('/') # variable is now ['11','26','2018']
        print('Month: ',date_list[0]) # returns Month: 11

#### CONCATENATE STRINGS ####
    # Concatenate strings - when you only have a few variables to concatenate:
    greeting = 'Hello'
    firstname = 'Tina'
    message = greeting + ' ' + firstname

    # Concatenating Strings using Formatted String:
        message = '{}, {}. Welcome!'.format(greeting, firstname) # older method
            # {} work as placeholders, and then we use the format method and include our arguments.
            # message printed returns 'Hello, Tina. Welcome!'

        # Formatted String "F string" logic - new way of formatting strings.
        message = f'{greeting}, {firstname}. Welcome!' # python 3.6 and higher method
            
            # and you can add functions to the placeholders:
            message = f'{greeting}, {firstname.upper()}. Welcome!' # adds all caps method

### SEE DIRECTORY AND GET HELP ###
    # See all methods available to variables using dir. 
    # Gives broad overview of all attributes and methods available.
        print(dir(firstname))

    # Get a description of methods.
        print(help(str))

    # Get more information on specific method.
        print(help(str.lower))


##### OPEN FILE AND READ CONTENTS TO A STRING #####
    a_file = open("sample.txt", "r")

    string_without_line_breaks = ""
    for line in a_file:
        stripped_line = line.rstrip()
        string_without_line_breaks += stripped_line
        a_file.close()

    print(string_without_line_breaks)