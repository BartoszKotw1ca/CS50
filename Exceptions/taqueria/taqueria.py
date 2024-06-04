def taqueria(food):
	price_list = {
		"Baja Taco": 4.25,
		"Burrito": 7.50,
		"Bowl": 8.50,
		"Nachos": 11.00,
		"Quesadilla": 8.50,
		"Super Burrito": 8.50,
		"Super Quesadilla": 9.50,
		"Taco": 3.00,
		"Tortilla Salad": 8.00
	}
	return price_list[food.title()]

def main():
	sum = 0.0
	while True:
		try:
			sum += taqueria(input("Item: "))
			print(f"${sum:.2f}")
		except EOFError:
			break
		except KeyError:
			continue
	print("\n", end="")

if __name__ == "__main__":
	main()
