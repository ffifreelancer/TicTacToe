board = [" "]*10
is_gameover = False
win_condition = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
turn_count = 0
player = ["X", "O"]
move = 1

def draw_board():
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])
    return

def fill_board():
    board[move] = player[turn_count%2]
    draw_board()
    return

def is_win():
    for i in range(len(win_condition)):
        if (board[win_condition[i-1][0]] == board[win_condition[i-1][1]] == board[win_condition[i-1][2]]) and  board[win_condition[i-1][2]] != " ":
            print(player[turn_count % 2] + ' win!')
            return True

def is_draw():
    if turn_count == 9:
        print("it's a draw!")
        return True

print("Welcome to TicTacToe! You are X. Here is the board:")
draw_board()
while True:
    move = int(input("What is your move?(1-9)"))
    fill_board()
    if is_win() == True:

        break
    if is_draw() == True:
        print("It's a draw!")
        break
    turn_count += 1

x = input("thanks for playing")








