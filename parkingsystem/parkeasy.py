import pickle
from os import system
from sys import exit as shut
from fare import *


def clear_screen(c=1):
    # input("\nPress any key to continue\n")
    if c:
        system('cls')


def menu(file=None):
    if file is None:
        try:
            with open('state.pl', 'rb') as f:
                file = [pickle.load(f)]
        except:
            file = []
    print("""
    1. ENTRY                     
    2. EXIT                      
    3. SEARCH          
    4. CHANGE FARE                          
    5. EXIT   
    6. UNDO           

    """)
    try:
        opt = int(input(">>>"))
    except (SyntaxError, NameError):
        system('cls')
        menu()
    else:
        clear_screen()
        if opt == 1:
            name = mandatory_field(input("{:12}:{:4}".format("NAME", " ")))
            phone = mandatory_field(input("{:12}:{:4}".format("PHONE", " ")))
            while len(phone) != 9 or not phone.isdigit():
                phone = invalid(phone)
            type = mandatory_field(input("{:12}:{:4}".format("type", " ")))
            id = mandatory_field(input("{:12}:{:4}".format("PLATE NUMBER", " ")))
            while len(id) != 4 or not id.isdigit():
                id = invalid(id)
            file.append(pl.entry(name=name, phone=phone, type=type, id=id))
            clear_screen()
            menu(file)
        elif opt == 2:
            if pl.get_occupancy() == 0:
                print("Lot is empty!")
            else:
                id = input("Enter license plate no. vehicle\n")
                temp = pl.exit(id=id)

                file.append(temp)
            clear_screen()
            menu(file)
        elif opt == 3:
            if pl.get_occupancy() == 0:
                print("Lot is empty!")
            else:
                z = pl.search(input("Enter license plate no. of vehicle\n"))
                if z is not None:
                    print(z)
                else:
                    print("Vehicle not found!")
            clear_screen()
            menu(file)
        elif opt == 4:
            fare = input("Enter the fare you want to set for the parking lot: ")
            while not isinstance(fare, int):
                print("Please enter an integer.")
                fare = input("Enter the fare you want to set for the parking lot: ")
            pl.setFare(fare)
            clear_screen()
            menu(file)
        elif opt == 5:
            clear_screen()
            with open('state.pl', 'wb') as f:
                pickle.dump(file[-1], f)
            shut()
        elif opt == 6:
            pl.undo(file)
            file = file[:len(file)-1]
            clear_screen()
            menu(file)
        else:
            print("WRONG OPTION")
            clear_screen()
            menu(file)


def mandatory_field(x):
    if x.isspace() or len(x) == 0:
        print("\nField cannot be empty!")
        x = mandatory_field(input("Enter again:"))
    return x


def invalid(attr):
    print("\nInvalid!")
    attr = mandatory_field(input("Enter again:"))
    return attr


# ------------------------------------MAIN----------------------------------
if __name__ == '__main__':
    clear_screen(1)
    pl = ParkingLot()
    fare = int(input("Enter the fare you want to set for the parking lot: "))
    while not isinstance(fare, int):
        print("Please enter an integer.")
        fare = input("Enter the fare you want to set for the parking lot: ")
    pl.setFare(fare)
    clear_screen()
    menu()
