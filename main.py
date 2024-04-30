
def main():
    print("\nHey, Welcome to Gallo 24 Car Garage! \n")
    print("Enter 1 to add, remove or change a booking.")
    print("Enter 2 to access information or learn more about different models of cars.")
    print("Enter 3 to access the build configurator.")
    print("Enter 4 to exit the garage.\n")

    feature = input(": ")
    return feature

service = main()

while service != '4':
    service = main()

    if service == '1':
        print("\n1")
    elif service == '2':
        print("\n2")
    elif service == '3':
        print("\n3")
    else:
        print("\nPlease enter one of the options shown above.")


print("\nThanks for visiting the Gallo 24 Car Garage, until next time!")