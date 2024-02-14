first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider? "))

if first_rider_age >= 12 and first_rider_age <= 17:
    golden_passport = input("Do you have a golden passport (yes/no)? ")
    if golden_passport.lower() == "yes":
        first_rider_age = 18

if first_rider_height < 36:
    print("You may not ride.")
else:
    second_rider = input("Is there a second rider (yes/no)? ")

    if second_rider.lower() == "yes":
        second_rider_age = int(input("What is the age of the second rider? "))
        second_rider_height = int(input("What is the height of the second rider? "))

        if second_rider_age >= 12 and second_rider_age <= 17:
            golden_passport_2 = input("Do you have a golden passport (yes/no)? ")
            if golden_passport_2.lower() == "yes":
                second_rider_age = 18
        
        if first_rider_age >= 18 or second_rider_age >= 18:
            print("You may ride.")
        elif first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height >= 52:
            print("You both may ride.")
        elif first_rider_age >= 14 and first_rider_height >= 52 and second_rider_age >= 16 and second_rider_height >= 52:
            print("You may both ride.")
        elif first_rider_age >= 16 and first_rider_height >= 52 and second_rider_age >= 14 and second_rider_height >= 52:
            print("You may both ride.")
        else:
            print("You may not ride.")
    elif first_rider_age >= 18 and first_rider_height >= 62:
        print("You may ride.")
