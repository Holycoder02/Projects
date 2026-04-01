# Rent Calculator

A comprehensive rent and expense splitting calculator for shared accommodation.

## Features

- **Multi-Person Support**: Split expenses among multiple people
- **Person Tracking**: Record names of all participants
- **Expense Categories**:
  - Rent
  - Food
  - Electricity (with per-unit calculation)
  - Water Bill
  - Internet Bill
- **Input Validation**: Ensures only positive numbers are entered
- **Currency Formatting**: Displays amounts in Indian Rupees (₹)
- **Save Results**: Export calculations to timestamped text files

## Functions

| Function | Description |
|----------|-------------|
| `get_positive_input(prompt)` | Gets validated positive integer input from user |
| `format_money(amount)` | Formats amounts as Indian Rupees |
| `save_to_file(data)` | Saves calculation results to a timestamped file |
| `calculate_rent()` | Main function that performs rent distribution calculation |

## Usage

Run the application:

```bash
python app.py
```

The program will:
1. Ask for the number of people sharing the accommodation
2. Request names of each person
3. Input all expenses (rent, food, electricity, water, internet)
4. Calculate individual shares
5. Display results and save them to a file

## Example

```
Enter the number of persons sharing = 2
Enter name of person 1 = Alice
Enter name of person 2 = Bob

Enter hostel/flat rent = 10000
Enter amount spent on food = 3000
Enter total electricity spend (in units) = 50
Enter charge per unit = 5
Enter water bill = 500
Enter internet bill = 800
```

## Output

Results show:
- Individual expense breakdowns
- Total amount each person owes
- Adjustments for unequal shares
- Option to save results to file

## Requirements

- Python 3.x
- No external dependencies

## File Naming

Results are saved with the pattern: `rent_calc_YYYYMMDD_HHMMSS.txt`

## Notes

- All amounts should be in the same currency (Rupees by default)
- Electricity calculation: Total Units × Charge per Unit
- Results are saved automatically for record keeping
