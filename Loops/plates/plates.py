def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
	tmp = ""
	if len(s) > 6 or len(s) < 2:
		return 0
	elif s[0].isalpha() == 0 or s[1].isalpha() == 0:
		return 0
	for char in s:
		if char.isalnum() == 0:
			return 0
	for i in range(len(s)):
		if s[i].isdigit():
			tmp += s[i:]
			break
	if tmp:
		if tmp[0] == "0":
			return 0
	for char in tmp:
		if char.isdigit() == 0:
			return 0
	return 1

if __name__ == "__main__":
	main()
