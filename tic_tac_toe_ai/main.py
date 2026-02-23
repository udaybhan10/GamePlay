import math
import sys

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # cols
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def print_instructions():
    print("Welcome to Tic-Tac-Toe Against an Unbeatable AI!")
    print("You are 'X', AI is 'O'.")
    print("Positions are numbered 0 to 8 like this:\n")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 \n")

def test_verification():
    # Simulate a scenario where human (X) is about to win
    board = ['X', 'X', ' ',
             ' ', 'O', ' ',
             ' ', ' ', ' ']
    print("Running Verification Test...")
    print("Board State:")
    print_board(board)
    print("X is threatening to win at position 2. AI (O) must block.")
    move = best_move(board)
    board[move] = 'O'
    print("AI plays at position:", move)
    print_board(board)
    
    if move == 2:
        print("✅ VERIFICATION PASSED: AI correctly blocked the human's winning move.")
    else:
        print("❌ VERIFICATION FAILED: AI did not block the human's winning move.")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test_verification()
        return

    print_instructions()
    board = [' '] * 9
    
    while True:
        # Human turn
        try:
            user_input = input("Enter your move (0-8): ")
            user_input = int(user_input)
            if user_input < 0 or user_input > 8 or board[user_input] != ' ':
                print("Invalid move. Space is occupied or out of bounds. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 8.")
            continue
            
        board[user_input] = 'X'
        print(f"You played 'X' at position {user_input}")
        print_board(board)
        
        if check_win(board, 'X'):
            print("Congratulations! You win! (Wait, this shouldn't happen!)")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
            
        # AI turn
        print("AI is thinking...")
        move = best_move(board)
        board[move] = 'O'
        print(f"AI plays 'O' at position {move}")
        print_board(board)
        
        if check_win(board, 'O'):
            print("AI Wins! Better luck next time.")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
