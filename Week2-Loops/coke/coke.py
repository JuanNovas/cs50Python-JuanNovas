print("Amount Due: 50")
due = 50

while due > 0:
    coin = input("Insert Coin: ")
    match coin:
        case "25":
            due -= 25
        case "10":
            due -= 10
        case "5":
            due -= 5
    print(f"Amount Due: {due}")

print(f"Change Owed: {due * -1}")
