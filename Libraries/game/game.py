import random

def main():

	while True:
		try:
			num = int(input("Level: "))
			if (num > 0):
				break
		except ValueError:
			pass
	guess = random.randint(1, num)
	while True:
		try:
			num = int(input("Guess: "))
			if (guess == num):
				print("Just right!", end="")
				break
			elif (num > guess):
				print("Too large!")
			else:
				print("Too small!")
		except ValueError:
			pass

if __name__ == "__main__":
	main()
