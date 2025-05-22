from collections import deque
import heapq

# Game Board Representation
def initialize_board():
    return [' '] * 9  # 3x3 Tic-Tac-Toe board

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")

def is_winner(board, player):
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def is_draw(board):
    return ' ' not in board and not is_winner(board, 'X') and not is_winner(board, 'O')

# BFS for Game State Exploration
def bfs_tic_tac_toe(start_board, player):
    queue = deque([(start_board, player)])
    visited = set()
    visited.add(tuple(start_board))

    while queue:
        current_board, current_player = queue.popleft()

        if is_winner(current_board, current_player):
            return current_board

        for move in valid_moves(current_board):
            next_board = make_move(current_board, move, current_player)
            if tuple(next_board) not in visited:
                visited.add(tuple(next_board))
                queue.append((next_board, switch_player(current_player)))

    return None

# DFS for Game State Exploration
def dfs_tic_tac_toe(start_board, player):
    stack = [(start_board, player)]
    visited = set()
    visited.add(tuple(start_board))

    while stack:
        current_board, current_player = stack.pop()

        if is_winner(current_board, current_player):
            return current_board

        for move in valid_moves(current_board):
            next_board = make_move(current_board, move, current_player)
            if tuple(next_board) not in visited:
                visited.add(tuple(next_board))
                stack.append((next_board, switch_player(current_player)))

    return None

# A* Search with Heuristic
def heuristic_tic_tac_toe(board, player):
    # Example heuristic: prioritize moves that block opponent's win or lead to victory
    opponent = 'X' if player == 'O' else 'O'
    score = 0
    if is_winner(board, player):
        score += 10
    if is_winner(board, opponent):
        score -= 10
    return score

def a_star_tic_tac_toe(start_board, player):
    pq = []
    heapq.heappush(pq, (0, start_board, player))
    visited = set()
    visited.add(tuple(start_board))

    while pq:
        _, current_board, current_player = heapq.heappop(pq)

        if is_winner(current_board, current_player):
            return current_board

        for move in valid_moves(current_board):
            next_board = make_move(current_board, move, current_player)
            if tuple(next_board) not in visited:
                visited.add(tuple(next_board))
                heuristic_score = heuristic_tic_tac_toe(next_board, current_player)
                heapq.heappush(pq, (-heuristic_score, next_board, switch_player(current_player)))

    return None

# Helper Functions
def valid_moves(board):
    return [i for i in range(len(board)) if board[i] == ' ']

def make_move(board, position, player):
    new_board = board[:]
    new_board[position] = player
    return new_board

def switch_player(player):
    return 'O' if player == 'X' else 'X'

# Compare Algorithms
def compare_algorithms():
    board = initialize_board()
    print("Initial Board:")
    display_board(board)

    print("\nBFS:")
    bfs_result = bfs_tic_tac_toe(board, 'X')
    display_board(bfs_result)

    print("\nDFS:")
    dfs_result = dfs_tic_tac_toe(board, 'X')
    display_board(dfs_result)

    print("\nA* Search:")
    astar_result = a_star_tic_tac_toe(board, 'X')
    display_board(astar_result)

compare_algorithms()
