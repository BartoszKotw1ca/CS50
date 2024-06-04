import emoji

def emojii(str):
	print(emoji.emojize(str, language="alias"))

def main():
	str = input("").strip()
	emojii(str)

if	__name__ == "__main__":
	main()
