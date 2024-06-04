def is_valid(s):
    tmp = ""
    if len(s) > 6 or len(s) < 2:
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False
    for char in s:
        if not char.isalnum():
            return False
    for i in range(len(s)):
        if s[i].isdigit():
            tmp += s[i:]
            break
    if tmp:
        if tmp[0] == "0":
            return False
    for char in tmp:
        if not char.isdigit():
            return False
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
