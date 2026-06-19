name = input("Enter your name:")
speed = float(input("Enter driver's speed (mph): "))
speed_limit = float(input("Enter posted speed limit (mph): "))
vehicle_type = input("Enter vehicle type (car / truck / motorcycle): ").strip().lower()
in_school_zone = input("Was this in a School Zone? (yes/no): ").strip().lower() == "yes"
ran_red_light = input("Did the vehicle run a red light? (yes/no): ").strip().lower() == "yes"

fine = 0.0
penalty_points = 0

speed_diff = speed - speed_limit

if speed_diff > 0:
     if speed_diff <= 10:
         fine += 500
         penalty_points += 1
         violations  = "Minor Speeding"
     elif speed_diff <= 20:
         fine += 1500
         penalty_points += 3
         violations = "Moderate Speeding"
     elif speed_diff <= 30:
         fine += 3000
         penalty_points += 5
         violations = "Severe Speeding"
     else:
         fine += 5000
         penalty_points += 6
         violations = "Reckless Speeding (Criminal)"
        

if in_school_zone:
    fine += 1000 
    penalty_points += 2
    violations_s = "School Zone Endangerment"

if vehicle_type == "truck":
    fine += 1000
    penalty_points += 1

if ran_red_light:
    fine += 1500
    penalty_points += 3
    violations_s_s = "Traffic Signal Non-Compliance (Red Light)"

if penalty_points > 7 :
    violations_s_s_s = print("Your license will be suspended")
else:
    print("You are good to go, but pay the fine.")

print("Hi",name)
print("Your fine amount is of rupee:",fine)
print("complaints:",violations, ',', violations_s ,",", violations_s_s)
print("Please pay the fine as soon as possible")
