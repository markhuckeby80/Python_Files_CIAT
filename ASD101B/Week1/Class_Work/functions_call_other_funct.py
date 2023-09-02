

# Example of a function calling another function

def cel2fahr(celsius):
    fahr = celsius * 9/5 + 32
    return fahr

# fahrenheit = cel2fahr(32)
# print(fahrenheit)


def farh2cel(fahr):
    cel = (fahr - 32) * 5/9
    return cel


def cel2kelvin(celsius):
    kel = celsius + 273.15
    return kel


def farh2kelvin(fahr):
    cel = farh2cel(fahr)
    kel = cel2kelvin(cel)
    return kel


kel1 = cel2kelvin(32)
kel2 = farh2kelvin(89.6)

print(f'The value of kelvin to celcius is {kel1}, which should be the same for fahrenheit {kel2}')

# fahrenheit = cel2fahr(32)
# celsius = farh2cel(fahrenheit)
# print(celsius)