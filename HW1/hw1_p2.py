
principal = int(input("Principal amount? "))
months = int(input("Lending period? "))
rates = float(input("Loan rates? "))

# TODO 1. compute monthly interest and total repayments
# 월 이자 = 원금 *(연이율 * 대출기간/12개월)/ 대출기간 (개월)
# 총 상환금 = 원금 + 월 이자(반올림된 금액) * 대출기간 (개월)
monthly_interest = round(principal * ((rates/100) * months/12)/months)
total_repayments = principal + monthly_interest*months


# TODO 2. print the result
print(f"Each month = {monthly_interest}")
print(f"Total repayments = {total_repayments}")
