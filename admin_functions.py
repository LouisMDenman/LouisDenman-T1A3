#Import python packages
import csv

#bookings
def add_booking(fname):
    FirstName = input("Please enter your first name: ").capitalize()
    LastName = input("Please enter your last name: ").capitalize()
    Date = input("Please enter the date you would like to book (format: YYYY-MM-DD): ")
    CarBrand = input("Please enter the brand of your car: ").capitalize()
    CarModel = input("Please enter the model of your car: ").capitalize()
    Service = input("Do you require a service, upgrade or repair? ").capitalize()
    with open(fname, "a") as f:
        write = csv.writer(f)
        write.writerow([LastName,FirstName,Date,CarBrand,CarModel,Service])
    print("\nThank you, your appointment is all booked in, see you then!")

def remove_booking(fname):
    Fname = input("\nEnter your first name to select your bookings: ").capitalize()
    Lname = input("Enter your last name to select your bookings: ").capitalize()
    Date = input("What was the date of the booking you would like to cancel? (format: YYYY-MM-DD): ")
    CarBrand = input("What was the brand of car for this booking: ").capitalize()
    Service = input("Finally, was this booking a service, upgrade or repair? ").capitalize()
    temp_list = []
    with open(fname, "r") as f:
        read = csv.reader(f)
        for row in read:
            if (row[1] == Fname) and (row[0] == Lname) and (row[2] == Date) and (row[3] == CarBrand) and (row[5] == Service):
                pass
            else:
                temp_list.append(row)



def view_booking(fname):
    try:
        Fname = input("\nEnter your first name to see your booked services: ").capitalize()
        Lname = input("Enter your last name to see your booked services: ").capitalize()
        appts = False
        with open(fname, "r") as f:
            read = csv.reader(f)
            read.__next__()
            for row in read:
                if row[0] == Lname and row[1] == Fname:
                    print(f"\n{row[1]} {row[0]}'s {row[3]} {row[4]} is booked in for {row[5]} on the {row[2]}")    
                    appts = True
            if appts == False:
                print("\nWe have no bookings under this name.")
    except FileNotFoundError:
        print("Booking csv file doesn't exist.")

#information
def specific_car_information():
    print("Specific car info")

def random_car_information():
    print("Random car info")

#configurator
def parts_in_stock():
    print("Parts in stock")

def new_configuration():
    print("New configuration")

def existing_configuration():
    print("Existing configuration")

