def camel(str):
	res = ""
	for i in range(len(str)):
		if str[i].isupper():
			res += "_"
		res += str[i].lower()
	print(res)

def main():
	camel(input("camelCase: "))

if __name__ == "__main__":
	main()
