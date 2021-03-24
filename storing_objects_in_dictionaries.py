# CHAPTER 10 - PAGE 522 #
    # program contact_manage.py and contact.py allows users to lookup, add, change, delete and quit,
    # and pickles the dictionary.

######################################## CLASS METHOD ############################################
    class Contact:
        def __init__(self, name, phone, email):
            self.__name = name
            self.__phone = phone
            self.__email = email

        # mutators
        def set_name(self, name):
            self.__name = name

        def set_phone(self, phone):
            self.__phone = phone

        def set_email(self, email):
            self.__email = email

        # accessors
        def get_name(self):
            return self.__name

        def get_phone(self):
            return self.__phone

        def get_email(self):
            return self.__email

        # The __str__ method returns the object's state
        # as a string.
        def __str__(self):
            return "Name: " + self.__name + \
                "\nPhone: " + self.__phone + \
                "\nEmail: " + self.__email

############################################# PROGRAM #################################################
    import contact

    mycontacts = {} # create empty dictionary

    #### ADD OBJECT TO DICTIONARY ####
        # Create variables for data attributes.
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')

        # Create a Contact object named entry.
        entry = contact.Contact(name, phone, email)

        # add entry to dictionary.
            if name not in mycontacts:
                mycontacts[name] = entry
                print('The entry has been added.')
            else:
                print('That name already exists.')

    #### LOOKUP OBJECT IN DICTIONARY ####
        name = input('Enter a name: ')
        print(mycontacts.get(name, 'That name is not found.'))

    #### CHANGE OBJECT IN DICTIONARY ####
        name = input('Enter a name: ')

        if name in mycontacts:
            phone = input('Enter the new phone number: ')
            email = input('Enter the new email address: ')
            entry = contact.Contact(name, phone, email) # Create a contact object named entry.
            mycontacts[name] = entry # Update the entry.
            print('Information updated.')
        else:
            print('That name is not found.')

    #### DELETE OBJECT IN DICTIONARY ####
        name = input('Enter a name: ')

        if name in mycontacts:
            del mycontacts[name]
            print('Entry deleted.')
        else:
            print('That name is not found.')