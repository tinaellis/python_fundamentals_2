# YouTube tutorials
# Python Object Inheritance
# "Has a" vs "is a" 
# Object composition vs inheritance
# * Note we will need to demonstrate how to properly relate objects
# Superclass sometimes call parent class
--------------------------------------------------------------------------------------------
############################## EXAMPLE - INHERITANCE ###############################
--------------------------------------------------------------------------------------------
# class file accounts.py
    class SavingsAccount:
        def __init__(self, account_num):
            self.__account_num = account_num
        def set_account_num(self, account_num): # mutator
            self.__account_num = account_num
        def get_account_num(self): # accessor
            return self.__account_num
    
    class CD(SavingsAccount): # subclass of SavingsAccount
        def __init__(self, account_num, mat_date):
            SavingsAccount.__init__(self, account_num) # Call superclass __init__ method.
            self.__maturity_date = mat_date # Initialize the __maturity_date attribute
        def set_maturity_date(self, mat_date): # mutator
            self.__maturity_date = mat_date
        def get_maturity_date(self): # accessor
            return self.__maturity_date

# program file account_demo.py
    import accounts
    acct_num = input('Account number: ') 
    savings = accounts.SavingsAccount(acct_num) # Create a SavingsAccount object.
    acct_num = input('Account number: ')
    maturity = input('Maturity date: ')
    cd = accounts.CD(acct_num, maturity) # Create a CD object.

     # SavingsAccount account number
    print('Account number:', savings.get_account_num())
    # CD account num and maturity date.
    print('Account number:', cd.get_account_num()) 
    print('Maturity date:', cd.get_maturity_date())

--------------------------------------------------------------------------------------------
############################## EXAMPLE - POLYMORPHISM ###############################
--------------------------------------------------------------------------------------------
# class file animals.py

    class Mammal:
        def __init__(self, species):
            self.__species = species
        def show_species(self):
            print('I am a', self.__species)
        def make_sound(self):
            print('Grrrrr')
    # dog class inherits species, show_species and make_sound
    class Dog(Mammal): 
        def __init__(self):
            Mammal.__init__(self, 'Dog') # overrides species with "Dog"
        def make_sound(self): # overrides make_sound
            print('Woof! Woof!')

# from program file polymorphism_demo.py
    import animals
    mammal = animals.Mammal('regular animal') # create mammal object
    dog = animals.Dog() # create dog object

    # call show_species and make_sound methods from superclass
    mammal.show_species() 
    mammal.make_sound()

    # call show_species and make_sound methods from subclass
    dog.show_species()
    dog.make_sound()
    ### OUTPUT ###
        # I am a regular animal
        # Grrrrr
        # I am a Dog
        # Woof! Woof!

###### isinstance and issubclass functions ######
    # Avoid AttributeError by determining if object is instance of class.
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a Mammal!')

    # OR
    print(isinstance(mgr_1, Manager)) # is object "mgr_1" an instance of "Manager" class?

    ###### issubclass function ######
        print(issubclass(Developer, Employee)) # is "Developer" a subclass of "Employee"?

--------------------------------------------------------------------------------------------
########################## Object Inheritance Tutorial Notes ############################
-------------------------------------------------------------------------------------------- 

### METHOD RESOLUTION ORDER ###
    # when python looks in subclass and doesn't find init method, it walks up the chain
    # of inheritance until it finds what its looking for. This chain is called the Method
    # Resolution Order.

### TO SEE INHERITANCE AND METHOD RESOLUTION ORDER ###
    # pass subclass through help function and python will display tons of info.
    print(help(Dog)) # dog is subclass name

    # Example of what you might see:
        # Method resolution order:
            # Dog - subclass python checks first
            # Mammal - superclass python checks next
            # builtins.object - and base class that all python objects inherit

### TWO WAYS OF CALLING PARENT INIT METHOD ###
    class CD(SavingsAccount): # FIRST
        def __init__(self, account_num, mat_date):
            SavingsAccount.__init__(self, account_num) 
            self.__maturity_date = mat_date 

    class CD(SavingsAccount): # SECOND
        def __init__(self, account_num, mat_date):
            super().__init__(account_num) # "super" class calls parent init method
            self.maturity_date = mat_date

    # using the super class with single inheritance keeps things a little more maintainable
    # but it's NESSECARY when you start using multiple inheritance.

--------------------------------------------------------------------------------------------
########################## INHERITANCE EXAMPLE 2 - FROM YOUTUBE ############################
-------------------------------------------------------------------------------------------- 
# from https://www.youtube.com/watch?v=RSl87lqOXDE
# full list of code examples: https://github.com/CoreyMSchafer/code_snippets/tree/master/Object-Oriented

    class Employee:
        raise_amt = 1.04
        
        def __init__(self,first,last,pay):
            self.first = first
            self.last = last
            self.email = first + '.' + last + '@email.com'
            self.pay = pay
        
        def fullname(self):
            return '{} {}'.format(self.first, self.last)

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)

    class Developer(Employee):
        raise_amt = 1.10

        def __init__(self, first, last, pay, prog_lang): 
            super().__init__(first, last, pay) 
            self.prog_lang = prog_lang

    ### PASSING THROUGH A LIST OF EMPLOYEES & SET DEFAULT TO NONE ###
    # Never pass mutable data types, such as lists or dictionary, as default arguments. This is why
    # we don't pass empty list as default argument in example below - and instead use boolean statement
    class Manager(Employee):
        def __init__(self, first, last, pay, employees=None): 
            super().__init__(first, last, pay) 
            if employees is None:
                self.employees = [] # create empty list
            else:
                self.employees = employees # set to employee list provided
        
        # add to list of employees that manager supervises
        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp) # append to list

        # remove employee from list
        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

        # print employees
        def print_emps(emps):
            for emp in self.employees:
                print('-->', emp.fullname())

# From program file:
    dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
    dev_2 = Developer('Test', 'Lastname', 60000, 'Python')

    mgr_1 = Manager('Sue','Smith', 90000, [dev_1])

    print(mgr_1.email) # comes from employee class
    mgr_1.print_emps() # prints fullname of the employee they manage

--------------------------------------------------------------------------------------------
####################################### COMPOSITION ########################################
-------------------------------------------------------------------------------------------- 
    #### "Inheritance" ("is-a") versus "Composition" ("has-a") ####
    # https://youtu.be/RiRrcCUyn4M

    "Composition is a design model where an object knows another object and explicitly delegates some tasks to it."
    # Inheritance: child class inherits all of the attributes and methods from the parent class.
    # Composition: you control what is inherited from the parent class.
        # Composition prevents the diamond problem from occurring.

    ### INHERITANCE - "is-a relationship" ### 
        class Animal():
            def eat(self):
                print('yum')

        class Dog(Animal):
            def bark(self):
                print('Woof')

        class Cat(Animal):
            def meow(self):
                print('Meow')
            
        snoopy = Dog()
        snoopy.bark()
        snoopy.eat()

    ### COMPOSITION - "has-a relationship" ###
    # make each skill a class and compose a new class by including objects 
    # from other classes.

        class Dog():
            def bark(self):
                print('Woof')
        class Robot():
            def move(self):
                print('Ahh mobility..')
        class CleanRobot():
            def clean(self):
                print('I vacuum dust')
        class CookRobot():
            def cook(self):
                print('I make homemade pasta')

        class Superbot():
            def __init__(self):
                # this class contains 3 objects.
                # Not using inheritance, we're using composition.
                self.o1 = Robot()
                self.o2 = Dog()
                self.o3 = CleanRobot()

            def playGame(self):
                print('Chess is best')
            
            # we still have to define these methods but we're calling them from the classes
            def move(self):
                return self.o1.move() 
            def bark(self):
                return self.o2.bark()
            def clean(self):
                return self.o3.clean()

        henry = Superbot()
        henry.move() # prints 'Ahh mobility'
        henry.bark() # prints 'Woof'
        henry.playGame() # prints 'chess is best'

        ### NOTES ###
        # Use composition when you can
        # Use inheritance when you must