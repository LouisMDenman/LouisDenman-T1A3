#Import python packages
import csv

#bookings
def add_booking(fname):
    FirstName = input("Please enter your first name: ")
    LastName = input("Please enter your last name: ")
    Date = input("Please enter the date you would like to book (format: YYYY-MM-DD): ")
    CarBrand = input("Please enter the brand of your car: ")
    CarModel = input("Please enter the model of your car: ")
    Service = input("Do you require a service, upgrade or repair? ")
    with open(fname, "a") as f:
        write = csv.writer(f)
        write.writerow([LastName,FirstName,Date,CarBrand,CarModel,Service])
    print("\nThank you, your appointment is all booked in, see you then!")

def remove_booking():
    print("Remove booking")

def change_booking():
    print("Change booking")

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

