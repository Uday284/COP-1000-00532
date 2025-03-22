import sys

def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("\n1. PRINT all Authorized Vehicles")
    print("2. Exit")

def print_vehicles():
    allowed_vehicles_list = [
        'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan'
    ]
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)
    print("\n")

def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            print_vehicles()
        elif choice == "2":
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            sys.exit()
        else:
            print("\nInvalid input, please enter a valid option.\n")

if __name__ == "__main__":
    main()