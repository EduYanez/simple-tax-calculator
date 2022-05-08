income = float(input("Enter the annual income: "))

# if income is greater than $85,528 then you need to:
# 1) calculate 18% of it and 2) substract a fixed 556.02 amount
scheme_1 = float((0.18*income)-556.02)

# if income is lower than $85,528 then you have to:
# 1) extract the difference between actual income and limit income 2) calculate its 32% 3) add a fixed amount of 14839.02
scheme_2 = float(14839.02+(0.32*(income-85528)))

if income > 85528: #if income is lesser than $85,528 
    tax = scheme_2
    
else:
    tax = scheme_1

tax = round(tax, 0)
print("The tax is:", tax, "thalers") #thaler = local currency :^)
