# Customer Banking System

## Overview
Module 3 challenge 'customer_banking' is application that implements a customer banking system that calculates and tracks interest earned on savings and CD (Certificate of Deposit) accounts. 

## Features
- Calculate interest earned on savings accounts
- Calculate interest earned on CD accounts
- Handle both percentage and decimal interest rate inputs
- Format currency outputs with proper decimal places and comma separators
- Error handling for invalid inputs
- Interactive command-line interface

## File Structure
- `Account.py`: Base class implementation for account management
- `savings_account.py`: Savings account functionality implementation
- `cd_account.py`: CD account functionality implementation
- `customer_banking.py`: Main program with user interface
- `banking_system_demo.ipynb`: Jupyter notebook demonstrating the system's functionality

## Implementation Details

### Account Class
The base `Account` class provides the foundation for both savings and CD accounts with:
- Balance tracking
- Interest tracking
- Methods to update both balance and interest

### Savings Account
The savings account implementation:
- Creates an instance of the Account class
- Calculates interest based on:
  * Initial balance
  * APR (Annual Percentage Rate)
  * Time period in months
- Updates and tracks both balance and earned interest

### CD Account
The CD account implementation:
- Creates an instance of the Account class
- Calculates interest based on:
  * Initial balance
  * APR (Annual Percentage Rate)
  * CD term in months
- Updates and tracks both balance and earned interest

### Interest Calculation
Interest is calculated using the following formula:
```
Monthly Interest Rate = APR / 12
Interest Earned = Initial Balance × Monthly Interest Rate × Number of Months
Final Balance = Initial Balance + Interest Earned
```

## Usage
1. Run the program:
   ```
   python customer_banking.py
   ```
2. Follow the prompts to enter:
   - Initial savings account balance
   - Savings account APR (as a percentage)
   - Time period for savings calculation
   - Initial CD account balance
   - CD account APR (as a percentage)
   - CD term length

3. The program will display:
   - Interest earned on each account
   - Updated balance for each account

## Example Output
```
Enter the initial savings account balance: 1000
Enter the APR interest rate for the savings account (as a percentage): 5
Enter the length of months to calculate interest for savings: 12

Savings Account Summary:
Interest earned: $50.00
Updated balance: $1050.00

Enter the initial CD account balance: 5000
Enter the APR interest rate for the CD account (as a percentage): 0.07
Enter the length of months for the CD: 24

CD Account Summary:
Interest earned: $700.00
Updated balance: $5700.00
```

## Error Handling
The program includes error handling for:
- Invalid numeric inputs
- Negative numbers
- Non-numeric characters
- Empty inputs

## Development Notes
- Built using Python 3
- Implements OOP principles with class inheritance
- Uses f-strings for formatted output
- Includes comprehensive error handling
- Follows PEP 8 style guidelines
