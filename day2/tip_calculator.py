print("Welcome to Tip Calculator")
bill = float(input("Enter your Bill : "))
tip_Percentage = float(input("What percent is tip? 10, 12 or 15 : "))
ppl_cnt = int (input("How many people split the bill : "))

tot_bill = round(bill * (1+tip_Percentage/100) ,2)

amount_per_head = tot_bill/ppl_cnt
print(amount_per_head)