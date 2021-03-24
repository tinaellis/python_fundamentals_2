# Check to see what class type is stored within a variable.
    print(type(variable_name))


####### DICTIONARIES #######
# Syntax: variable_name = {'keyname':'value','keyname':'value'}

# Create empty dictionary.
    phonebook={}
    phonebook = dict() # built in dict() method also creates empty dictionary. 
        # make sure you didn't create anthing called dict 

# Create a dictionary with elements.
    phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joe':'555-3333'} # 'chris' = key & '555-1111' = value.
    example2 = dict([(1,"welcome"),(2,"to"),(3,"Python")]) # passing list - same result as above
    example3 = {1:'Welcome',2:'to',3:'Python'}  # just another example.

# Test if value is in a dictionary - allows you to avoid error exception.
    if 'Chris' in phonebook:
        print(phonebook['Chris'])

# Add elements to a dictionary.
    phonebook['Ray'] = '555-4444' # if key already exists, it's value will be changed.

    # add tuple to dictionary.
    phonebook['Place'] = ('New jersey','NY')
        # will print {'Ray':'555-4444', 'Place' ('New Jersey','NY')}

# Retreive value from dictionary.
    phonebook['Chris'] # returns '555-1111' | remember string comparisons are case sensitive.
    print(phonebook['Chris'])
        # Raises error exception if value doesn't exist.

# Delete element from dictionary.
    del phonebook['Chris'] # to prevent error exception, check if key exists before del.

# Get number of elements in a dictionary.
    number_elements = len(phonebook)

# Mix data types in a dictionary:
    # Keys can be strings, integers, tuples.
    # values can be integer, string, and lists.
    test_scores = {'Kayla':[88,92,100], 'Jacob':[95,74,81]}

# Assign dictionary value to a variable.
    kayla_scores = test_scores['Kayla']
    print(kayla_scores) # prints [88,92,100]

# Use for loop to iterate through values in a dictionary.
    for var in phonebook:
        print(key)
        # prints list of keys one by one.

    for key in phonebook:
        print(key,phonebook[key])
        # prints Chris 555-1111 and on down the list.

# Nested Dictionary
    student_info = {'Name':{'First':'Sam','Last':'Crew'},'Age':22,'Profession':'Student'}

    # Retrieving nested dictionary values:
    print(student_info['Name']['First'])

#### Some dictionary methods ####

# The clear method
    # deletes all elements in a dictionary leaving it empty.
    phonebook.clear()

# The get method
    # Doesn't raise exception if key isn't found, instead displays default message.
    dictionary.get(key, default)
    # Example: 
        value = phonebook.get('sam','no sam here')
        print(value) 
    # or
    print(phonebook.get('sam'))

# The items method
    # Returns all keys and values. They are returned as a special type of sequence known as 
    # a dictionary view. Each element in dictionary view is a tuble and each typle contains a key
    # and it's associated value.

    phonebook = {'Chris':'555-1111','Sally':'555-2222'}
    phonebook.items()
    # returns:
        [('Chris','555-1111'),('Sally','555-2222')]

# Uses items method and for loop to iterate over tuples:
    for key, value in phonebook.items():
        print(key,value)

# The keys method
    # Reutrns all of a dictionary's keys as a dictionary view.
    phonebook.keys()
    # returns ['Chris','Sally'] <-- just the keys

    # for loop to iterate over the sequence.
    for key in phonebook.keys():
        print(key)

# The pop method
    # Returns value of key and removes the key pair from the dictionary. If not found, returns
    # default value.
    phonebook = {'Chris':'555-1111','Sally':'555-2222'}
    phone_num = phonebook.pop('Andy','Element not found')
    # prints element not found

# The popitem method
    # returns a randomly selected key-value pair and removes it. The key-value pair is returned 
    # as a tuple.

    # with popitem do not specify the element you want to delete because it's always
    # the last element.
    phonebook.popitem()

    # use assignment statement to return key and value to individual variables.
    k, v = dictionary.popitem()

    # This assignment is known as a multiple assignment because multiple variables are being 
    # assigned at once.
    key, value = phonebook.popitem()
    print(key,value) # chris 555-1111

# The values method
    # Returns all dictionary values (without their keys) as dictionary view.
    phonebook.values()
    # returns ['555-1111','555-2222']

    # use for loop to iterate over sequence that is returned back:
    for val in phonebook.values():
        print(val)

# The fromkeys method
    # allows you to create a dictionary based on a set of predefined keys and values.
    keys = {'a','b','c','d'}
    value = 1
    dict.fromkeys(keys,value)
    # dictionary now looks like this {'c':1,'b':1,'a':1,'d':1}

####### SETS #######
# You can pass one iterable argument to the set function (lists, tuples, or string).
# Syntax: variable_name=set(['a','b','c','d'])

# Create a set
set1 = set()

# Convert a list to a set.
set1 = set(listname)
 # or: myset=set(['one','two','three'])

    # NOTE Strings are broken down into individual strings:
        myset=set('abc')
        # this becomes ('a','b','c')

# Get number of elements in a set
    myset = set([1,2,3,4,5])
    len(myset)

# Adding items
    myset = set()
    myset.add(1)
    myset.add(2)
    # {1,2}

# Updating a set
    myset = set([1,2,3,4,5])
    myset.update([6,7,8])

    # OR
    set1 = set([1,2,3,4,5])
    set2 = set([6,7,8])
    set1.update(set2)

# Remove an item
    # discard doesn't raise exceptions
    # remove raising exception if item doesn't exist
    myset.discard(s)
    myset.remove(1)
    # or
    myset.clear() # to clear all elements 

# Create a frozen set where the elements are immutable.
    set1=frozenset([1,2,3,4])
    
# Use loop to iterate over a set
myset = set(['a','b','c'])
for val in myset:
    print(val)

# Use in and not operators to test
if 1 in myset:
    print('yes')

if 11 not in my set:
    print('no')

# print items on a new line as it iterates.
print(*set1, sep = '\n')

---------------------------------------------------------------------------------------------
##### SET METHODS ######
set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7,8])

#### UNION METHOD ####
    # Union method to combine sets - sets don't allow duplicates. 
    # Good way to find all of the unique values contained in two different sets.
        
    set3 = set1.union(set2)
    # set3 now contains {1, 2, 3, 4, 5, 6, 7, 8}

    ### SHORTHAND: | ###
    set3 = set1 | set2

#### INTERSECTION METHOD ####
    # The intersection of two sets contains only the elements that are found in both sets.
    set3 = set1.intersection(set2)

    ### SHORTHAND: & ###
    set3 = set1 & set2

#### DIFFERENCE METHOD ####
    # The difference of set1 and set2 is the elements that appear in set1 but do not appear
    # in set2.

    set3 = set1.difference(set2)

    ### SHORTHAND: - ###
    set3 = set1 - set2

#### SYMMETRIC DIFFERENCE METHOD ####
    # The symmetric difference of two sets is a set that contains the elements that are
    # not shared by the sets.
    
    set3 = set1.symmetric_difference(set2)

    ### SHORTHAND: ^ ###
    set3 = set1 ^ set2
---------------------------------------------------------------------------------------------
### OPERATORS WITH SETS ###
set1 == set2 # returns true or false

set1 > set2 # returns true or false

### SUBSET AND SUPERSET ###
# If one set contains all of the same elements of another set it is considered 
# a subset and the other set is a superset.

    # returns true if it is false if not:

    # Find subset with issubset
    set2.issubset(set1) 
    # Find superset with issuperset
    set1.issuperset(set2)

    ### SHORTHAND: <= and >= ###
    set2 <= set1 # is set2 a subset of set1
    set1 >= set2 # is set1 a superset of set2

### PICKLING ###
# Serializing a object is the process of converting the object to a stream of bytes that
# can be saved to a file for later retrieval.

# Writing a pickled data.
    # import pickle
    import pickle

    # create your sets or objects.
    phonebook = {'Chris':'555-1111','Katie':'555-2222','Sam':'555-3333'}

    # Open file for binary writing:
    outputfile = open('mydata.dat','wb') # 'wb' is the mode for writing

    # Call pickles dump function:
    pickle.dump(phonebook,outputfile)

    # Close the file.
    outputfile.close()

# Retreive pickled data from file:
    import pickle
    input_file = open('phonebook.dat','rb') # 'rb' is the mode for reading
    pb = pickle.load(input_file)
    print(pb)
    input_file.close()

# If you try to read past the end of the file, EOFError exception is raised.
# see unpickle_objects for example of avoiding error exception.











