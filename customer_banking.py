# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is the balance of your Savings Account? "))
    savings_interest = float(input("What is the interest rate on your Savings Account (no decimal)? "))
    savings_maturity = int(input("What is the number of months that you have had your Savings Account? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
 
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print('Savings account details.')
    format_savings_balance = format(updated_savings_balance,".2f")
    format_interest_earned = format(interest_earned,".2f")
    print(f"Updated Savings Account Balance: ${format_savings_balance}")
    print(f"Savings Interest earned: {format_interest_earned}") 

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("What is the balance of your Certificate of Deposit Account? "))
    cd_interest = float(input("What is the interest rate on your Certificate of Deposit Account (no decimal)? "))
    cd_maturity = int(input("What is the number of months that you have had your Certificate of Deposit Account? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
  
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print('Certificate of Deposit account details.')
    format_cd_balance = format(updated_cd_balance,".2f")
    format_cd_interest_earned = format(cd_interest_earned,".2f")
    print(f"Updated Certificate of Deposit Account Balance: ${format_cd_balance}")
    print(f"Certificate of Deposit Interest earned: {format_cd_interest_earned}")

if __name__ == "__main__":
    # Call the main function.
    main()