##
## EPITECH PROJECT, 2024
## gomoku_board_eval.py
## File description:
## gomoku board score evaluation
##

from math import inf

def evaluate_line(board, x, y, dx, dy, player, opponent, equivalent_scores):
    line_length = 1
    multiplier = 0
    board_height, board_width = len(board), len(board[0])
    prev_x, prev_y = x - dx, y - dy
    if 0 <= prev_x < board_height and 0 <= prev_y < board_width:
        if board[prev_x][prev_y] == player:
            return (0)
        elif board[prev_x][prev_y] != opponent:
            multiplier += 1
    for i in range(1, 6):
        next_x, next_y = x + i * dx, y + i * dy
        if not (0 <= next_x < board_height and 0 <= next_y < board_width):
            break
        if board[next_x][next_y] != player:
            break
        line_length += 1
    next_x, next_y = x + line_length * dx, y + line_length * dy
    if 0 <= next_x < board_height and 0 <= next_y < board_width:
        if board[next_x][next_y] != opponent:
            multiplier += 1
    score = equivalent_scores[multiplier][line_length]
    return (score) if score != inf else inf

def evaluate_position(board, x, y, player, opponent, equivalent_scores):
    total_score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dx, dy in directions:
        line_score = evaluate_line(board, x, y, dx, dy, player, opponent, equivalent_scores)
        if line_score == inf:
            return (inf)
        total_score += line_score
    return (total_score)

def evaluate_board_score(board, player, opponent):

    total_score = 0
    equivalent_scores = [[0, 0, 0, 0, 0, inf],
                         [0, 1, 4, 16, 64, inf],
                         [0, 2, 8, 32, 1000, inf]]
    board_height, board_width = len(board), len(board[0])
    try:
        for x in range(board_height):
            for y in range(board_width):
                if board[x][y] == player:
                    position_score = evaluate_position(board, x, y, player, opponent, equivalent_scores)
                    if position_score == inf:
                        return (inf)
                    total_score += position_score
    except Exception as error:
        print(f"ERROR error: {error}", flush=True)
    return (total_score)

def compute_score_difference(board, player, opponent):
    player_total_score = 0
    opponent_total_score = 0
    player_score = evaluate_board_score(board, player, opponent)
    if player_score == inf:
        player_total_score = inf
    else:
        player_total_score = player_score
    opponent_score = evaluate_board_score(board, opponent, player)
    if opponent_score == inf:
        opponent_total_score = inf
    else:
        opponent_total_score = opponent_score
    return (player_total_score - opponent_total_score)