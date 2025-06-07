def total_amount(bill, tip):
    total = bill*(1+0.01*tip)
    total = round(total, 2)
    print("You have to pay $",total)

total_amount(70, 20)