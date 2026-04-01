import os
from datetime import datetime

# Function to get positive input (Feature #5: Input Validation)
def get_positive_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number!")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")

# Function to format currency (Feature #2: Better Formatting)
def format_money(amount):
    return f"₹{amount:.2f}"

# Function to save results to file (Feature #6: Save to File)
def save_to_file(data):
    filename = f"rent_calc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as f:
        f.write(data)
    print(f"\n Results saved to: {filename}")

# Main calculator function
def calculate_rent():
    print("\n" + "="*50)
    print("🏠 RENT CALCULATOR 🏠")
    print("="*50)
    
    # Feature #8: Get person names
    persons = get_positive_input("\nEnter the number of persons sharing = ")
    names = []
    for i in range(persons):
        name = input(f"Enter name of person {i+1} = ")
        names.append(name)
    
    # Get expenses
    rent = get_positive_input("\nEnter hostel/flat rent = ")
    food = get_positive_input("Enter amount spent on food = ")
    electricity_spend = get_positive_input("Enter total electricity spend (in units) = ")
    charge_per_unit = get_positive_input("Enter charge per unit = ")
    water = get_positive_input("Enter water bill = ")  # Feature #3: Water
    internet = get_positive_input("Enter internet bill = ")  # Feature #3: Internet
    
    # Calculate totals
    total_electricity = electricity_spend * charge_per_unit
    total_bill = rent + food + total_electricity + water + internet
    
    # Feature #4: Calculate remainder
    per_person = total_bill // persons
    remainder = total_bill % persons
    
    # Build output string for display and saving
    output = "\n" + "="*50 + "\n"
    output += "BILL BREAKDOWN\n"
    output += "="*50 + "\n"
    
    # Feature #1: Show breakdown
    output += f"Rent:             {format_money(rent)}\n"
    output += f"Food:             {format_money(food)}\n"
    output += f"Electricity ({electricity_spend} units × {charge_per_unit}): {format_money(total_electricity)}\n"
    output += f"Water:            {format_money(water)}\n"
    output += f"Internet:         {format_money(internet)}\n"
    output += "-"*50 + "\n"
    output += f"TOTAL BILL:       {format_money(total_bill)}\n"
    output += "="*50 + "\n"
    
    # Per person breakdown
    output += f"\n👥 PER PERSON BREAKDOWN ({persons} persons):\n"
    output += "-"*50 + "\n"
    output += f"Each person pays: {format_money(per_person)}\n"
    
    # Feature #4: Show remainder
    if remainder > 0:
        output += f"Remaining amount: {format_money(remainder)}\n"
        output += f"(First {remainder} person/people pay ₹{per_person + 1:.2f})\n"
    
    output += "-"*50 + "\n"
    
    # Feature #8: Individual billing
    output += "\n INDIVIDUAL BILLS:\n"
    output += "-"*50 + "\n"
    for i, name in enumerate(names):
        if i < remainder:
            amount = per_person + 1
        else:
            amount = per_person
        output += f"{name}: {format_money(amount)}\n"
    
    output += "="*50 + "\n"
    
    # Display results
    print(output)
    
    # Feature #6: Save to file
    save_choice = input("\nDo you want to save results to file? (yes/no) = ").lower()
    if save_choice in ['yes', 'y']:
        save_to_file(output)
    
    return True

# Feature #7: Multiple calculations with loop
def main():
    while True:
        calculate_rent()
        
        # Feature #7: Ask if they want to calculate again
        again = input("\n🔄 Do you want to calculate again? (yes/no) = ").lower()
        if again not in ['yes', 'y']:
            print("\n Thank you for using Rent Calculator!")
            input("Press Enter to exit...")
            break

# Run the program
if __name__ == "__main__":
    main()