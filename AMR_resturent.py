print("=" * 40)
print("      WELCOME TO AMR RESTAURANT")
print("=" * 40)
Menu = {
    1: ("Burger", 250),
    2: ("Medium Pizza", 600),
    3: ("Large Pizza", 1200),
    4: ("Tea", 100),
    5: ("Cold Drink", 150),
    6: ("Finger Fries", 150),
    7: ("Full Chicken", 1000),
    8: ("Shawarma", 200),
    9: ("Zinger Burger", 350),
    10: ("Chicken Roll", 180),
    11: ("Chicken Karahi", 1500),
    12: ("Biryani", 300),
    13: ("Ice Cream", 120),
    14: ("Coffee", 180)
}
total = 0
while True:
    print("\n" + "-" * 40)
    print("MENU")
    print("-" * 40)

    for i in Menu:
        print(f"{i}. {Menu[i][0]:<15} Rs {Menu[i][1]}")

    print("-" * 40)
    choice = int(input("Enter choice (0 to exit): "))
    if choice == 0:
        break
    qty = int(input("Quantity: "))
    if choice in Menu:
        name, price = Menu[choice]
        cost = price * qty
        total += cost
        print("Added:", name, "x", qty, "=", cost)
    else:
        print("Wrong choice!")
print("\n" + "=" * 40)
print("BILL RECEIPT")
print("=" * 40)
print("Total Amount:", total)
print("=" * 40)
print("Thank you for visiting AMR Restaurant")
print("=" * 40)print("=" * 40)
print("      WELCOME TO AMR RESTAURANT")
print("=" * 40)

Menu = {
    1: ("Burger", 250),
    2: ("Medium Pizza", 600),
    3: ("Large Pizza", 1200),
    4: ("Tea", 100),
    5: ("Cold Drink", 150),
    6: ("Finger Fries", 150),
    7: ("Full Chicken", 1000),
    8: ("Shawarma", 200),
    9: ("Zinger Burger", 350),
    10: ("Chicken Roll", 180),
    11: ("Chicken Karahi", 1500),
    12: ("Biryani", 300),
    13: ("Ice Cream", 120),
    14: ("Coffee", 180)
}

total = 0

while True:
    print("\n" + "-" * 40)
    print("MENU")
    print("-" * 40)

    for i in Menu:
        print(f"{i}. {Menu[i][0]:<15} Rs {Menu[i][1]}")

    print("-" * 40)

    choice = int(input("Enter choice (0 to exit): "))

    if choice == 0:
        break

    qty = int(input("Quantity: "))

    if choice in Menu:
        name, price = Menu[choice]
        cost = price * qty
        total += cost
        print("Added:", name, "x", qty, "=", cost)
    else:
        print("Wrong choice!")

print("\n" + "=" *40)