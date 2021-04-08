'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

def f_to_c(degrees):
    """Takes degrees (Fahrenheit) and returns value in Celcius"""

    c = (degrees - 32) * (5/9)
    return c

print("\n\n--CONVERT FAHRENHEIT TO CELCIUS--\n enter 'q' to quit")
run = True
while run:
    degrees = input("Degrees Fahrenheit: ")
    if degrees == 'q':
        run = False
    else:
        celcius = int(f_to_c(int(degrees)))
        print(f"{degrees} degrees fahrenheit = {celcius} degrees celcius\n")
