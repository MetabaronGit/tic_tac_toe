SEPARATOR = "=" * 40

def draw_greeting() -> None:
    """
    Vypíše úvodní pozdrav

    :return: None
    """
    print()
    print("Welcome to Tic Tac Toe")
    print(SEPARATOR)
    print("GAME RULES:".center(len(SEPARATOR)))
    print("""Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""")
    print(SEPARATOR)
    print("Let's start the game".center(len(SEPARATOR)))


def main():
    draw_greeting()


if __name__ == "__main__":
    main()
