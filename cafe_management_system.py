#menu of the cafe
menu = {
    'Pizza': 120,
    'Pasta': 90,
    'Chai': 30,
    'Coffee': 60,
    'Chowmin': 80,
    'Filter coffee': 140,
    'Sandwich': 60,
    'Garlic bread': 70,
}

print("Welcome to apna cafe.")
print("Pizza: 120\nPasta: 90\nChai: 30\nCoffee: 60\nChowmin: 80\nFilter coffee: 140\nSandwich: 60\nGarlic bread: 70")

#for total amount
order_total = 0

item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your item {item_1} has been added to your order.")
else:
    print("This item {item_1} is not available in the menu!")

another_order = input("Do you want to add another item in your order? (yes/no) ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} has been added to your order.")
    else:
        print(f"{item_2} is not available in the menu!")

print(f"Total amount of items to pay is {order_total}")
print("Thank You")
    

