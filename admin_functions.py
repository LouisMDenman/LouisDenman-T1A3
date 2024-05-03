#Import python packages
import csv
from random import randint
from datetime import date

#Import external packages 
from colored import Fore, Back, Style

#establish a variable for what the date is
today = date.today()

#booking csv error message function
def bookingcsv_error():
    print(f"{Fore.red}Booking csv file doesn't exist.{Style.reset}")

#car database csv error message function
def cardatabasecsv_error():
    print(f"{Fore.red}Car database csv file doesn't exist.{Style.reset}")

#general issues error message function
def general_error():
    print(f"{Fore.red}Apologies, something went wrong.{Style.reset}")

#exited the game msg
def exit_game():
    print(f"{Fore.red}\nYou have exited the game, see you next time.{Style.reset}")

#bookings
def add_booking(bookings):
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

#information
def all_car_information(cardatabase):
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

#car guesser
def car_guess(cardatabase):
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
