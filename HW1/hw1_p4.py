
principal = int(input("Principal amount? "))
months = int(input("Lending period? "))

rates = float(input("Interest rates? "))

# TODO 1. compute and 2. print the repayment for each month

monthly_pay = principal/months 
sum = 0
rate_m = rates/(100*12)

for  i in range(1, months+1):
    interest = (principal-monthly_pay*(i-1))*rate_m
    print (f"Month {i} = {(interest + monthly_pay)//1:.0f}")
    sum += (interest + monthly_pay)//1
           
    
    
    




# TODO 3. print the total repayments
print(f"Total repayment = {sum//1:.0f}")
