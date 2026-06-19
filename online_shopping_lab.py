
product_cost = float(input("Enter the cost of the product:"))
product_q = int(input("Enter the quantity of product:"))
membership = input("Enter your membership status (YES/NO):")
coupon = input("Enter your coupon status (YES/NO):")
payment_method = input("Enter your payment method (CARD/CASH):")
card_payment_per = 1
tax_per = 6
shipping_per = 5
reward_1 = 2
reward_2 = 4
reward_3 = 6
cost = product_cost * product_q
print("Bill Summary")
# calculating the total cost after membership and coupon discount
if (membership == "yes" or membership == "Yes" or membership == "YES") and (coupon == "yes" or coupon == "Yes" or coupon =="YES"):
    membership_dis = cost*(10/100)
    cost_after_mem = cost - membership_dis
    coupon_dis = cost_after_mem*(3/100)
    cost_m_c = cost_after_mem - coupon_dis
    tax_rate = cost_m_c*(tax_per/100)
    shipping_rate = cost_m_c*(shipping_per/100)
    total_cost = cost_m_c + tax_rate + shipping_rate
    print("Membership disocunt = ",membership_dis)
    print("Coupon discount =",coupon_dis)
    print("Tax rate = ",tax_rate)
    print("Shipping Rate =",shipping_rate)
elif (membership == "yes" or membership == "Yes" or membership == "YES") and (coupon == "No" or coupon == "no" or coupon == "NO"):
    membership_dis = cost*(10/100)
    cost_after_mem = cost - membership_dis
    tax_rate = cost_after_mem*(tax_per/100)
    shipping_rate = cost_after_mem*(shipping_per/100)
    total_cost = cost_after_mem + tax_rate + shipping_rate
    print("Membership disocunt =",membership_dis)
    print("Tax rate = ",tax_rate)
    print("Shipping Rate =",shipping_rate)
elif (membership == "No" or membership == "no" or membership == "NO") and (coupon == "Yes" or coupon == "yes"or coupon =="YES"):
    coupon_dis = cost*(3/100)
    cost_after_cou = cost - coupon_dis
    tax_rate = cost_after_cou*(tax_per/100)
    shipping_rate = cost_after_cou*(shipping_per/100)
    total_cost = cost_after_cou + tax_rate + shipping_rate
    print("Coupon discount =",coupon_dis)
    print("Tax rate = ",tax_rate)
    print("Shipping Rate =",shipping_rate)
else:
    tax_rate = cost*(tax_per/100)
    shipping_rate = cost*(shipping_per/100)
    total_cost = cost + tax_rate + shipping_rate
    print("membership discount =",0)
    print("coupon discount =",0)
    print("Tax rate = ",tax_rate)
    print("Shipping Rate =",shipping_rate)
    

#calculating the charges for the card payment
if payment_method == "card" or payment_method=="Card":
    card_payment_charge = total_cost*(card_payment_per/100)
    total_payable = total_cost + card_payment_charge
    print("Card charges = ",card_payment_charge)
else:
    card_payment_charge = 0
    total_payable = total_cost
    print("Card charges = ",card_payment_charge)
    

    
# checking whether you are eligible for reward points, if yes how much you have earned
if total_payable <= 2500:
    reward = 0
    print("Reward points = ",reward)
elif total_payable <= 5000 and total_payable > 2500:
    reward = total_payable * (reward_1/100)
    print("Reward points = ",reward)
elif total_payable <= 10000 and total_payable > 5000:
    reward = total_payable *(reward_2/100)
    print("Reward points = ",reward)
else:
    reward = total_payable *(reward_3/100)
    print("Reward points = ",reward)

# checking whether you are eligible for premium membership upgrades
if total_payable > 8000 or reward > 600:
    print("Premium memerchip = Eligible")
else:
    print("Premium membership = Not eligible")
print("Your total payable amount is of rupee:",total_payable)
    
    
    
    
    
    
    
