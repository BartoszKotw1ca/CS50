def grocery():
	table = {}
	while True:
		try:
			food = input("")
			if (food in table):
				table[food] += 1
			else:
				table[food] = 1
		except EOFError:
			break
	sort = {k: table[k] for k in sorted(table)}
	print("\n", end="")
	for key in sort:
		print(sort[key], key.upper())

def main():
	grocery()

if __name__ == "__main__":
	main()
