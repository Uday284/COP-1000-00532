def display_menu():
    print("""
********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. Exit
********************************
""")

def print_allowed_vehicles(allowed_vehicles):
    print("Authorized Vehicles:")
    for vehicle in allowed_vehicles:
        print(vehicle)

def search_vehicle(allowed_vehicles):
    vehicle_name = input("Please Enter the full Vehicle name: ")
    if vehicle_name in allowed_vehicles:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def main():
    allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    
    while True:
        display_menu()
        try:
            user_choice = int(input())
            if user_choice == 1:
                print_allowed_vehicles(allowed_vehicles_list)
            elif user_choice == 2:
                search_vehicle(allowed_vehicles_list)
            elif user_choice == 3:
                print("Exiting program...")
                break
            else:
                print("Invalid option. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
