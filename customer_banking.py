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
    savings_processing = True
    while savings_processing:
        savings_balance = input("Enter the balance of your Savings Account? ")
        try:
            savings_balance = float(savings_balance)
            savings_balance = round(savings_balance,2)
            print(f"Savings Balance Entered: {savings_balance:.2f}")
            savings_processing = False
        except:
            print("Savings Balance entered is invalid. Please enter a valid number for Savings Balance")
    savings_processing = True
    while savings_processing:
        savings_interest = input("Enter the interest rate on your Savings Account? ")
        try:
            savings_interest = float(savings_interest)
            savings_interest = round(savings_interest,3)
            print(f"Savings Interest Rate Entered: {savings_interest:.3f}")
            savings_processing = False
        except:
            print("Savings Interest entered is invalid. Please enter a valid number for Savings Interest")
    savings_processing = True
    while savings_processing:
        savings_maturity = input("Enter the number of months that you have had your Savings Account? ")
        try:
            savings_maturity = float(savings_maturity)
            savings_maturity = round(savings_maturity,3)
            print(f"Savings Number of Months Entered: {savings_maturity:.3f}")
            savings_processing = False
        except:
            print("Savings Number of Months entered is invalid. Please enter a valid number for Savings Number of Months")    

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
 
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print('Savings account details.')
    format_savings_balance = format(updated_savings_balance,".2f")
    format_interest_earned = format(interest_earned,".2f")
    print(f"Updated Savings Account Balance: ${format_savings_balance}")
    print(f"Savings Interest earned: {format_interest_earned}") 

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_processing = True
    while cd_processing:
        cd_balance = input("Enter the balance of your Certificate of Deposit Account? ")
        try:
            cd_balance = float(cd_balance)
            cd_balance = round(cd_balance,2)
            print(f"Certificate of Deposit Balance Entered: {cd_balance:.2f}")
            cd_processing = False
        except:
            print("Certificate of Deposit Balance entered is invalid. Please enter a valid number for Certificate of Deposit Balance")
    cd_processing = True
    while cd_processing:
        cd_interest = input("Enter the interest rate on your Certificate of Deposit Account? ")
        try:
            cd_interest = float(cd_interest)
            cd_interest = round(cd_interest,3)
            print(f"Certificate of Deposit Interest Rate Entered: {cd_interest:.3f}")
            cd_processing = False
        except:
            print("Certificate of Deposit Interest entered is invalid. Please enter a valid number for Certificate of Deposit Interest")
    cd_processing = True
    while cd_processing:
        cd_maturity = input("Enter the number of months that you have had your Certificate of Depostit Account? ")
        try:
            cd_maturity = float(cd_maturity)
            cd_maturity = round(cd_maturity,3)
            print(f"Certificate of Deposit Months Entered: {cd_maturity:.3f}")
            cd_processing = False
        except:  
            print("Certificate of Deposit Number of Months entered is invalid. Please enter a valid number for Certificate of Deposit Number of Months")    

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