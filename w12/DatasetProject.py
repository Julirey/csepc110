# File: DatasetProject.py
# Author: Julio Reyes

# Summary: This program that reads through a dataset containing information about life expectancies over the years 
# throughout the countries of the world, analyzes it, and outputs relevant insight on it per user command.

# -Full version-

print ()
print ("    Life Expectancy Dataset")
print ()
print ("The following data comes from OurWorldInData.org from an article on the Spanish Flu.")
print ("[https://ourworldindata.org/spanish-flu-largest-influenza-pandemic-in-history]")
print ()
print ("This dataset is licensed under the Creative Commons BY license")
print ("[https://creativecommons.org/licenses/by/4.0/]")
print ()

keep_going = "yes" 

while keep_going.lower() == "yes": 
    life_expectancy_highest = 0
    life_expectancy_highest_name = ""
    life_expectancy_highest_year = 0

    life_expectancy_lowest = 99999999
    life_expectancy_lowest_name = ""
    life_expectancy_lowest_year = 0 

    user_year = int(input("Enter the year of interest: "))
    user_year_life_highest = 0
    user_year_life_highest_name = ""
    user_year_life_lowest = 99999999
    user_year_life_lowest_name = ""
    total_user_year = 0
    total_user_year_count = 0
    average_user_year = 0
    print()

    user_country = input("Enter the country of interest: ")
    user_country_life_highest = 0
    user_country_life_highest_year = 0
    user_country_life_lowest = 99999999
    user_country_life_lowest_year = 0
    total_user_country = 0
    total_user_country_count = 0
    average_user_country = 0
    print()


    with open("Week 11\life-expectancy.csv") as lines: 
        next(lines)
        for line in lines:
            clean_line = line.strip()
            parts = clean_line.split(",")
            country_name = parts[0]
            country_code = parts[1]
            country_year = int(parts[2])
            life_expectancy = float(parts[3])

            if life_expectancy > life_expectancy_highest:
                life_expectancy_highest = life_expectancy
                life_expectancy_highest_name = country_name
                life_expectancy_highest_year = country_year
            elif life_expectancy < life_expectancy_lowest:
                life_expectancy_lowest = life_expectancy
                life_expectancy_lowest_name = country_name
                life_expectancy_lowest_year = country_year

            if country_year == user_year :
                total_user_year += life_expectancy
                total_user_year_count += 1
                average_user_year = total_user_year / total_user_year_count
                if life_expectancy > user_year_life_highest:
                    user_year_life_highest = life_expectancy
                    user_year_life_highest_name = country_name
                elif life_expectancy < user_year_life_lowest:
                    user_year_life_lowest = life_expectancy
                    user_year_life_lowest_name = country_name
            
            if country_name.lower() == user_country.lower():
                total_user_country += life_expectancy
                total_user_country_count += 1
                average_user_country = total_user_country / total_user_country_count
                if life_expectancy > user_country_life_highest:
                    user_country_life_highest = life_expectancy
                    user_country_life_highest_year = country_year
                elif life_expectancy < user_country_life_lowest:
                    user_country_life_lowest = life_expectancy
                    user_country_life_lowest_year = country_year


    print (f"The overall max life expectancy is: {life_expectancy_highest} from {life_expectancy_highest_name} in {life_expectancy_highest_year}")
    print (f"The overall min life expectancy is: {life_expectancy_lowest} from {life_expectancy_lowest_name} in {life_expectancy_lowest_year}")
    print ()
    
    if total_user_year_count != 0:
        print (f"For the year {user_year}:")
        print (f"The average life expectancy across all countries was {average_user_year:.3f}")
        print (f"The max life expectancy was in {user_year_life_highest_name} with {user_year_life_highest}")
        print (f"The min life expectancy was in {user_year_life_lowest_name} with {user_year_life_lowest}")
    else:
        print (f"Information for the year {user_year} was not found")
    print ()

    if total_user_country_count != 0:
        print (f"For the country {user_country.title()}:")
        print (f"The average life expectancy across all years was {average_user_country:.3f}")
        print (f"The max life expectancy was {user_country_life_highest} in the year {user_country_life_highest_year}")
        print (f"The min life expectancy was {user_country_life_lowest} in the year {user_country_life_lowest_year}")
    else:
        print (f"Information for the country {user_country.title()} was not found")
    print ()
    
    keep_going = input("Do you want to look at different information? [YES/NO] ")
    print ()