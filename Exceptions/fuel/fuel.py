def fuelGauge():
	while True:
		fuel = input("Fraction: ")
		try:
			tmp = fuel.split("/")
			res = int(tmp[0]) / int(tmp[1])
			if (res > 1):
				continue
			return "F" if ((res) >= 0.99 and \
				  (res) <= 1.00)  \
					else ("E" if  (res) <= 0.01 \
		  				else res)
		except (ValueError, IndexError, ZeroDivisionError):
			pass

def main():
	fu = fuelGauge()
	try:
		print(str(int(fu * 100 + 0.5)) + "%", end="")
	except (TypeError, ValueError):
		print(fu, end="")

if __name__ == "__main__":
	main()
