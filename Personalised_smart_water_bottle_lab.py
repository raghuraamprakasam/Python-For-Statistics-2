name = input("enter your name:")
age = int(input("Enter the age:"))
if age <=8:
    target = 1.2
elif age <=13:
    target = 1.8
elif age <= 18:
    target = 2.3
elif age <= 50 :
    target = 3.0
else:
    target = 2.5

print("Hello",name)
print("your daily water intake is",target,"in litres")

water_intake = float(input("Enter the litres of water you intake:"))
progress = ((water_intake)/target)*100
print("You have completed",progress,"% of daily water intake")
if water_intake>=target:
    print("Hi",name,"You have achieved the daily target amount")
elif progress >= 75:
    remaining = target - water_intake
    print("Hi",name,"Still you have to drink",remaining,"Litres of water")
elif progress >=50:
    remaining = target - water_intake
    print("Hi",name,"Still you have to drink",remaining,"Litres of water")
elif progress >=25:
    remaining = target - water_intake
    print("Hi",name,"Still you have to drink",remaining,"Litres of water")
else:
    remaining = target - water_intake
    print("Hi",name,"Still you have to drink",remaining,"Litres of water")
