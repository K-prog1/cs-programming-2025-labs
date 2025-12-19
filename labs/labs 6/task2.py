def task2(amount, years):
    if amount < 30000:
        return 0.0
    if years <= 3:
        base_rate = 3.0
    elif 4<= years <= 6:
        base_rate = 5.0
    else:
        base_rate = 2.0
    
    if amount >30000:
        additional = min(5.0, 0.3 * (amount - 30000)/10000)
    else:
        additional = 0.0
    
    rate= base_rate+ additional
    total = amount
    for year in range(years):
        total = total * (1 + rate/100)

    profit = total - amount

    return round(profit,2)

print(task2(30000, 3))