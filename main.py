SCREEN_WIDTH = 45
SEPARATOR = "=" * SCREEN_WIDTH

def draw_greeting() -> None:
    """
    Vypíše úvodní pozdrav a pravidla hry.

    :return: None
    """
    print()
    print("Welcome to Tic Tac Toe")
    print(SEPARATOR)
    print("GAME RULES:".center(SCREEN_WIDTH))
    print("""Each player can place one mark (or stone)
per turn on the 3x3 grid. 
Numbers of fields is as NumPad numbers:""")
    draw_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("""The WINNER is who succeeds in placing three of 
their marks in a:
* horizontal,
* vertical or
* diagonal row""")
    print(SEPARATOR)
    print("Let's start the game".center(SCREEN_WIDTH))
    print(SEPARATOR)


def draw_board(game_board: list) -> None:
    """
    Vykreslí aktuální stav hrací plochy.

    :return: None
    """
    table_line = "+---+---+---+".center(SCREEN_WIDTH)
    print(table_line)
    print("|{:^3}|{:^3}|{:^3}|".format(game_board[6], game_board[7], game_board[8]).center(SCREEN_WIDTH))
    print(table_line)
    print("|{:^3}|{:^3}|{:^3}|".format(game_board[3], game_board[4], game_board[5]).center(SCREEN_WIDTH))
    print(table_line)
    print("|{:^3}|{:^3}|{:^3}|".format(game_board[0], game_board[1], game_board[2]).center(SCREEN_WIDTH))
    print(table_line)


def draw_message(message: str) -> None:
    """
    Vypíše zprávu pro hráče

    :param message: zpráva
    :return: None
    """
    print(SEPARATOR)
    print(message, end="")


def is_win(player: str, game_board: list, win_lines: list) -> bool:
    """
    Kontroluje, jestli hráč docílil výherní kombinaci.

    :param player: aktuální hráč
    :param game_board: herní deska
    :param win_lines: list výherních kombinací
    :return: True pokud je dosaženo výherní kombinace.
    """
    result = False
    for line in win_lines:
        if game_board[line[0]] == game_board[line[1]] == game_board[line[2]] == player:
            result = True
    return result


def is_board_full(game_board: list) -> bool:
    """Vrací True pokud je hrací deska plná."""
    return "" not in game_board


def place_mark(player_mark: str, game_board: list) -> list:
    """
    place_mark("o", ["", "x", "", "", "o", "", "", "", ""])
    Vloží značku aktivního hráče na hrací desku.

    :param player_mark: značka hráče
    :param game_board: hrací deska
    :return: aktualizovaná hrací deska
    """
    while True:
        field_number = input()
        check_message = check_mark(field_number, game_board)
        if check_message == "ok":
            break
        print(check_message, end="")

    game_board[int(field_number) - 1] = player_mark
    return game_board


def check_mark(field_number, game_board: list) -> str:
    """
    Kontroluje, jestli je možné hráčovu značku umístit na zvolené místo.

    :param field_number: číslo pole hrací desky
    :param game_board: hrací deska
    :return: zpráva o výsledku kontroly
    """
    result = "ok"
    if not field_number.isdecimal() or int(field_number) not in range(1, 10):
        result = "Your move number must be in range 1 - 9!\nTry again: "
    elif game_board[int(field_number) - 1] != "":
        result = "Selected field is occupied already!\nSelect another number:  "
    return result


def main():
    draw_greeting()
    game_board = ["", "", "", "", "", "", "", "", ""]
    win_lines = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]
    draw_board(game_board)
    actual_player = "o"

    while True:
        draw_message(f"Player {actual_player} | Please enter your move number: ")
        place_mark(actual_player, game_board)
        print(SEPARATOR)
        draw_board(game_board)
        if is_win(actual_player, game_board, win_lines):
            draw_message(f"Congratulations, the player {actual_player} WON!")
            break
        elif is_board_full(game_board):
            draw_message(f"Game board is full. Draw!")
            break

        if actual_player == "o":
            actual_player = "x"
        else:
            actual_player = "o"


if __name__ == "__main__":
    main()
