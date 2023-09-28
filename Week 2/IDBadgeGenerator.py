# File: IDBadgeGenerator.py
# Author: Julio Reyes

# Documentation: A generator for ID badges, asks for the user's  information, returns them in an organized
# easily readable format.

import time

print ("\n  Welcome to the ID Badge Generator\n")
time.sleep(1.5)
print ("To proceed with the creation of your ID Card")
time.sleep(2)
print ("Fill the following prompts with your information:")
time.sleep(2)

print ()
first_name = input ("First Name: ")
last_name = input ("Last Name: ")
email_address = input ("Email Address: ")
phone_number = input ("Phone Number: ")
job_title = input ("Job Title: ")
id_number = input ("ID Number: ")
hair_color = input ("Hair Color: ")
eye_color = input ("Eye Color: ")
start_month = input ("Start Month: ")
training = input ("Completed any training? [yes/no]: ")

print ("\nYour ID Card is:")
print ("----------------------------------------")
print (f"{last_name.upper()}, {first_name.capitalize()}")
print (job_title.title())
print (f"ID: {id_number}")
print ()
print (email_address.lower())
print (phone_number)
print ()
# This part is different to the sample solution shown in the course. In the solution, the selected approach
# was to encase in curly braces only the variable, making it so that a specific number had to be chosen in
# each case for both lines to line up. Whereas I chose to encase everything in curly braces so that the same 
# number would appear in both cases.
print (f"{'Hair: ' + hair_color.title():<20} Eyes: {eye_color.title()}")
print (f"{'Month: ' + start_month.capitalize():<20} Training: {training.capitalize()}")
print ("----------------------------------------")
print ()
