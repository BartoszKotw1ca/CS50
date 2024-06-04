def interpreter(num1, num2, sign):
	match sign:
		case "+":
			print(num1 + num2)
		case "/":
			if (num2 == 0):
				print("Error")
			else:
				print(num1 / num2)
		case "*":
			print(num1 * num2)
		case "-":
			print(num1 - num2)

def main():
	exp = input("Expression: ")
	exp = exp.split(" ")
	interpreter(float(exp[0]), float(exp[2]), exp[1])

main()
