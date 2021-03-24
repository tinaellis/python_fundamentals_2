#### Object Oriented Programming ####
    # Object contains both data and procedures:
        # Data = data attributes
        # Procedures = methods
    # Encapsulation is what happens when you combine data and code into a single object.

######################################## CLASSES ###########################################

--------------------------------------------------------------------------------------------
############################## EXAMPLE 1 - SIMPLE INFO CLASS ###############################
--------------------------------------------------------------------------------------------
    class PersonalInfo: # class name
        
        # Initializes the attributes.
        def __init__(self,name,address,age): # include self in the attributes and arguments
            self.__name = name
            self.__address = address
            self.__age = age
        
        # mutators to accept arguments (the set methods).
            # These mutators are only needed if attribute data will be changed during the program execution.
            #### NOTESS arguments are not always needed - method might perform calculation etc.

        def set_name(self, name): # "name" argument comes from the file where set_name is being called.
            self.__name = name
        
        def set_address(self, address): # "address" argument comes from the file where set_address is being called.
            self.__address = address

        def set_age(self, age): # "age" argument comes from the file where set_age is being called.
            self.__age = age

        # accessors to return attribute values (the get methods).
        def get_name(self):
            return self.__name
        
        def get_address(self):
            return self.__address

        def get_age(self):
            return self.__age

        # string method displays information when print function is called.
        def __str__(self):
            return "Name: " + self.__name + \
                "\nAddress: " + self.__animal_type + \
                    "\nAge: " + self.__age
    
    ### FILE THAT IMPORTS CLASS ###
        import personalinfo

        # variables created for attribute data:
        name = input('Please enter your name: ')
        address = input('Please enter your address: ')
        age = input('Please enter your age: ')

        # create class instance for info and assign values to attributes.
        info = personalinfo.PersonalInfo(name, address, age)

        # use mutator methods to change information.
        name = input('Please enter the new name: ')
        info.set_name(name)

        # accessor methods get this information and display it individually.
        print(info.get_name())
        print(info.get_address())
        print(info.get_age())
        # or use string method on object to display all information at once.
        print(info)

--------------------------------------------------------------------------------------------
############################    EXAMPLE 2 - COIN EXAMPLE    ################################
--------------------------------------------------------------------------------------------
### See coin.py and coin_demo5.py for complete code and notes.
import random
class Coin:    
    def __init__(self): # initialize object
        self.__sideup = 'Heads'

    def toss(self): # mutator method
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    
    def get_sideup(self): # accessor method
        return self.__sideup

### coin_demo5.py file:
    import coin

    coin1 = coin.Coin() # initialize object.

    # Display the side of each coin that is facing up (accessor method).
    print('The coin is this sideup:')
    print(coin1.get_sideup())

    # Toss the coin (mutator method)
    coin1.toss()

    # Display side up (accessor method)
    print('The coin is now this sideup:')
    print(coin1.get_sideup())

    --------------------------------------------------------------------------------------------
    ## VIDEO TUTORIAL NOTES ##
    .self # argument needs to be added to every method under a class.

    #### SIMPLE EXAMPLE #### SEE CONSTRUCTOR FOR BEST PRACTICE ####
        class Robot:
            def introduce_self(self):
                print('My name is ' + self.name)
        
        ## Create object and attributes ##
        r1 = Robot()     # create object
        r1.name = 'Tom'    # assign attributes to that object
        r1.color = 'red'
        r1.weight = 30

        ## Call introduce self method from robot class
        r1.introduce_self() # prints 'My name is Tom'

    #### CONSTRUCTOR ####
    # this code does what the simple example above does, but it is best
    # practice to use a constructor to assign the attributes to the object
    # this prevents spelling errors etc.
        class Robot:
            def __init__(self, name, color, weight):
                self.name = name
                self.color = color
                self.weight = weight
            
            def introduce_self(self):
                print('My name is' + self.name)
        
        ## Create object and attributes ##
        r1 = Robot('Tom','red',30)
        
        ### CREATE A NEW CLASS FOR PERSON ###
            class Person:
                def __init__(self, name):
                    self.name = name
            
            p1 = Person('Tammy') # initialize object with attribute value
            
            # assign a new attribute called robot_owned to object
            p1.robot_owned = r1  # person 1 owns robot 1

            # access robot 1 method 
            p1.robot_owned.introduce_self()
                # this prints 'My name is Tom'