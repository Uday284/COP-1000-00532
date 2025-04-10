import os

# Define file path for storing vehicle data
file_path = "allowed_vehicles.txt"

# Function to load vehicles from the file
def load_vehicles():
    if not os.path.exists(file_path):
        # Return a default list if the file doesn't exist
        return ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']
    
    # If file exists, read vehicles from the file
    with open(file_path, 'r') as file:
        vehicles = file.readlines()
    return [vehicle.strip() for vehicle in vehicles]

# Function to save vehicles to the file
def save_vehicles(vehicles):
    with open(file_path, 'w') as file:
        for vehicle in vehicles:
            file.write(f"{vehicle}\n")

# Function to print all authorized vehicles
def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Function to search for a vehicle
def search_vehicle():
    vehicle_name = input("Enter the vehicle name to search for: ")
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is authorized.")
    else:
        print(f"{vehicle_name} is not authorized.")

# Function to add a vehicle
def add_vehicle():
    vehicle_name = input("Enter the vehicle name to add: ")
    if vehicle_name not in AllowedVehiclesList:
        AllowedVehiclesList.append(vehicle_name)
        save_vehicles(AllowedVehiclesList)
        print(f"{vehicle_name} has been added to the list.")
    else:
        print(f"{vehicle_name} is already in the list.")

# Function to delete a vehicle
def delete_vehicle():
    vehicle_name = input("Enter the vehicle name to delete: ")
    if vehicle_name in AllowedVehiclesList:
        AllowedVehiclesList.remove(vehicle_name)
        save_vehicles(AllowedVehiclesList)
        print(f"{vehicle_name} has been removed from the list.")
    else:
        print(f"{vehicle_name} is not in the list.")

# Function to display the menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

# Main program flow
def main():
    global AllowedVehiclesList
    AllowedVehiclesList = load_vehicles()  # Load the list of vehicles from the file
    
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            print_vehicles()  # Call the function to print all authorized vehicles
        elif choice == '2':
            search_vehicle()  # Call the function to search for a specific vehicle
        elif choice == '3':
            add_vehicle()  # Call the function to add a new vehicle
        elif choice == '4':
            delete_vehicle()  # Call the function to delete a vehicle
        elif choice == '5':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break  # Exit the program
        else:
            print("Invalid option, please try again.")

# Run the main program
if __name__ == "__main__":
    main()
