import random

def main():
    level = get_level()
    correct_answers = generate_integer(level)
    print(f"Number of correct answers: {correct_answers}")

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 1 <= lvl <= 3:
                return lvl
        except ValueError:
            pass

def generate_integer(level):
    ranges = [
        range(0, 10),
        range(10, 100),
        range(100, 1000),
    ]

    level_range = ranges[level - 1]
    correct_count = 0

    for _ in range(10):
        num1 = random.randint(level_range.start, level_range.stop - 1)
        num2 = random.randint(level_range.start, level_range.stop - 1)

        for attempt in range(3):
            try:
                guess = int(input(f"{num1} + {num2} = "))
                if guess == num1 + num2:
                    correct_count += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                continue

        if attempt == 2 and guess != num1 + num2:
            print(f"{num1} + {num2} = {num1 + num2}")

    return correct_count

if __name__ == "__main__":
    main()
