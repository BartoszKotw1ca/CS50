def omit_vowels(str):
	res = ""
	vowels = ["a", "e", "i", "o", "u"]
	for char in str:
		if char.lower() not in vowels:
			res += char
	print(res)

def main():
	omit_vowels(input("Input: "))

if __name__ == "__main__":
	main()
