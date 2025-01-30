"""Import the Account class from the Account.py file."""
from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the Account class with initial balance and interest of 0
    savings_account = Account(balance, 0)
    
    # Calculate interest earned
    # Convert interest_rate to decimal if it's not already (handle both 5 and 0.05 inputs)
    interest_rate = interest_rate if interest_rate < 1 else interest_rate/100
    interest_earned = balance * (interest_rate/12) * months
    
    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned
    
    # Pass the updated_balance to the set balance method
    savings_account.set_balance(updated_balance)
    
    # Pass the interest_earned to the set interest method using the instance of the Account class
    savings_account.set_interest(interest_earned)
    
    # Return the updated balance and interest earned
    return updated_balance, interest_earned
