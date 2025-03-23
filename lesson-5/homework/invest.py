import math


def invest(_amount, _rate, _years):
    p = 1 + _rate
    for i in range(1, _years + 1):
        _amount *= p
        print(f"year {i}: ${round(_amount, 2)}")

amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate in percent: "))
years = int(input("Enter how many years to calculate for: "))

invest(amount, rate / 100, years)