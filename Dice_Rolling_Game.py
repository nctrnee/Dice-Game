import random


def dice_num_getter() -> int:
    while True:
        dice_num = input("How many dice do you want to roll?\nChoose from 1-5: ")
        print()
        try:
            dice_num = int(dice_num)
        except ValueError:  # if user input is not num
            print("ERROR: Enter a whole number from 1-5 only")
            continue  # stops the current loop cycle > starts over.

        if 5 >= dice_num > 0:
            return dice_num
        else:
            print("ERROR: Out of range")


def main():
    playing = True
    counter = 0
    print("WELCOME TO THE DICE ROLLING GAME!")
    while playing:
        choice = input("[x] START    [y] EXIT: ").lower().strip()
        print()

        if choice in ["x", ""]:
            while playing:
                dice_num = dice_num_getter()
                roll_dice(dice_num)
                counter += 1
                print()
                playing = ask_willingness(counter)

        elif choice == "y":
            print_session_summary(counter)
            break

        else:
            print("ERROR: Invalid input")


def roll_dice(num):
    numbers = [random.randint(1, 6) for i in range(1, num + 1)]
    print(f"You rolled: {numbers} = {sum(numbers)}")


def print_session_summary(counter):
    print(f"Session Ended\nTotal Rounds: {counter}")


def ask_willingness(counter):
    while True:
        user_willingness = input("[x] ROLL AGAIN    [y] EXIT: ")
        print()
        if user_willingness in ["x", ""]:
            return True
        elif user_willingness == "y":
            print_session_summary(counter)
            return False
        else:
            print("Invalid input")


if __name__ == '__main__':
    main()
