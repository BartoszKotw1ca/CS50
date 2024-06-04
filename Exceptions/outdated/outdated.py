def outdated():
	months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
	while True:
		data = input("Date: ").strip()
		if data.find("/") == -1:
			lista = data.split(" ")
			if (len(lista[1]) == 1):
				continue
			if (lista[0].capitalize() not in months):
				continue
			elif (int(lista[1].split(",")[0]) > 31 or
		 			int(lista[1].split(",")[0]) <= 0):
				continue
			else:
				for i in range(len(months)):
					if months[i] == lista[0]:
						break
					i += 1
				print(f"{lista[2]}-{i + 1:02d}-{int(lista[1].split(",")[0]):02d}", end="")
				break
		else:
			lista = data.split("/")
			for i in range(len(lista)):
				if lista[i].isdigit() == False:
					break
			if i + 1 != len(lista):
				continue
			if (int(lista[0]) > 12):
				continue
			if (int(lista[1]) > 32 or int(lista[1]) <= 0):
				continue
			print(f"{lista[2]}-{int(lista[0]):02d}-{int(lista[1]):02d}", end="")
			break

def main():
	outdated()

if __name__ == "__main__":
	main()
