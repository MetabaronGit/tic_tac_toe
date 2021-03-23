SCREEN_WIDTH = 41
separator = "=" * SCREEN_WIDTH

def draw_greeting() -> None:
    """
    Vypíše úvodní pozdrav

    :return: None
    """
    print()
    print("Welcome to Tic Tac Toe")
    print(separator)
    print("GAME RULES:".center(SCREEN_WIDTH))
    print("""Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""")
    print(separator)
    print("Let's start the game".center(SCREEN_WIDTH))
    print(separator)


def draw_board(game_board: list) -> None:
    """
    Vykreslí aktuální stav hrací plochy.

    :return: None
    """
    print("+---+---+---+".center(SCREEN_WIDTH))
    print("|{:^3}|{:^3}|{:^3}|".format(game_board[7], game_board[8], game_board[9]).center(SCREEN_WIDTH))
    print("+---+---+---+".center(SCREEN_WIDTH))
    print("|{:^3}|{:^3}|{:^3}|".format(game_board[4], game_board[5], game_board[6]).center(SCREEN_WIDTH))
    print("+---+---+---+".center(SCREEN_WIDTH))
    print("|{:^3}|{:^3}|{:^3}|".format(game_board[1], game_board[2], game_board[3]).center(SCREEN_WIDTH))
    print("+---+---+---+".center(SCREEN_WIDTH))


def draw_message(message: str) -> None:
    """
    Vypíše zprávu pro hráče

    :param message: zpráva
    :return: None
    """
    print(separator)
    print(message.center(SCREEN_WIDTH))
    print(separator)


def main():
    draw_greeting()
    # v listu je schválně o 1 pole víc, aby souhlasily indexy polí s tlačítky čísel
    game_board = ["", "", "x", "", "o", "x", "", "", "", ""]
    draw_board(game_board)
    game_messages = ["Player {} | Please enter your move number: ", "Congratulations, the player {} WON!"]
    # is_player_o() kolečkář začíná
    draw_message("pokuston")


if __name__ == "__main__":
    main()
