# File: Windchill.py
# Author: Julio Reyes

# Summary: This program calculates the windchill by obtaining the temperature from user input, asking whether it is in Fahrenheit or Celsius,
# in case it is in Celsius it gets converted into Fahrenheit, and lastly computes the windchill through wind speeds of 5 mph up to 60 mph
# in increments of 5 mph. 

def convert_to_fahrenheit(temperature):
    return temperature * (9/5) + 32

def compute_windchill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)

keep_going = "yes"
while keep_going.lower() == "yes":
    temperature = 0
    wind_speed = 5 
    measure_unit = "" 

    print()
    temperature_input = int(input("What is the temperature? "))

    while measure_unit not in ["C", "F"]:
        measure_unit = input("Fahrenheit or Celsius (F/C)? ")
        measure_unit = measure_unit.upper()
        if measure_unit == "F":
            temperature = temperature_input
        elif measure_unit == "C":
            temperature = convert_to_fahrenheit(temperature_input)
        else:
            print ("It has to be either Fahrenheit (F) or Celsius (C)")
    print()

    while wind_speed <= 60:
        windchill = compute_windchill(temperature, wind_speed)
        print (f"At temperature {temperature:.2f}F, and wind speed {wind_speed:>2} mph, the windchill is: {windchill:>10.2f}F")
        wind_speed += 5
    print()

    keep_going = input ("Repeat? [Yes/No] ")