# Calculate Net Amount

price = int(input("Enter price :"))
qty = int(input("Enter qty : "))
amount = price * qty
discount = amount * 0.15
net_amount = amount - discount

print(f"Amount      : {amount:10}")
print(f"- Discount  : {discount:10.0f}")
print(f"              {'-' * 10}")
print(f"Net Amount  : {net_amount:10.0f}")