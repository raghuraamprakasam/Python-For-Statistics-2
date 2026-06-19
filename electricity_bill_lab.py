
units_consumed = int(input("Enter the electricity units consumed:"))
fixed_charge = 200
tax_percent = 10
slab_1 = 100
slab_2 = 300
slab_1_rate = 5
slab_2_rate = 7
slab_3_rate = 10
print("The fixed cost for electricity =",fixed_charge," and tax is 10% of the total cost")
if units_consumed < slab_1:
    usage_cost = units_consumed*slab_1_rate
    print("Your usage cost is:",usage_cost)
elif units_consumed < 300 and units_consumed > 100:
    usage_cost = ((slab_1)*(slab_1_rate)) + ((units_consumed-slab_1)*(slab_2_rate))
    print("Your usage cost is:",usage_cost)
else:
    usage_cost = ((slab_1)*(slab_1_rate)) + ((units_consumed-slab_1)*(slab_2_rate)) + ((units_consumed-slab_2)*(slab_2_rate))
    print("Your usage cost is:",usage_cost)
sub_total = fixed_charge + usage_cost
tax_rate = sub_total*(tax_percent/100)
total_cost = sub_total + tax_rate

rebate_energy = 150
rebate_amount = 35
if units_consumed <= rebate_energy:
    total = total_cost - rebate_amount
    print("You are eligible for discount, for using electricity efficiently")
    print("After discounting for efficency")
    print("Your total electricity bill is =",total,"In rupees")
else:
    print("You are not eligible for discount,")
    print("Since your electricty consumed is more than efficeint usage")
    print("Your electricity bill for the month is =",total_cost,"in rupees")



    
    
                                             
                                        
