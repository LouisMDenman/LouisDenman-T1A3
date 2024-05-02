#Import python packages
import os.path

#Import external packages 
from colored import Fore, Back, Style

#Imported functions written for application
from admin_functions import *

#Main function loop
def main():
    print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.rgb('53%', '12%', '47%')}\nHey, Welcome to Gallo 24 Car Garage! \n")
    print("Enter 1 to add, remove or view a booking.")
    print("Enter 2 to access information or learn more about different models of cars.")
    print("Enter 3 to guess a car.")
    print("Enter 4 to exit the garage.\n")

    user_input = input(f":{Style.reset} ")
    return user_input

#Booking function loop
def booking_feature():
        print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.rgb('0%', '100%', '100%')}\nEnter 1 to add a booking.")
        print("Enter 2 to remove a booking.")
        print("Enter 3 to view bookings.")
        print(f"Enter 4 to cancel.\n")

        user_input = input(f":{Style.reset} ")
        return user_input

#Car information loop
def carinfo_feature():
        print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.rgb('56%', '93%', '56%')}\nEnter 1 to see information on all cars in our database.")
        print("Enter 2 to see information on a specfic car.")
        print("Enter 3 to see information on a random car.")
        print("Enter 4 to cancel.\n")

        user_input = input(f":{Style.reset} ")
        return user_input

#Car guesser loop
def carguess_feature():
        print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.rgb('100%', '84%', '0%')}\nEnter 1 to guess a random car selected from out database. You will get increasing hints with more guesses, and if you would like to exit or cannot guess the vehicle once in the game, type quit.")
        print("Enter 2 to return to main menu.\n")

        user_input = input(f":{Style.reset} ")
        return user_input

#assign variables required csv names
cardatabase = 'cardatabase.csv'
bookings = 'bookings.csv'

#write bookings csv function
def write_bookings_csv():
    file = open(bookings, 'w')
    file.write("LastName,FirstName,Date,CarBrand,CarModel,Service\n")
    file.close()

#write car database csv function
def write_cardatabase_csv():
    file = open(cardatabase, 'w')
    file.write("CarBrand,CarModel,BodyType,0To60,Cylinders,Aspirated,Horsepower,TopSpeed\nSubaru,BRZ,coupe,7.5,4,naturally aspirated,228,220")
    file.close()

#Check if booking csv doesn't exist and writes a file if that is the case
if (not os.path.isfile(bookings)):
    write_bookings_csv()

#Check if car database csv doesn't exist and writes a file if that is the case
if (not os.path.isfile(cardatabase)):
    write_cardatabase_csv()

#initialise the service variable and commence the main menu loop
service = ''
while service != '4':
    service = main()
    if service == '1':
        feature = ''
        while feature != '4':
            feature = booking_feature()

            if feature == '1':
                add_booking(bookings)
            elif feature == '2':
                remove_booking(bookings)
            elif feature == '3':
                view_booking(bookings)
            elif feature == '4':
                pass
            else:
                print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.red}\nPlease enter one of the options shown above.{Style.reset}")
    elif service == '2':
        feature = ''
        while feature != '4':
            feature = carinfo_feature()

            if feature == '1':
                all_car_information(cardatabase)
            elif feature == '2':
                specific_car_information(cardatabase)
            elif feature == '3':
                random_car_information(cardatabase)
            elif feature == '4':
                pass
            else:
                print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.red}\nPlease enter one of the options shown above.{Style.reset}")
    elif service == '3':
        feature = ''
        while feature != '2':
            feature = carguess_feature()

            if feature == '1':
                car_guess(cardatabase)
            elif feature == '2':
                pass
            else:
                print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.red}\nPlease enter one of the options shown above.{Style.reset}")
    elif service == '4':
        pass
    else:
        print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.red}\nPlease enter one of the options shown above.{Style.reset}")

#Print a goodbye message
print(f"{Fore.rgb('82.7%', '82.7%', '82.7%')}{Back.red}\nThanks for visiting the Gallo 24 Car Garage, until next time!{Style.reset}")