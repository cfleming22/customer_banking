"""Import the create_cd_account and create_savings_account functions"""
from cd_account import create_cd_account
from savings_account import create_savings_account

def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    try:
        savings_balance = float(input("Enter the initial savings account balance: "))
        savings_interest = float(input("Enter the APR interest rate for the savings account (as a percentage): "))
        savings_maturity = int(input("Enter the length of months to calculate interest for savings: "))

        # Call the create_savings_account function and pass the variables from the user.
        updated_savings_balance, savings_interest_earned = create_savings_account(
            savings_balance, savings_interest, savings_maturity
        )

        # Print out the interest earned and updated savings account balance with interest earned
        print(f"\nSavings Account Summary:")
        print(f"Interest earned: ${savings_interest_earned:,.2f}")
        print(f"Updated balance: ${updated_savings_balance:,.2f}")

        # Prompt the user to set the CD balance, interest rate, and months for the CD account.
        cd_balance = float(input("\nEnter the initial CD account balance: "))
        cd_interest = float(input("Enter the APR interest rate for the CD account (as a percentage): "))
        cd_maturity = int(input("Enter the length of months for the CD: "))

        # Call the create_cd_account function and pass the variables from the user.
        updated_cd_balance, cd_interest_earned = create_cd_account(
            cd_balance, cd_interest, cd_maturity
        )

        # Print out the interest earned and updated CD account balance with interest earned
        print(f"\nCD Account Summary:")
        print(f"Interest earned: ${cd_interest_earned:,.2f}")
        print(f"Updated balance: ${updated_cd_balance:,.2f}")

    except ValueError as e:
        print("\nError: Please enter valid numeric values for balances, interest rates, and months.")
        print("Balances and interest rates should be numbers, and months should be whole numbers.")
        return

if __name__ == "__main__":
    main()
