#!/usr/bin/python3

board = [["." for _ in range(7)] for _ in range(6)]

def print_board(board: list[list[str]]):
    for row in board:
        print(" ".join(row))

def in_bounds(x: int, y: int) -> bool:
    if x < 0 or x > 6:
        return False
    if y < 0 or y > 5:
        return False
    return True

def place_piece(board, piece, x):
    if not in_bounds(x, 0):
        print("Out of bounds")

    for y in range(5, -1, -1):
        if board[y][x] == ".":
            board[y][x] = piece
            print(f"Placed at {x},{y}")
            return x, y
    
    print("Column full")

def check_direction(board, piece, x1, x2, y1, y2):
    # Currently only workds for verticals and horizontals
    # Diagonal checks like a 5x5 sqaure for some reason
    # One potential fix is by using a while loop and a xstep and ystep 
    # argument as well

    # x = x1
    # y = y1
    # while x <= x2 and y <= y2:
    #   ...
    #   x += xstep
    #   y += ystep

    num = 0

    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if not in_bounds(x, y):
                continue
            elif board[y][x] == piece:
                num += 1
            else:
                num = 0

            print(x, y)

            if num == 4:
                return True
    
    return False

def check_win(board, piece, x, y):
    """
    return (check_direction(board, piece, x-3, x+3, y, y) or
            check_direction(board, piece, x, x, y-3, y+3) or
            check_direction(board, piece, x-3, x+3, y-3, y+3) or
            check_direction(board, piece, x+3, x-3, y-3, y+3))
    """
    return check_direction(board, piece, x-3, x+3, y-3, y+3)

def main():
    while 1:
        for piece in ("X", "O"):
            print_board(board)
            col = int(input("> "))
            x, y = place_piece(board, piece, col)
            print(check_win(board, piece, x, y))

if __name__ == "__main__":
    main()

