def bank(greeting):
	greeting = greeting.strip().lower()
	if (greeting[0:5] == "hello"):
		print("$0")
	elif (greeting[0] == 'h'):
		print("$20")
	else:
		print("$100")

def main():
	greeting = input("Write something: ")
	bank(greeting)

main()
