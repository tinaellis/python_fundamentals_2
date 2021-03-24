import compositionrobot

def main():

    print('What do you want your robot to do for you today? ')
    clean = input('What do you want the robot to clean? ')
    babysit = input('Who do you want the robot to babysit? ')
    cook = input('What do you want the robot to cook? ')
    account = input('Which account do you need the robot to balance? ')
    teach = input('What do you need your robot to teach? ')
    letter = input('Who do you need to write a letter to? ')
    
    robot1 = compositionrobot.Superbot(clean, babysit, cook, account, teach, letter)

    
    print('\nYour super robot is happy to help you with these tasks!')
    print('Today your robot will...')
    print('1) Clean', robot1.clean())
    print('2) Cook', robot1.cook(), 'for you and', robot1.babysit())
    print('3) Balance the', robot1.account(), 'account')
    print('4) Teach you', robot1.teach())
    print('5) Write a letter to', robot1.letter())
    print('6) All while babysitting', robot1.babysit())
    

main()