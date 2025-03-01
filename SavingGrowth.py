def savings_growth(initial, monthly, annual_rate, years):
    months = years * 12
    rate = (annual_rate / 100) / 12
    total = initial
    for _ in range(months):
        total = (total + monthly) * (1 + rate)
    return round(total, 2)

def savings_calculator():
    print("Welcome to the Savings Growth Calculator!")
    
    try:
        initial_investment = float(input("Enter the initial investment amount: $"))
        monthly_contribution = float(input("Enter the monthly contribution amount: $"))
        annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
        investment_duration_years = int(input("Enter the investment duration (in years): "))

        #Calculate the final amount
        final_amount = savings_growth(initial_investment, monthly_contribution, annual_interest_rate, investment_duration_years)
        
        #Display the result
        print(f"\nFinal amount after {investment_duration_years} years: ${final_amount}")
    
    except ValueError:
        print("Invalid input. Please make sure to enter numerical values.")

if __name__ == "__main__":
    savings_calculator()