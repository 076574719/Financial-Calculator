def compound_interest(principal, annual_rate, times_compounded, years):
    amount = principal * (1 + (annual_rate / 100) / times_compounded) ** (times_compounded * years)
    return round(amount, 2)

#Get user input
principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
times_compounded = int(input("Enter the number of times interest is compounded per year: "))
years = float(input("Enter the number of years: "))

#Calculate compound interest
final_amount = compound_interest(principal, annual_rate, times_compounded, years)

#Display the result
print(f"Final amount after {years} years: {final_amount}")

