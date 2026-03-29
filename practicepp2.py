customer = input("Enter customer name: ")

total = 0.0
items = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item == "done":
        break
    price = float(input("Enter price: "))
    total = total + price
    items = items + 1

print("Customer :", customer.upper())
print("Items :", items)
print("Subtotal :", total, "KZT")

hour = int(input("Enter current hour (0-23): "))

print("-" * 30)

if hour >= 6 and hour < 12:
    type = "Morning discount"
    discount = total * 0.10
    discounted = total - discount
    tip = discounted * 0.10
    final_total = discounted + tip
    print("Time period :", type)
    print("Discount :", discount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", final_total, "KZT")
elif hour >= 12 and hour < 17:
    type = "No discount"
    discount = 0.0
    discounted = total - discount
    tip = discounted * 0.10
    final_total = discounted + tip
    print("Time period :", type)
    print("Discount :", discount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", final_total, "KZT")
elif hour >= 17 and hour < 22:
    type = "Evening discount"
    discount = total * 0.05
    discounted = total - discount
    tip = discounted * 0.10
    final_total = discounted + tip
    print("Time period :", type)
    print("Discount :", discount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", final_total, "KZT")
else:
    print("Closed")

print("-" * 30)

print("Name uppercase :", customer.upper())
print("Name lowercase :", customer.lower())
print("Name length :", len(customer))

if customer[0].upper() == "A" or customer[0].upper() == "S":
    print("VIP customer")
else:
    print("Regular customer")