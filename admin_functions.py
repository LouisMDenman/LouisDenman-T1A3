#Import python packages
import csv
from random import randint

#bookings
def add_booking(bookings):
    try:
        FirstName = input("Please enter your first name: ").capitalize()
        LastName = input("Please enter your last name: ").capitalize()
        Date = input("Please enter the date you would like to book (format: YYYY-MM-DD): ")
        CarBrand = input("Please enter the brand of your car: ").capitalize()
        CarModel = input("Please enter the model of your car: ").capitalize()
        Service = input("Do you require a service, upgrade or repair? ").capitalize()
        with open(bookings, "a") as f:
            write = csv.writer(f)
            write.writerow([LastName,FirstName,Date,CarBrand,CarModel,Service])
        print("\nThank you, your booking is sorted, see you then!")
    except FileNotFoundError:
        print("Booking csv file doesn't exist.")

def remove_booking(bookings):
    try:
        Fname = input("\nEnter your first name to select your bookings: ").capitalize()
        Lname = input("Enter your last name to select your bookings: ").capitalize()
        Date = input("What was the date of the booking you would like to cancel? (format: YYYY-MM-DD): ")
        CarBrand = input("What was the brand of car for this booking: ").capitalize()
        Service = input("Finally, was this booking a service, upgrade or repair? ").capitalize()
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
            print("\nThank you, your booking is cancelled, until next time!")
        else:
            print("\nSorry, we couldn't find a booking under these details. Perhaps a spelling or format error was made, feel free to try again.")
    except FileNotFoundError:
        print("Booking csv file doesn't exist.")

def view_booking(bookings):
    try:
        Fname = input("\nEnter your first name to see your booked services: ").capitalize()
        Lname = input("Enter your last name to see your booked services: ").capitalize()
        has_booking = False
        with open(bookings, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                if row[0] == Lname and row[1] == Fname:
                    print(f"\n{row[1]} {row[0]}'s {row[3]} {row[4]} is booked in for {row[5]} on the {row[2]}")    
                    has_booking = True
            if has_booking == False:
                print("\nWe have no bookings under this name.")
    except FileNotFoundError:
        print("Booking csv file doesn't exist.")

#information
def all_car_information(cardatabase):
    try:
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                print(f"\nThe {row[0]} {row[1].capitalize()} is a sport {row[2]} that accelerates from 0-100km/h in {row[3]} seconds, powered by a {row[4]} cylinder {row[5]} engine, which produces {row[6]} horsepower and gives the car a top speed of {row[7]}km/h.")    
    except FileNotFoundError:
        print("Car database csv file doesn't exist.")

def specific_car_information(cardatabase):
    try:
        CarBrand = input("\nEnter the brand of car you would like to know more about: ").capitalize()
        CarModel = input("\nEnter the model of car you would like to know more about: ").upper()
        has_vehicle = False
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                if row[0] == CarBrand and row[1] == CarModel:
                    print(f"\nThe {row[0]} {row[1].capitalize()} is a sport {row[2]} that accelerates from 0-100km/h in {row[3]} seconds, powered by a {row[4]} cylinder {row[5]} engine, which produces {row[6]} horsepower and gives the car a top speed of {row[7]}km/h.")  
                    has_vehicle = True
            if has_vehicle == False:
                print("\nWe have no cars in our database under this name.")
    except FileNotFoundError:
        print("Car database csv file doesn't exist.")

def random_car_information(cardatabase):
    try:
        temp_list = []
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                temp_list.append(row)
        randnum = randint(0,len(temp_list)-1)
        print(f"\nThe {temp_list[randnum][0]} {temp_list[randnum][1].capitalize()} is a sport {temp_list[randnum][2]} that accelerates from 0-100km/h in {temp_list[randnum][3]} seconds, powered by a {temp_list[randnum][4]} cylinder {temp_list[randnum][5]} engine, which produces {temp_list[randnum][6]} horsepower and gives the car a top speed of {temp_list[randnum][7]}km/h.")
    except FileNotFoundError:
        print("Car database csv file doesn't exist.")

#car guesser
def car_guess(cardatabase):
    try:
        temp_list = []
        with open(cardatabase, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                temp_list.append(row)
        randcar = randint(0,len(temp_list))
        guess = ''
        quit = 'quit'.upper()
        count = 0
        while guess != (f"{temp_list[randcar][0].upper()} {temp_list[randcar][1].upper()}") and quit:
            if count == 0:
                guess = input(f"\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds. ")
                guess = guess.upper()
                count += 1
            elif count < 5:
                guess = guess.upper()
                count += 1
            elif count == 5:
                guess = input(f"\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine. ")
                guess = guess.upper()
                count += 1
            elif count < 10:
                guess = guess.upper()
                count += 1
            elif count == 10:
                guess = input(f"\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine, which produces {temp_list[randcar][6]} horsepower and gives the car a top speed of {temp_list[randcar][7]}km/h. ")
                guess = guess.upper()
                count += 1
            elif count < 15:
                guess = guess.upper()
                count += 1
            elif count == 15:
                guess = input(f"\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine, which produces {temp_list[randcar][6]} horsepower and gives the car a top speed of {temp_list[randcar][7]}km/h. It is a {temp_list[randcar][2]} .")
                guess = guess.upper()
                count += 1
            elif count < 20:
                guess = guess.upper()
                count += 1
            elif count == 20:
                guess = input(f"\nThe vehicle you are trying to guess goes from 0-100km/h in {temp_list[randcar][3]} seconds, and is powered by a {temp_list[randcar][4]} cylinder {temp_list[randcar][5]} engine, which produces {temp_list[randcar][6]} horsepower and gives the car a top speed of {temp_list[randcar][7]}km/h. It is a {temp_list[randcar][2]} made by {temp_list[randcar][0]}. ")
                guess = guess.upper()
                count += 1
            else:
                guess = guess.upper()
                count += 1
                print(guess)
                print((f"{temp_list[randcar][0].upper()} {temp_list[randcar][1].upper()}"))
        if guess == 'QUIT':
            print(f"\nThe vehicle you were trying to guess was the {temp_list[randcar][0]} {temp_list[randcar][1].capitalize()}.")
        else:
            guess = print(f"\nGreat work! you correctly guessed the {temp_list[randcar][0]} {temp_list[randcar][1].capitalize()} in {count} guesses.")
    except FileNotFoundError:
        print("Car database csv file doesn't exist.")
