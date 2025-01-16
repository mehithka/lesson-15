price = 2.50

def calculate_due(amount_given):
    return amount_given - price
due = calculate_due(4)
print("the amount due is : ", due)