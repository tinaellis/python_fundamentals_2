### create empty lists, tuples and sets ###
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()

#### LISTS ####

 _items_in_list = len(listname)
access_values_in_list = print(listname[0]) 
    # index 0 is the starting value. 
    # This can be negative if you want to start from end
access_range_of_values = print(listname[0:2]) # This is called Slicing
    # this would return all values from beginning not including 2
    # listname[:2] would return same results
    # listname[2:] would start index at position 2 and go through end
listname.append(item)
    #The append() method adds an item to the end of the list.

listname1 = [1,2,3]
listname2 = []
for item in listname1:
    listname2.append(item)
    # makes a copy of a list

listname.extend(list2)
    # adds a list onto an existing list. Not to be confused with append.
listname.remove('Math')
    # removes 'math' item from the list

listname = [1,2,3,4,5]
del listname[2]
    # the del statement deletes an item at a specific index location.

listname.insert(0,'Joe')
    # Inserts Joe at position 0. The item that was there and all others are shifted
    # 1 position towards the end.

listname.pop() 
    # .pop removes last item from a list
popped = courses.pop() 
    # returns the value it removed | you'd do print(popped)
listname.reverse()
    # reverses the list
listname.sort()
    # sorts by assending order - alterate original
listname.sort(reverse=True)
    # sorts by descending order - alterates original
sortedlist = sorted(listname)
    # using sorted this way prevents alterating the orginal list



print(min(listname)) # retreives minimum value in list
print(max(listname)) # retreives max value in list
print(sum(listname)) # retreives sum of list

find_index_of_item = print(listname.index('Art')) # returns index position of value
get_true_or_false = print('Math' in listname) # use in method to find if value exists

# See index of items while looping throug items in list:
for index, item in enumerate(listname):
    print(index,value)
    # if you don't want to start at index 0, pass through a 
    # starting value as an argument:
    for index, item in enumerate(listname, start=1):
        print(index,value)

# Turn list into a comma separated list of values:
list_str = ', '.join(listname) # join method does this - include space
    # To reverse this:
    list_str_reverse = list_str.split(', ') # removes all of the commas & spaces.

# Flatten a nested list - flatten two-dimensional list.
grid = [[4,9,2],[3,5,7],[8,1,6]] # the given two-dimensional list.
flat_list = [item for l in grid for item in l] # unnest the list.
    # results will be flat_list = [4,9,2,3,5,7,8,1,6]

#### TUPLES ####
# tuples are immutable - can't be changed.
tuple_lists = (1,2,3,4) # parenthesis

#### SETS ####
set_lists = {'Curly','Brackets','Rock'} # curly brackets
# Sets automatically remove duplicates
# Sets do not keep order of items

find_if_value_is_in_list = print('math' in setname) # called a membership test

# Find what values a set shares or doesn't share with another set:
print(setname.intersection(setname2)) # intersection method
    # results return the values that are in both sets

print(setname.difference(setname2)) # difference method
    # results return the values that are in setname but not setname2

# Combine sets using union method.
setname.union(setname2) # union method
    # Combines sets and automatically removes duplicates. 

#### Converting between Lists and Tuples ####

# Convert tuple to list:
number=(1,2,3)
number_list = list(number)

# Convert list to tuple:
number = ['one','two','three']
number_tuple = tuple(number)

