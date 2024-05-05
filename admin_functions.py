#Import python packages.
import csv
from random import randint
from datetime import date

#Import external packages.
from colored import Fore, Back, Style

#Establish a global variable for what the current date is to be used by other functions.
today = date.today()

def bookingcsv_error():
    """Function that is called when the user tries to make use of a function that utilises the 'bookings.csv' file when it has been deleted or isn't present. This shouldn't happen as main.py writes a new file under that name when the application is first run to avoid this issue, but this function provides a relevant error message just in case it does happen."""
    print(f"{Fore.red}Booking csv file doesn't exist.{Style.reset}")

def cardatabasecsv_error():
    """Function that is called when the user tries to make use of a function that utilises the 'cardatabase.csv' file when it has been deleted or isn't present. This shouldn't happen as main.py writes a new file under that name when the application is first run to avoid this issue, but this function provides a relevant error message just in case it does happen."""
    print(f"{Fore.red}Car database csv file doesn't exist.{Style.reset}")

def general_error():
    """Function that is called when the user creates an unexpected error that hasn't been accounted for. This shouldn't happen as code in both main.py and admin_functions.py implements thorough control structues and control flow, but in the chance that it does occur, this function provides a general error message to keep the programming from crashing."""
    print(f"{Fore.red}Apologies, something went wrong.{Style.reset}")

def exit_game():
    """Function that is called when a user chooses to end the game in the car guesser feature, and provides a message acknowledging that they have left the game."""
    print(f"{Fore.red}\nYou have exited the game, see you next time.{Style.reset}")

def add_booking(bookings):
    """The add_booking() function is responsible for handling adding a booking to the 'bookings.csv' file, and is called in the bookings sub loop of the main menu by selecting the add booking feature. This function first takes input and stores multiple local variables as the details required in the 'bookings.csv' file. Whilst doing so, when retrieving the desired date for a booking, the date is compared with the global variable 'today' that stores the current date, and uses a while loop to make sure that the entered date is in the future or today, not the past. The function then opens the 'bookings.csv' file in append mode, and writes the values stored in the local variables to a new line at the bottom of the file. The function then thanks the user and acknowledges that their booking has been saved 'in the system.'"""
    try:
        FirstName = input(f"{Fore.rgb('0%', '100%', '100%')}Please enter your first name:{Style.reset} ").capitalize()
        LastName = input(f"{Fore.rgb('0%', '100%', '100%')}Please enter your last name:{Style.reset} ").capitalize()
        Date = input(f"{Fore.rgb('0%', '100%', '100%')}Please enter the date you would like to book (format: YYYY-MM-DD):{Style.reset} ")
        while str(today) > Date:
            Date = input(f"{Fore.red}Please enter a date in the future (format: YYYY-MM-DD):{Style.reset} ")
        CarBrand = input(f"{Fore.rgb('0%', '100%', '100%')}Please enter the brand of your car:{Style.reset} ").capitalize()
        CarModel = input(f"{Fore.rgb('0%', '100%', '100%')}Please enter the model of your car:{Style.reset} ").capitalize()
        Service = input(f"{Fore.rgb('0%', '100%', '100%')}Do you require a service, upgrade or repair?{Style.reset} ").capitalize()
        with open(bookings, "a") as f:
            write = csv.writer(f)
            write.writerow([LastName,FirstName,Date,CarBrand,CarModel,Service])
        print(f"{Fore.rgb('0%', '100%', '100%')}\nThank you, your booking is sorted, see you then!{Style.reset}")
    except FileNotFoundError:
        bookingcsv_error()
    except:
        general_error()

def remove_booking(bookings):
    """The remove_booking() function is responsible for handling removing a booking from the 'bookings.csv' file, and is called in the bookings sub loop of the main menu by selecting the remove booking feature. This function first takes input and stores multiple local variables as the details of the booking that the user wants to delete in the 'bookings.csv' file. Whilst doing so, when retrieving the date of the booking being deleted, the date is compared with the global variable 'today' that stores the current date, and uses a while loop to make sure that the entered date is in the future or today, not the past. Following this, the function establishes a local temporary list variable called temp_list as well as a has_booking variable with value False. The function then copies all lines of 'bookings.csv' to temp_list, unless there is a line that matches all of the inputs of the users desired appointment to delete. If this occurs, the for loop at this point simply changes has_booking to True, and moves on hence not copying that line to the temp_list. Once the for loop has finished, if the has_booking variable is True, then the temp_list is written back into the 'bookings.csv' file which does not contain the 'deleted' line, whereas if the has_booking variable was never set to True, the function warns the user that the details they provided did not match any bookings within the 'system.'"""
    try:
        Fname = input(f"{Fore.rgb('0%', '100%', '100%')}\nEnter your first name to select your bookings:{Style.reset} ").capitalize()
        Lname = input(f"{Fore.rgb('0%', '100%', '100%')}Enter your last name to select your bookings:{Style.reset} ").capitalize()
        Date = input(f"{Fore.rgb('0%', '100%', '100%')}What was the date of the booking you would like to cancel? (format: YYYY-MM-DD):{Style.reset} ")
        while str(today) > Date:
            Date = input(f"{Fore.red}Please enter a date in the future (format: YYYY-MM-DD):{Style.reset} ")
        CarBrand = input(f"{Fore.rgb('0%', '100%', '100%')}What was the brand of car for this booking:{Style.reset} ").capitalize()
        Service = input(f"{Fore.rgb('0%', '100%', '100%')}Finally, was this booking a service, upgrade or repair?{Style.reset} ").capitalize()
        temp_list = []
        has_booking = False
        with open(bookings, "r") as f:
            read = csv.reader(f)
            for row in read:
                if (row[1] == Fname) and (row[0] == Lname) and (row[2] == Date) and (row[3] == CarBrand) and (row[5] == Service):
                    has_booking = True
                else:
                    temp_list.append(row)
        if has_booking:
            with open(bookings, "w") as f:
                write = csv.writer(f)
                write.writerows(temp_list)
            print(f"{Fore.rgb('0%', '100%', '100%')}\nThank you, your booking is cancelled, until next time!{Style.reset}")
        else:
            print(f"{Fore.red}\nSorry, we couldn't find a booking under these details. Perhaps a spelling or format error was made, feel free to try again.{Style.reset}")
    except FileNotFoundError:
        bookingcsv_error()
    except:
        general_error()

def view_booking(bookings):
    """The view_booking() function is responsible for handling displaying all of a users booking to them from the 'bookings.csv' file, and is called in the bookings sub loop of the main menu by selecting the view booking feature. This function first takes input in the form of the users first name and list name, so that these details may be used to check if a booking belongs to that person or not. The function then reads 'bookings.csv' and utilises a for loop with an if statement to go through each line of the file, and print the line if the first name and last name of the booking matches the user input. The variable has_booking is once again locally utlisied and is turned from False to true if there is a booking with a matching name, otherwise if this variable is False at the end of the file it prints a polite message letting the user know that there are no bookings matching their inputted name."""
    try:
        Fname = input(f"{Fore.rgb('0%', '100%', '100%')}\nEnter your first name to see your booked services:{Style.reset} ").capitalize()
        Lname = input(f"{Fore.rgb('0%', '100%', '100%')}Enter your last name to see your booked services:{Style.reset} ").capitalize()
        has_booking = False
        with open(bookings, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                if row[0] == Lname and row[1] == Fname:
                    print(f"{Fore.rgb('0%', '100%', '100%')}\n{row[1]} {row[0]}'s {row[3]} {row[4]} is booked in for {row[5]} on the {row[2]}{Style.reset}")    
                    has_booking = True
            if has_booking == False:
                print(f"{Fore.red}\nWe have no bookings under this name.{Style.reset}")
    except FileNotFoundError:
        bookingcsv_error()
    except:
        general_error()

def all_car_information(cardatabase):
    """The all_car_information() function is responsible for displaying all cars and their information that are stored in the 'cardatabase.csv' file to the user, and is called in the car information sub loop of the main menu by selecting the see information about all cars feature. This function is passed the global variable cardatabase, which stores the name 'cardatabase.csv' and uses it to open the file in read mode. The function then loops through the file and prints each line, producing the pieces of data in a specfic format shown in the f string to make it sound formatted and informative."""
    try:
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                print(f"{Fore.rgb('56%', '93%', '56%')}\nThe {row[0]} {row[1].capitalize()} is a sport {row[2]} that accelerates from 0-100km/h in {row[3]} seconds, powered by a {row[4]} cylinder {row[5]} engine, which produces {row[6]} horsepower and gives the car a top speed of {row[7]}km/h.{Style.reset}")    
    except FileNotFoundError:
        cardatabasecsv_error()
    except:
        general_error()

def specific_car_information(cardatabase):
    """The spcefic_car_information() function is responsible for displaying a specific car and its information that is stored in the 'cardatabase.csv' file to the user, and is called in the car information sub loop of the main menu by selecting the see information about a specfic car feature. This function is passed the global variable cardatabase, which stores the name 'cardatabase.csv' and uses it to open the file in read mode. The function then loops through the file and prints a line only if the name of the brand and model of the car match the users input, wich produces the pieces of data in a specfic format shown in the f string to make it sound formatted and informative."""
    try:
        CarBrand = input(f"{Fore.rgb('56%', '93%', '56%')}\nEnter the brand of car you would like to know more about:{Style.reset} ").capitalize()
        CarModel = input(f"{Fore.rgb('56%', '93%', '56%')}\nEnter the model of car you would like to know more about:{Style.reset} ").upper()
        has_vehicle = False
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                if row[0] == CarBrand and row[1] == CarModel:
                    print(f"{Fore.rgb('56%', '93%', '56%')}\nThe {row[0]} {row[1].capitalize()} is a sport {row[2]} that accelerates from 0-100km/h in {row[3]} seconds, powered by a {row[4]} cylinder {row[5]} engine, which produces {row[6]} horsepower and gives the car a top speed of {row[7]}km/h.{Style.reset}")  
                    has_vehicle = True
            if has_vehicle == False:
                print(f"{Fore.red}\nWe have no cars in our database under this name.{Style.reset}")
    except FileNotFoundError:
        cardatabasecsv_error()
    except:
        general_error()

def random_car_information(cardatabase):
    """The random_car_information() function is responsible for displaying a random car and its information that is stored in the 'cardatabase.csv' file to the user, and is called in the car information sub loop of the main menu by selecting the see information about a random car feature. This function is passed the global variable cardatabase, which stores the name 'cardatabase.csv' and uses it to open the file in read mode. The function then loops through the file and copies all the lines of the file to a local variable called temp_list. A variable randnum is then established using the randint function which was imported from the random package, by taking the range between 0 and the length of the temp_list - 1 (to account for index starting at 0) and letting randint select a random number. The function then uses this random number as the index of temp_list to display, and uses the information about the car within that index to display information about the car in the informative f string."""
    try:
        temp_list = []
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                temp_list.append(row)
        randnum = randint(0,len(temp_list)-1)
        print(f"{Fore.rgb('56%', '93%', '56%')}\nThe {temp_list[randnum][0]} {temp_list[randnum][1].capitalize()} is a sport {temp_list[randnum][2]} that accelerates from 0-100km/h in {temp_list[randnum][3]} seconds, powered by a {temp_list[randnum][4]} cylinder {temp_list[randnum][5]} engine, which produces {temp_list[randnum][6]} horsepower and gives the car a top speed of {temp_list[randnum][7]}km/h.{Style.reset}")
    except FileNotFoundError:
        cardatabasecsv_error()
    except:
        general_error()

def car_guess(cardatabase):
    """The car_guess() function is responsible for displaying limited output in a game style format relating to a specfic car, and having the user try to guess the make and model of vehicle based off of the information provided. To begin, like the random_car_information() function, car_guess() copies the current 'cardatabase.csv' in read mode to a temp_list variable, and creates a randnum in the valid index range using randint from the random module. Following this, a guess variable is established as the input variable and initialised with '', as well as a count variable initialised with 0. At this point, the function imediately checks if the length of the temp_list is greater than 1, because if this is not the case it means main.py() wrote 'cardatabase.csv' at the start of the application and there is only 1 car to guess. If this else case is triggered, the program explains that the 'database' is not fully available, and we only have information on the 1 car and displays it, apologising and suggesting that it will be playable when there are more cars in the 'database.' It then also changes the value of guess to 'QUIT' so that the winners message is not played at the bottom of the function. If the temp_list length is greater than 1, the function immediately goes into a while loop that will only break when the users guess is correct. The while loop contains a long if statement that begins when count == 0, which is when the program begins, and gives the intial hint. The next elif statement will be count < 5, so that the clue is not printed every time, and just says 'try again: '. if count == 5, the clue is repeated but with slightly more detail and is followed by 'try again: ' while count < 10, which continues until count == 20. At this point, all of the clues have been given, and there is only an else statement repeating 'try again: '. Within all of these if,elif,else statements there is also a nested if statement that checks if guess == 'QUIT' which calls the exit_game() function and then utilises break to exit the while loop. At the bottom of the function as mentioned before, there is a function that check if guess != 'QUIT', and is triggered if the user did play the game and didn't quit, displaying a congratulations message that shows the correctly guessed car and the amount of guesses it took."""
    try:
        temp_list = []
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                temp_list.append(row)
        randcar = randint(0,len(temp_list)-1)
        guess = ''
        count = 0
        if len(temp_list) > 1:
            while guess != (f"{temp_list[randcar][0].upper()} {temp_list[randcar][1].upper()}"):
                if count == 0:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds.{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count < 5:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}Try again:{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count == 5:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine.{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count < 10:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}Try again:{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count == 10:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine, which produces {temp_list[randcar][6]} horsepower and gives the car a top speed of {temp_list[randcar][7]}km/h.{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count < 15:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}Try again:{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count == 15:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine, which produces {temp_list[randcar][6]} horsepower and gives the car a top speed of {temp_list[randcar][7]}km/h. It is a {temp_list[randcar][2]}.{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count < 20:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}Try again:{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                elif count == 20:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine, which produces {temp_list[randcar][6]} horsepower and gives the car a top speed of {temp_list[randcar][7]}km/h. It is a {temp_list[randcar][2]} made by {temp_list[randcar][0]}.{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
                else:
                    guess = input(f"{Fore.rgb('100%', '84%', '0%')}Try again:{Style.reset} ")
                    guess = guess.upper()
                    if guess == "QUIT":
                        exit_game()
                        break
                    count += 1
        else:
            print(f"{Fore.red}\nSorry, it looks like most of our database is unavailable for some reason. The only car we have information on right now is the {temp_list[0][0]} {temp_list[0][1].capitalize()}, a sport {temp_list[0][2]} that accelerates from 0-100km/h in {temp_list[0][3]} seconds, powered by a {temp_list[0][4]} cylinder {temp_list[0][5]} engine, which produces {temp_list[0][6]} horsepower and gives the car a top speed of {temp_list[0][7]}km/h. It wouldn't be fun guessing the same car over and over again, so when we update the database you can guess between many cars!{Style.reset}")
            guess = 'QUIT'
        if guess != 'QUIT':
            guess = print(f"{Fore.rgb('100%', '84%', '0%')}\nGreat work! you correctly guessed the {temp_list[randcar][0]} {temp_list[randcar][1].capitalize()} in {count} guesses.{Style.reset}")
    except FileNotFoundError:
        cardatabasecsv_error()
    except:
        general_error()
