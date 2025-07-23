while True:
    celsius = input('Enter Celsius temp: ')
    if celsius.lower().startswith('q'):
        break
    if celsius == '':
        continue

    try:
        celsius = float(celsius)
    except ValueError as err:
        print("Please enter a number")
    else:
        fahrenheit = ((9 * celsius) / 5) + 32
        print(f'{celsius:.1f}\u00B0 C is {fahrenheit:.1f}\u00B0 F\n')

