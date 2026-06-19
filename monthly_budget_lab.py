# monthly budget programmer

name = input("Enter your name:")
monthly_income = float(input("Enter monthly income:"))
fixed_exp = float(input("Enter your fixed expenses:"))
variable_exp = float(input("Enter your variable expenses:"))
savings_percentage = float(input("Enter the % of monthly income you need to save:"))

expected_savings = monthly_income*(savings_percentage/100)
total_exp = fixed_exp + variable_exp
actual_savings = monthly_income - total_exp

print("Hi",name,"Your monthly income is:",monthly_income)
print("Your total expense for the month is:",total_exp)
print("Your expected savings for the month is:",expected_savings) 
print("Your actual savings after all the expense  for the month is:",actual_savings)

if actual_savings > expected_savings:
    save = actual_savings - expected_savings
    print("Hi",name,"You have made rupees",save,"than you are expected savings, congratulations")
elif actual_savings == expected_savings:
    print("Hi",name,"You have done a good job managing you are expense, and saved your espected savings, try a bit more dude")
elif actual_savings < expected_savings and actual_savings > 0:
    save = expected_savings - actual_savings
    print("Hi",name,"Dude please watch out your expense, couse you are actual savings of rupees",save," is lower than your expected savings")
elif actual_savings == 0 or actual_savings<0:
    print(" Warning!Warning!Warning!Warning!, please look onto your expense",name)

