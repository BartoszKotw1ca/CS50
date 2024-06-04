def shorten(str):
	res = ""
	vowels = ["a", "e", "i", "o", "u"]
	for char in str:
		if char.lower() not in vowels:
			res += char
	return (res)

def main():
	print(shorten(input("Input: ")))

if __name__ == "__main__":
	main()
