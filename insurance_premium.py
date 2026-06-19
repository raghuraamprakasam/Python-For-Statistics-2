name = input("Enter you name:")
age = int(input("Enter age: "))
bmi = float(input("Enter BMI (e.g., 22.5): "))
smoking_status = input("Do you smoke? (yes/no): ").strip().lower()
pre_existing = input("Any pre-existing medical conditions? (yes/no): ").strip().lower()
    
        
base_premium = 3000  
risk_score = 0  
if age < 18:
    age_premium = base_premium * 0.8  
elif age <= 35:
    age_premium = base_premium        
elif age <= 55:
    age_premium = base_premium * 1.3
    risk_score += 1
else:
    age_premium = base_premium * 1.7  
    risk_score += 2

    
bmi_premium_add = 0
if bmi < 18.5:
    bmi_premium_add = 200  
elif bmi <= 24.9:
    bmi_premium_add = 0 
elif bmi <= 29.9:
    bmi_premium_add = 400  
    risk_score += 1
else:
    bmi_premium_add = 800  
    risk_score += 2

    
smoking_premium_add = 0
if smoking_status == "yes":
    smoking_premium_add = 1500

    risk_score += 2

    
conditions_premium_add = 0
if pre_existing == "yes":
    conditions_premium_add = 2000
    risk_score += 2

total_premium = age_premium + bmi_premium_add + smoking_premium_add + conditions_premium_add

if risk_score == 0:
    category = "Low Risk (Preferred)"
elif risk_score <= 2:
    category = "Standard Risk"
elif risk_score <= 4:
        category = "Moderate Risk"
else:
    category = "High Risk (Substandard)"

print("Hi",name,"The calculated premium for the year is",total_premium)
print("You are falling in the",category)
