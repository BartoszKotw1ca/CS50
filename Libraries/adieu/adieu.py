def main():
    res = "Adieu, adieu, to "
    names = []

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass

    if len(names) == 1:
        print(f"{res}{names[0]}")
    elif len(names) == 2:
        print(f"{res}{names[0]} and {names[1]}")
    else:
        formatted_names = ', '.join(names[:-1]) + ", and " + names[-1]
        print(f"{res}{formatted_names}")

if __name__ == "__main__":
    main()
