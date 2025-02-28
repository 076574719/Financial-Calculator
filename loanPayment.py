def loan_payment(principal, annual_rate, years):
    rate = annual_rate / 100 / 12  # Convert annual rate to monthly rate
    months = years * 12  # Convert years to months
    payment = (principal * rate) / (1 - (1 + rate) ** -months)
    return round(payment, 2)

#Get user input
principal = float(input("Enter the loan amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the loan term (in years): "))

#Calculate monthly payment
monthly_payment = loan_payment(principal, annual_rate, years)

#Display the result
print(f"Monthly payment: {monthly_payment}")

