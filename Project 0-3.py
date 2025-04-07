# Initial list of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to display the menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
    print("********************************")

# Function to print all authorized vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    print("\n")

# Function to search for a vehicle in the list
def search_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is an authorized vehicle.")
    else:
        print(f"{vehicle_name} is not an authorized vehicle.")

# Function to add a vehicle to the list
def add_vehicle(vehicle_name):
    AllowedVehiclesList.append(vehicle_name)
    print(f'\nYou have added "{vehicle_name}" as an authorized vehicle\n')

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print_vehicles()
        elif choice == '2':
            vehicle_to_search = input("Please enter the vehicle name to search: ")
            search_vehicle(vehicle_to_search)
        elif choice == '3':
            new_vehicle = input("Please enter the full vehicle name you would like to add: ")
            add_vehicle(new_vehicle)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
