#Import python packages
import os.path

#Import external packages 

#Imported functions written for application
from admin_functions import *

#Main function loop
def main():
    print("\nHey, Welcome to Gallo 24 Car Garage! \n")
    print("Enter 1 to add, remove or view a booking.")
    print("Enter 2 to access information or learn more about different models of cars.")
    print("Enter 3 to guess a car.")
    print("Enter 4 to exit the garage.\n")

    user_input = input(": ")
    return user_input

#Booking function loop
def booking_feature():
        print("\nEnter 1 to add a booking.")
        print("Enter 2 to remove a booking.")
        print("Enter 3 to view bookings.")
        print("Enter 4 to cancel.\n")

        user_input = input(": ")
        return user_input

#Car configurator loop
def carinfo_feature():
        print("\nEnter 1 to see information on all cars in our database.")
        print("Enter 2 to see information on a specfic car.")
        print("Enter 3 to see information on a random car.")
        print("Enter 4 to cancel.\n")

        user_input = input(": ")
        return user_input

#Car guesser loop
def carguess_feature():
        print("\nEnter 1 to guess a random car selected from out database. You will get increasing hints with more guesses, and if you would like to exit or cannot guess the vehicle once in the game, type quit.")
        print("Enter 2 to return to main menu.\n")

        user_input = input(": ")
        return user_input

#Create a booking csv if it does not already exist
bookings = 'bookings.csv'
if (not os.path.isfile(bookings)):
    file = open(bookings, 'w')
    file.write("LastName,FirstName,Date,CarBrand,CarModel,Service\n")
    file.close()

#assign car database csv to a variable
cardatabase = 'cardatabase.csv'

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
                print("\nPlease enter one of the options shown above.")
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
                print("\nPlease enter one of the options shown above.")
    elif service == '3':
        feature = ''
        while feature != '2':
            feature = carguess_feature()

            if feature == '1':
                car_guess(cardatabase)
            elif feature == '2':
                pass
            else:
                print("\nPlease enter one of the options shown above.")
    elif service == '4':
        pass
    else:
        print("\nPlease enter one of the options shown above.")

#Print a goodbye message
print("\nThanks for visiting the Gallo 24 Car Garage, until next time!")