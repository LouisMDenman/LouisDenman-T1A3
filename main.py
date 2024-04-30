
def main():
    print("\nHey, Welcome to Gallo 24 Car Garage! \n")
    print("Enter 1 to add, remove or change a booking.")
    print("Enter 2 to access information or learn more about different models of cars.")
    print("Enter 3 to access the build configurator.")
    print("Enter 4 to exit the garage.\n")

    user_input = input(": ")
    return user_input

def booking_feature():
        print("\nEnter 1 to add a booking.")
        print("Enter 2 to remove a booking.")
        print("Enter 3 to change a booking.")
        print("Enter 4 to cancel.\n")

        user_input = input(": ")
        return user_input

def carinfo_feature():
        print("\nEnter 1 to get information about a specific car.")
        print("Enter 2 to get information about a random car.")
        print("Enter 3 to cancel.\n")

        user_input = input(": ")
        return user_input

def buildconfig_feature():
        print("\nEnter 1 to see parts in stock for a specific car.")
        print("Enter 2 to start a new configuration.")
        print("Enter 3 to modify an existing configuration.")
        print("Enter 4 to cancel.\n")

        user_input = input(": ")
        return user_input

service = -1

while service != '4':
    service = main()

    if service == '1':
        feature = -1

        while feature != '4':
            feature = booking_feature()

            if feature == '1':
                print("\nPlaceholder for ADD BOOKING function.")
            elif feature == '2':
                print("\nPlaceholder for REMOVE BOOKING function.")
            elif feature == '3':
                print("\nPlaceholder for CHANGE BOOKING function.")
            else:
                print("\nPlease enter one of the options shown above.")

    elif service == '2':
        feature = -1

        while feature != '3':
            feature = carinfo_feature()

            if feature == '1':
                print("\nPlaceholder for SPECIFIC CAR function.")
            elif feature == '2':
                print("\nPlaceholder for RANDOM CAR function.")
            else:
                print("\nPlease enter one of the options shown above.")

    elif service == '3':
        feature = -1

        while feature != '4':
            feature = buildconfig_feature()

            if feature == '1':
                print("\nPlaceholder for PARTS IN STOCK function.")
            elif feature == '2':
                print("\nPlaceholder for NEW CONFIGURATION function.")
            elif feature == '3':
                print("\nPlaceholder for EXISTING CONFIGURATION function.")
            else:
                print("\nPlease enter one of the options shown above.")

    else:
        print("\nPlease enter one of the options shown above.")


print("\nThanks for visiting the Gallo 24 Car Garage, until next time!")