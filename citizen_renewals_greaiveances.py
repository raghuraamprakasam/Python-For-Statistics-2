name = input("Enter your name:")
age = int(input("Enter your age:"))
print("Press 1 for Passport renewal")
print("Press 2 for Driving License Renewal")
print("Press 3 for Tax Payment")
print("Press 4 for Utility Bill Payment")
print("Press 5 for Greivenace Submission")
service = int(input("Enter the service which you want to take:"))

fee = 0
match service:
    case 1:
        eligible = input("Do you have existing passport (YES/NO):").lower()
        if eligible == "yes":
          pass_no = input("Enter you passport number:")
          expiry = input("Enter you expiry date of paasport (DD/MM/YYYY):")
          fee += 1500
          status = "Eligible for Passport renewal"
        else:
            fee = fee
            status = "Not Eligible for Passport Renewal"

    case 2:
        eligible = input("Do you have existing driving license (YES/NO):").lower()
        if eligible == "yes":
          pass_no = input("Enter you driving license number:")
          expiry = input("Enter you expiry date of driving license (DD/MM/YYYY):")
          fee += 1000
          status = "Eligible for driving license renewal "
        else:
            fee = fee
            status = "Not Eligible for driving license renewal"

    case 3:
        tax = float(input("Enter your tax amount:"))
        if tax <= 10000:
            discount = 0
            fee = tax - discount
        elif tax <= 15000:
            discount = tax*(5/100)
            fee = tax - discount
        else:
            discount = tax*(10/100)
            fee = tax - discount

    case 4:
        eligible = input("Enter you house number:")
        am = int(input("Enter your bill amount:"))
        if am < 500:
            discount = 0
            fee = am - discount
        elif am <1500:
            discount = am*(5/100)
            fee = am - discount
        elif am <2500:
            discount = am*(10/100)
            fee = am - discount
        else:
            discount = am*(12/100)
            fee = am - discount

    case 5:
           issue = input(" Is there any issue (YES/NO):").lower()
           if issue == "yes":
               get = input("What is the grevience about, explain in detail:")
               print("Your greivenace submittes successfully, there is no fee for greivenaces submition")
               fee = 0

    case _:
        print("Enter a valid Choice")

print("Hi",name)
print("Your fee for the following is of rupee:",fee)

   

    
          
            
        
