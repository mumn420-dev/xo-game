import random
import time

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, mark):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    return any(board[a] == mark and board[b] == mark and board[c] == mark for a, b, c in win_conditions)

def is_full(board):
    return all(spot in ['X', 'O'] for spot in board)

def get_bot_move(board, bot_mark):
    human_mark = 'O' if bot_mark == 'X' else 'X'
    
    # 1. Check if bot can win in the next move
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = bot_mark
            if check_win(board, bot_mark):
                board[i] = str(i + 1)
                return i
            board[i] = str(i + 1)
            
    # 2. Check if human can win in the next move, and block them
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = human_mark
            if check_win(board, human_mark):
                board[i] = str(i + 1)
                return i
            board[i] = str(i + 1)
            
    # 3. Take center if available
    if board[4] == '5':
        return 4
        
    # 4. Take random available spot
    available_moves = [i for i, spot in enumerate(board) if spot not in ['X', 'O']]
    return random.choice(available_moves)

def get_human_move(board, mark):
    while True:
        try:
            move = int(input(f"Player {mark}, choose position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                return move
            else:
                print("Invalid move! Spot already taken or out of range. Try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def play_game(mode):
    # mode: 1 = Human vs Human, 2 = Human vs Bot, 3 = Bot vs Bot
    board = [str(i + 1) for i in range(9)]
    current_mark = 'X'
    
    print_board(board)
    
    while True:
        if mode == 1: # Human vs Human
            move = get_human_move(board, current_mark)
        elif mode == 2: # Human vs Bot
            if current_mark == 'X':
                move = get_human_move(board, current_mark)
            else:
                print(f"Bot (O) is thinking...")
                time.sleep(0.6) # Brief pause for realism
                move = get_bot_move(board, 'O')
        else: # Bot vs Bot
            print(f"Bot ({current_mark}) is thinking...")
            time.sleep(0.6)
            move = get_bot_move(board, current_mark)
            
        board[move] = current_mark
        print_board(board)
        
        if check_win(board, current_mark):
            if mode == 3:
                print(f"🎉 Bot ({current_mark}) wins!\n")
            elif mode == 2:
                if current_mark == 'X':
                    print("🎉 Congratulations! You (X) win!\n")
                else:
                    print("🤖 Bot (O) wins! Better luck next time.\n")
            else:
                print(f"🎉 Player {current_mark} wins!\n")
            break
            
        if is_full(board):
            print("It's a tie!\n")
            break
            
        current_mark = 'O' if current_mark == 'X' else 'X'

def main():
    while True:
        print("=== WELCOME TO TIC-TAC-TOE ===")
        print("1. Human vs Human")
        print("2. Human vs Bot")
        print("3. Bot vs Bot")
        print("4. Exit")
        
        choice = input("Select game mode (1-4): ").strip()
        
        if choice == '1':
            play_game(1)
        elif choice == '2':
            play_game(2)
        elif choice == '3':
            play_game(4)  # Pass mode 3 setup
            play_game(3)
        elif choice == '4':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
