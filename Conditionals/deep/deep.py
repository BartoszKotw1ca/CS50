def deep(name):
	name = name.strip().lower()
	match name:
		case "42" | "forty-two" | "forty two":
			print("Yes")
		case _:
			print("No")

def main():
	name = input("What is the answer? \n")
	deep(name)

main()
