# Class example of composition "has-a" relationship.
class Drycleaner:
    def __init__(self, clean):
        self.__clean = clean
        
    def get_clean(self):
        return self.__clean

class Babysitter:
    def __init__(self, babysit):
        self.__babysit = babysit
        
    def get_babysit(self):
        return self.__babysit
    
class Chef:
    def __init__(self, cook):
        self.__cook = cook
        
    def get_cook(self):
        return self.__cook
    
class Accountant:
    def __init__(self, account):
        self.__account = account
        
    def get_account(self):
        return self.__account
    
class Teacher:
    def __init__(self, teach):  
        self.__teach = teach
        
    def get_teach(self):
        return self.__teach
    
class Secretary:
    def __init__(self, letter):
        self.__letter = letter
        
    def get_letter(self):
        return self.__letter
    
class Superbot:
    # this class contains 6 objects.
    def __init__(self, clean, babysit, cook, account, teach, letter):
         # o1 is object name | Drycleaner is class | clean is argument
        self.o1 = Drycleaner(clean)
        self.o2 = Babysitter(babysit)
        self.o3 = Chef(cook)
        self.o4 = Accountant(account)
        self.o5 = Teacher(teach)
        self.o6 = Secretary(letter)
        
    # o1 is object name | get_clean() is method we want from Drycleaner class.
    def clean(self):
        return self.o1.get_clean()
    
    def babysit(self):
        return self.o2.get_babysit()
    
    def cook(self):
        return self.o3.get_cook()
    
    def account(self):
        return self.o4.get_account()
    
    def teach(self):
        return self.o5.get_teach()
    
    def letter(self):
        return self.o6.get_letter()
    
    # To use these objects, you create object with arguments, example:
        # obj2 = Superbot('clean: toilet','babysit: Jimbo', 'cook: pizza', 'bal: checkbook', 'Teach: French', 'Write: To president')
    # To call you would just call object methods under the Superbot class:
        # print(obj2.clean(), obj2.babysit(), obj2.cook(), obj2.account(), obj2.teach(), obj2.letter())
    
    
    
    
    

# obj2 = Superbot('clean: toilet','babysit: Jimbo', 'cook: pizza', 'bal: checkbook', 'Teach: French', 'Write: To president')
# print(obj2.clean(),obj2.babysit(),obj2.cook(),obj2.account(),obj2.teach(),obj2.letter())


    
    
    
    
    
    
    
    
    
    