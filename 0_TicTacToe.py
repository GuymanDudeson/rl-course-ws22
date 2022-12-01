import random
import time

boardSize = 3
game_state = ["_" for i in range(0, 9)]
validPositions = [i for i in range(0, 9)]


def print_board():
    start = time.time()
    for i in range(boardSize):
        print(game_state[i * boardSize : (i+1) * boardSize])
    end = time.time()
    print("print_board took:",str(end - start))

def print_valid_moves():
    start = time.time()

    board = ""
    for index, state in enumerate(game_state):
        board += "---" if state != "_" else str(index).zfill(3)
        if (index + 1) % boardSize == 0:
            print("[", board, "]")
            board = ""
        else:
            board += ","

    end = time.time()
    print("print_valid_moves took:", str(end - start))


def update_board(position, symbol):
    if position < 0 or position > boardSize * boardSize or game_state[position] != "_":
        print("Position is invalid, please enter a valid position")
        return
    game_state[position] = symbol
    validPositions.remove(position)


def game_finished(position):
    start = time.time()


    symbol = game_state[position]
    win_string = str(symbol) + str(symbol) + str(symbol)

    #Empty spaces to the left
    leftBound = position - min(2, position % boardSize)
    #Empty spaces to the right
    rightBound = position + min(2, boardSize - 1 - (position % boardSize))
    check_string = ''.join([i for i in game_state[leftBound: rightBound + 1]])
    if win_string in check_string:
        print(symbol + "wins")
        return True

    check_string = ""
    for index in range(-2, 3):
        #Get the value of the upper 2, the position itself and the lower two spaces
        game_state_index = position + (boardSize * index)
        check_string += game_state[game_state_index] if boardSize * boardSize > game_state_index >= 0 else "_"
    if win_string in check_string:
        print(symbol + "wins")
        return True

    check_string = ""
    for index in range(-2, 3):
        # Get the value of the upper left 2, the position itself and the lower right two spaces of the diagonal
        game_state_index = position + (boardSize * index) + index
        check_string += game_state[game_state_index] if boardSize * boardSize > game_state_index >= 0 else "_"
    if win_string in check_string:
        print(symbol + "wins")
        return True

    check_string = ""
    for index in range(-2, 3):
        # Get the value of the upper right 2, the position itself and the lower left two spaces of the diagonal
        game_state_index = position + (boardSize * index) - index
        check_string += game_state[game_state_index] if boardSize * boardSize > game_state_index >= 0 else "_"
    if win_string in check_string:
        print(symbol + "wins")
        return True

    if "_" not in game_state:
        print("Draw")
        return True

    end = time.time()
    print("game_finished took:", str(end - start))

    return False


if __name__ == "__main__":
    print("Welcome to TicTacToe!")

    while True:
        try:
            j = int(input("Bitte geben Sie die Board Größe an"))
            if 10000 > j < 3:
                print("Board has to be at least 3 big")
            else:
                boardSize = j
                break
        except ValueError:
            print("Bitte eine Zahl zwischen 3-100 eingeben")

    game_state = ["_" for i in range(0, boardSize * boardSize)]
    validPositions = [i for i in range(0, boardSize * boardSize)]

    player = True

    while True:
        print_board()
        symbol = "X" if player else "O"

        if player:
            print("You can put your 'x' at the following positions:")
            print_valid_moves()

        while True:
            try:
                i = int(input("Where do you want to put your '" + symbol + "'? (0-" + str(boardSize * boardSize) + ")")) if player else validPositions[random.randrange(len(validPositions))]
                break
            except ValueError:
                print("Bitte eine Zahl zwischen 0-8 eingeben")
        update_board(i, symbol)

        if game_finished(i):
            break

        player = not player

