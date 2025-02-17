def calculate_bonus(productivity_score):
    if productivity_score <= 30:
        return 50.0
    elif productivity_score <= 69:
        return 75.0
    elif productivity_score <= 199:
        return 100.0
    else:
        return 200.0

def main():
    # Get user input
    employee_name = input("Enter Employee Name: ")
    shifts_worked = int(input("Enter number of shifts: "))
    num_transactions = int(input("Enter number of transactions: "))
    transaction_value = float(input("Enter transactions dollar value: "))
    
    # Calculate productivity score
    if shifts_worked > 0 and num_transactions > 0:
        productivity_score = (transaction_value / num_transactions) / shifts_worked
    else:
        productivity_score = 0  # Handling case where shifts or transactions are zero
    
    # Determine bonus
    bonus = calculate_bonus(productivity_score)
    
    # Print output
    print(f"Employee Name: {employee_name}")
    print(f"Employee Bonus: ${bonus}")

if __name__ == "__main__":
    main()
