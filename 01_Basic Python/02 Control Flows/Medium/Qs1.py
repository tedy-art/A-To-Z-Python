"""
Question 1:
Implement a program that calculates the discount based on the purchase amount.
If the purchase amount is greater than 100, apply a 10% discount;
otherwise, no discount.
"""

price = int(input())
discount = 10

if price > 100:
    discount_amount = (discount * price) // 100
    discounted_price = price - discount_amount
    print(f"discount price is : {discount_amount} and with discount MRP : {discounted_price}.")
if price < 100:
    print("no discount")