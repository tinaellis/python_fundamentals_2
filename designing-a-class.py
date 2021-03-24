### Techniques for Designing Classes ###

### UNIFIED MODELING LANGUAGE UML ###
    # UML DIAGRAM
        # TOP: Name of class
        # MIDDLE: List of class's attributes
        # BOTTOM: List of class's methods

### FINDING THE CLASSES IN A PROBLEM ###
    # 1) Get a written description of problem domain
    # 2) Identify the nouns
    # 3) Refine list to only classes relavant to the problem

### IDENTIFYING A CLASS'S RESPONSIBILITY ###
# attributes: The things the class is responsible for knowing
# methods: The things the class is responsible for doing

# Example, Customer class:
    # what must the class know (attributes):
        # customer name
        # customer address
        # customer phone

    # what must the class do (methods):
        # initialize an object
        # set and return name
        # set and return address
        # set and return phone

    # UML DIAGRAM:
    ------------------------------
            Customer                # class name
    ------------------------------
    __name
    __address
    __phone                         # class attributes
    ------------------------------
    __init__(name, address, phone)
    set_name(name)
    set_address(address)
    set_phone(phone)
    get_name(name)
    get_address(address)
    get_phone(phone)                # class methods
    ------------------------------

# Customer class program.
class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone