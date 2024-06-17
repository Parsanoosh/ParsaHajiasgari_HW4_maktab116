def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

celsius_temperatures = [10, 20, 30, 40, 50]
fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in celsius_temperatures]
print(fahrenheit_temperatures)


