def coke():
    price = 50
    cents = [25, 10, 5]
    while price > 0:
        print(f"Amount Due: {price}")
        cash = int(input("Insert Coin: "))
        if cash in cents:
            price -= cash
    print(f"Change Owed: {abs(price)}")


def main():
    coke()


if __name__ == "__main__":
    main()
