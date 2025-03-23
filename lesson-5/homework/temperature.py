def convert_cel_to_far(cel):
    return cel * 9 / 5 + 32


def convert_far_to_cel(fah):
    return (fah - 32) * 5 / 9


fahrenheit = float(input("Enter a temperature in degrees F: "))
to_celsius = convert_far_to_cel(fahrenheit)
print(f"{int(fahrenheit) if fahrenheit.is_integer() else fahrenheit} degrees F = {round(to_celsius, 2)} degrees C")

celsius = float(input("Enter a temperature in degrees C: "))
to_fahrenheit = convert_cel_to_far(celsius)
print(f"{int(celsius) if celsius.is_integer() else celsius} degrees C = {round(to_fahrenheit, 2)} degrees F")
