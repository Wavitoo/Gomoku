import time
from gomoku_board_eval import compute_score_difference

def has_adjacent_non_empty_cell(board: list, col: int, row: int) -> bool:
    rows, cols = len(board), len(board[0])
    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (-1, -1), (1, 1),
        (-1, 1), (1, -1)
    ]
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != 0:
            return (True)
    return (False)

def get_priority_moves(board: list, player_symbol: int, opponent_symbol: int) -> list:
    priority_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                if has_adjacent_non_empty_cell(board, col, row):
                    priority_moves.append((row, col))
    priority_moves.sort(key=lambda move: evaluate_move_potential(board, move[0], move[1], player_symbol, opponent_symbol), reverse=True)
    return (priority_moves)

def evaluate_move_potential(board: list, row: int, col: int, player_symbol: int, opponent_symbol: int) -> int:
    score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dx, dy in directions:
        score += count_consecutive_stones(board, row, col, dx, dy, player_symbol)
        score -= count_consecutive_stones(board, row, col, dx, dy, opponent_symbol)
    return (score)

def count_consecutive_stones(board: list, row: int, col: int, dx: int, dy: int, symbol: int) -> int:
    count = 0
    while 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == symbol:
        count += 1
        row += dx
        col += dy
    return (count)

def algo_a_b(board: list, prof: int, is_maximizing_player: bool, player_symbol: int, opponent_symbol: int, a: int, b: int, time_limit: int, start_time: int) -> int:
    if prof == 0:
        return (compute_score_difference(board, player_symbol, opponent_symbol))
    possible_moves = get_priority_moves(board, player_symbol, opponent_symbol)
    best_score = -float('inf') if is_maximizing_player else float('inf')
    for row, col in possible_moves:
        if board[row][col] == 0:
            board[row][col] = player_symbol if is_maximizing_player else opponent_symbol
            score = algo_a_b(board, prof - 1, not is_maximizing_player, player_symbol, opponent_symbol, a, b, time_limit, start_time)
            board[row][col] = 0
            if is_maximizing_player:
                best_score = max(best_score, score)
                a = max(a, best_score)
                if b <= a:
                    return (best_score) 
            else:
                best_score = min(best_score, score)
                b = min(b, best_score)
                if b <= a:
                    return (best_score)
            elapsed_time = (time.time() * 1000) - start_time
            if elapsed_time > time_limit * 0.9:
                return (best_score)
    return (best_score)

def extract_5x5_subboard(board, center_x, center_y):
    rows, cols = len(board), len(board[0])
    subboard = [[0 for _ in range(5)] for _ in range(5)]
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            sub_x, sub_y = center_x + dx, center_y + dy
            if 0 <= sub_x < rows and 0 <= sub_y < cols:
                subboard[dx + 2][dy + 2] = board[sub_x][sub_y]
    return (subboard)

def calculate_distance_to_center(pos_x, pos_y, game_board):
    height, width = len(game_board), len(game_board[0])
    mid_x, mid_y = height // 2, width // 2
    horizontal_gap = pos_x - mid_x if pos_x > mid_x else mid_x - pos_x
    vertical_gap = pos_y - mid_y if pos_y > mid_y else mid_y - pos_y
    return (horizontal_gap + vertical_gap)
