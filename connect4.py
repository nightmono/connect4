#!/usr/bin/python3

def print_board(board: list[list[str]]):
    for row in board:
        print(" ".join(row).replace(".", "--").replace("X", "\033[1;31m██\033[0m").replace("O", "\033[1;33m██\033[0m"))

def in_bounds(x: int, y: int) -> bool:
    return x >= 0 and x <= 6 and y >= 0 and y <= 5

def place_piece(board, piece, x):
    if not in_bounds(x, 0):
        print("Out of bounds")
        return -1, -1

    for y in range(5, -1, -1):
        if board[y][x] == ".":
            board[y][x] = piece
            return x, y
    
    print("Column full")
    return -1, -1

def check_direction(board, piece, x1, x2, xstep, y1, y2, ystep):
    num = 0

    x = x1
    y = y1
    while x != x2 and y != y2:
        if not in_bounds(x, y):
            pass
        elif board[y][x] == piece:
            num += 1
        else:
            num = 0

        if num == 4:
            return True

        x += xstep
        y += ystep

    return False

def check_win(board, piece, x, y):
    return (check_direction(board, piece, x-3, x+4, 1, y, y+1, 0) or
            check_direction(board, piece, x, x+1, 0, y-3, y+4, 1) or
            check_direction(board, piece, x-3, x+4, 1, y-3, y+4, 1) or
            check_direction(board, piece, x-3, x+4, 1, y+3, y-4, -1))

def start_game():
    board = [["." for _ in range(7)] for _ in range(6)]
    game_running = True
    
    while game_running:
        for piece in ("X", "O"):
            print_board(board)
            col = int(input("> "))
            x, y = place_piece(board, piece, col)
            if check_win(board, piece, x, y):
                print(f"Player {piece} wins!")
                print_board(board)
                game_running = False
                break
            print()

def main():
    start_game()

if __name__ == "__main__":
    main()

