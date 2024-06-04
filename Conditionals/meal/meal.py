def convert(time):
	time = time.split(":")
	hours = int(time[0])
	min = int(time[1])
	min /= 60;
	return (hours + min)

def main():
	time = input("What time is it? ")
	time = convert(time)
	if (time >= 7 and time <= 8):
		print("breakfast time")
	elif (time >= 12 and time <= 13):
		print("lunch time")
	elif (time >= 18 and time <= 19):
		print("dinner time")

if __name__ == "__main__":
	main()
