##
## EPITECH PROJECT, 2024
## AI.py
## File description:
## AI
##

import time
from math import inf
from Algo import extract_5x5_subboard, algo_a_b, calculate_distance_to_center

class AI:
    def __init__(self):
        self._turn = 0
        self.width = 0
        self.height = 0
        self._board = []
        self._info = {}
        self._info["timeout_turn"] = 5000
        self.VOID = 0
        self.MATE = 1
        self.OPPS = 2

    from commands.command import about, start, info, rectstart, play, restart, takeback, display, turn, board, begin

    def parsing(self, command):
        print(f"MESSAGE Command Received {command}", flush=True)
        command_list = {

            "ABOUT": self.about,
            "START": self.start,
            "INFO": self.info,
            "PLAY": self.play,
            "TAKEBACK": self.takeback,
            "RECTSTART": self.rectstart,
            "RESTART": self.restart,
            "DISPLAY": self.display,
            "BEGIN": self.begin,
            "BOARD": self.board,
            "TURN": self.turn
        }
        command_func = command_list.get(command[0])
        if command_func:
            return command_func(command)
        print("ERROR Unknown command", flush=True)
        return (False)

    def exec_algo(self):
        best_position = (self.width // 2, self.height // 2)
        current_time = int(time.time() * 1000)
        optimal_value = -inf
        move_found = False
        for row in range(self.width):
            for col in range(self.height):
                if self._board[row][col] == self.VOID:
                    subboard = extract_5x5_subboard(self._board, row, col)
                    occupied_count = sum(1 for subrow in subboard for cell in subrow if cell in [self.MATE, self.OPPS])
                    if occupied_count > 0:
                        self._board[row][col] = self.MATE
                        move_value = algo_a_b(
                            self._board,
                            prof=1,
                            is_maximizing_player=False,
                            player_symbol=self.MATE,
                            opponent_symbol=self.OPPS,
                            a=-inf,
                            b=inf,
                            time_limit=int(self._info["timeout_turn"]),
                            start_time=current_time
                        )
                        self._board[row][col] = self.VOID
                        is_better_value = move_value > optimal_value
                        is_closer_to_center = (
                            move_value == optimal_value and 
                            calculate_distance_to_center(row, col, self._board) < calculate_distance_to_center(best_position[0], best_position[1], self._board)
                        )
                        if is_better_value or is_closer_to_center or not move_found:
                            optimal_value = move_value
                            best_position = (row, col)
                            move_found = True
        if not move_found:
            print("MESSAGE No move found", flush=True)
        print(f"{best_position[0]},{best_position[1]}", flush=True)
        self._board[best_position[0]][best_position[1]] = self.MATE
        return (True)
