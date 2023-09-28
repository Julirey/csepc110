# File: DatasetProject.py
# Author: Julio Reyes

# Summary: This program that reads through a dataset containing information about life expectancies over the years 
# throughout the countries of the world, analyzes it, and outputs relevant insight on it per user command.

# -Milestone version-

life_expectancy_highest = 0
life_expectancy_lowest = 99999999

print ()
print ("    Life Expectancy Dataset")
print ()
print ("The following data comes from OurWorldInData.org from an article on the Spanish Flu.")
print ("[https://ourworldindata.org/spanish-flu-largest-influenza-pandemic-in-history]")
print ()
print ("This dataset is licensed under the Creative Commons BY license")
print ("[https://creativecommons.org/licenses/by/4.0/]")
print ()

with open("Week 11\life-expectancy.csv") as lines: 
    next(lines)
    for line in lines:
        clean_line = line.strip()
        parts = clean_line.split(",")
        life_expectancy = float(parts[3])
        if life_expectancy > life_expectancy_highest:
            life_expectancy_highest = life_expectancy
        elif life_expectancy < life_expectancy_lowest:
            life_expectancy_lowest = life_expectancy

print (f"The highest value for life expectancy is: {life_expectancy_highest}")
print (f"The lowest value for life expectancy is: {life_expectancy_lowest}")

print ()