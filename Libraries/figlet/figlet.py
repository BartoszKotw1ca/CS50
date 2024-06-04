import sys
from pyfiglet import Figlet
import random
import pyfiglet

def main():
	len_sys_argv = len(sys.argv)
	if (len_sys_argv != 1 and len_sys_argv != 3):
			sys.exit("Invalid usage")
	figlet = Figlet()
	if (len_sys_argv == 1):
		str = input("Input: ")
		num = random.randint(0, len(figlet.getFonts()))
		figlet.setFont(font=figlet.getFonts()[num])
		print(figlet.renderText(str))
	elif (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
		if (sys.argv[2] in figlet.getFonts()):
			str = input("Input: ")
			figlet.setFont(font=sys.argv[2])
			print(figlet.renderText(str))
		else:
				sys.exit("Invalid format")
	else:
		sys.exit("Invalid format")

if __name__ == "__main__":
	main()
