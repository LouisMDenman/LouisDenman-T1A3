#Import python packages.
import os.path

#Import external packages.
from colored import Fore, Back, Style

#Imported functions written for application in admin_functions.py.
from admin_functions import *

#Main menu function used for printing output and recieving user input that detirmines what feature to use.
def main():
    print(f"{Fore.rgb('53%', '12%', '47%')}\nHey, Welcome to Gallo 24 Car Garage! \n")
    print("Enter 1 to add, remove or view a booking.")
    print("Enter 2 to access information or learn more about different models of cars.")
    print("Enter 3 to guess a car.")
    print("Enter 4 to exit the garage.\n")

    user_input = input(f":{Style.reset} ")
    return user_input

#Sub menu function for the booking feature, responsible for printing output and recieving user input to detirmine if the user wants to add, remove, view booking/(s), or return to the main menu.
def booking_feature():
        print(f"{Fore.rgb('0%', '100%', '100%')}\nEnter 1 to add a booking.")
        print("Enter 2 to remove a booking.")
        print("Enter 3 to view bookings.")
        print(f"Enter 4 to cancel.\n")

        user_input = input(f":{Style.reset} ")
        return user_input

#Sub menu function for the car information feature, responsible for printing output and recieving user input to detirmine if the user wants to see information on all available cars, a specific car, a random car, or return to the main menu.
def carinfo_feature():
        print(f"{Fore.rgb('56%', '93%', '56%')}\nEnter 1 to see information on all cars in our database.")
        print("Enter 2 to see information on a specfic car.")
        print("Enter 3 to see information on a random car.")
        print("Enter 4 to cancel.\n")

        user_input = input(f":{Style.reset} ")
        return user_input

#Sub menu function for the car guesser feature, responsible for printing output and recieving user input to detirmine if the user wants to play the guessing game, or return to the main menu.
def carguess_feature():
        print(f"{Fore.rgb('100%', '84%', '0%')}\nEnter 1 to guess a random car selected from out database. You will get increasing hints with more guesses, and if you would like to exit or cannot guess the vehicle once in the game, type quit.")
        print("Enter 2 to return to main menu.\n")

        user_input = input(f":{Style.reset} ")
        return user_input

#A simple function that is called when misinput is entered at both the main menu and sub menu levels, and informs the users that they must enter an option displayed above in the relevant menu.
def wrong_input():
    print(f"{Fore.red}\nPlease enter one of the options shown above.{Style.reset}")

#Assign the names of the required csv files for the application to global variables, so that they can be used to check if those file names exist in the directory and write them if they are not.
cardatabase = 'cardatabase.csv'
bookings = 'bookings.csv'

#Function that creates a new csv file called 'bookings.csv' which is a required file for the application to run.
def write_bookings_csv():
    file = open(bookings, 'w')
    file.write("LastName,FirstName,Date,CarBrand,CarModel,Service\n")
    file.close()

#Function that creates a new csv file called 'cardatabase.csv' which is a required file for the application to run.
def write_cardatabase_csv():
    file = open(cardatabase, 'w')
    file.write("CarBrand,CarModel,BodyType,0To60,Cylinders,Aspirated,Horsepower,TopSpeed\nSubaru,BRZ,coupe,7.5,4,naturally aspirated,228,220")
    file.close()

#Checks if the 'bookings.csv' file exists within the directory, which is a required file for the application to run all the booking features, and calls on the write_bookings_csv() function if it cannot find the file.
if (not os.path.isfile(bookings)):
    write_bookings_csv()

#Checks if the 'cardatabase.csv' file exists within the directory, which is a required file for the application to run all the car information and guesser features, and calls on the write_cardatabase_csv() function if it cannot find the file.
if (not os.path.isfile(cardatabase)):
    write_cardatabase_csv()

#Initialises the service variable, which is then given the main() functions input which is entered by the user to control what they would like to do. Once the user selects a service, the same process occurs in a nested loop for each feature, with the feature variable being established and used to detirmine what the user would like to do in any given sub loop.
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
                wrong_input()
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
                wrong_input()
    elif service == '3':
        feature = ''
        while feature != '2':
            feature = carguess_feature()

            if feature == '1':
                car_guess(cardatabase)
            elif feature == '2':
                pass
            else:
                wrong_input()
    elif service == '4':
        pass
    else:
        wrong_input()

#Print a polite goodbye message when the user chooses to terminal the application.
print(f"{Fore.red}\nThanks for visiting the Gallo 24 Car Garage, until next time!{Style.reset}")