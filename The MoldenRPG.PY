import os

def What_With_Bag():
    c3 = input(WHITE + "1. Check Bag \n2. Equip bag ")
    if c3 == "1":
        input(CYAN + "you have a 100 dollar note ")
        os.system('cls')
        Starting_Select()

    if c3 == "2":
        input(CYAN + "You wore your bag ")
        os.system('cls')
        Starting_Select()

def What_With_Vending_Machine():
    c2 = input(WHITE + "1. Get a Pepsi \n2. Get a water bottle \n3. Kick the Vending Machine \n4. Leave ")
    if c2 == "1":
        input(CYAN + "You get a Pepsi ")
        os.system('cls')
        Starting_Select()

    if c2 == "2":
        input(CYAN + "You got a water bottle ")
        os.system('cls')
        Starting_Select()

    if c2 == "3":
        input(CYAN + "You kicked the Vending Machine and got a free Coke ")
        os.system('cls')
        Starting_Select()

    if c2 == "4":
        os.system('cls')
        Starting_Select()


    

def Starting_Select():
    c1 = input(WHITE + "What do you want to interact with \n1. Vending Machine \n2. Bag ")
    if c1 == "1":
        What_With_Vending_Machine()
    
    if c1 == "2":
        What_With_Bag()


CYAN    = '\033[36m'
WHITE   = '\033[37m'

input(CYAN + "Welcome to the MoldenRPG ")
input(CYAN + "are you ready? ")
input(CYAN + "I hope so.. here we go! ")
os.system('cls')
Starting_Select()


