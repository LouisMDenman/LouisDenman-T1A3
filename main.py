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
    print("Enter 3 to access the build configurator.")
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

#Car information loop
def carinfo_feature():
        print("\nEnter 1 to get information about all cars in the database.")
        print("Enter 2 to get information about a specific car.")
        print("Enter 3 to get information about a random car.")
        print("Enter 4 to cancel.\n")

        user_input = input(": ")
        return user_input

#Car configurator loop
def buildconfig_feature():
        print("\nEnter 1 to see parts in stock for a specific car.")
        print("Enter 2 to start a new configuration.")
        print("Enter 3 to modify an existing configuration.")
        print("Enter 4 to cancel.\n")

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
        while feature != '4':
            feature = buildconfig_feature()

            if feature == '1':
                parts_in_stock()
            elif feature == '2':
                new_configuration()
            elif feature == '3':
                existing_configuration()
            elif feature == '4':
                pass
            else:
                print("\nPlease enter one of the options shown above.")
    elif service == '4':
        pass
    else:
        print("\nPlease enter one of the options shown above.")

#Print a goodbye message
print("\nThanks for visiting the Gallo 24 Car Garage, until next time!")