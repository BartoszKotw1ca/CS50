def extensions(file):
	file = file.strip().lower()
	index = file.rfind(".")
	file = file[index + 1:]
	if index == -1:
		print("application/octet-stream")
	else:
		match file:
			case "gif":
				print("image/gif")
			case "jpg":
				print("image/jpeg")
			case "txt":
				print("text/plain")
			case "zip":
				print("application/zip")
			case "png":
				print("image/png")
			case "jpeg":
				print("image/jpeg")
			case "pdf":
				print("application/pdf")
			case _:
				print("application/octet-stream")


def main():
	file = input("Type your file: ")
	extensions(file)

main()
