import random


def validate_input(s):
    if not s.isdigit():
        print("Invalid input (please enter a number)")
        return False
    x = int(s)
    if x > 100 or x < 1:
        print("your number must be between 1 and 100")
        return False
    return True


def main():
    num = random.randint(1, 100)

    score = 100

    while True:
        s = input("Guess the number betweem 1 and 100 (or type 'exit' to quit): ")
        if s == 'exit':
            print("Game exited. The number was:", num)
            break
        if not validate_input(s):
            continue
        x = int(s)
        if x == num:
            print("Correct answer!\nYour score is:", score)
            break
        elif x < num:
            print("Answer is more than", x)
        else:
            print("Answer is less than", x)
        score = max(score - 10, 0)


if __name__ == '__main__':
    while True:
        main()
        S = input("Do you wanna play again ? (if yes type 'Y' otherwise type anything else): ")
        if S != 'Y': 
            break