##
## EPITECH PROJECT, 2024
## command.py
## File description:
## command
##

def about(self, command):
    print("DEBUG: Received ABOUT command", flush=True)
    print("name=\"Gomoku\", version=\"1.0\", author=\"Lucas, Eliot, Arslan\", country=\"France\"", flush=True)
    return (True)

def start(self, command):
    print(f"DEBUG: Received START command with args: {command}", flush=True)
    if len(command) != 2:
        print("ERROR: START Too much arguments or not enough", flush=True)
        return (False)
    try:
        start_board_size = int(command[1])
        print(f"DEBUG: Parsed board size: {start_board_size}", flush=True)
        if start_board_size <= 0:
            print("ERROR: start_board_size must be a positive integer")
            return (False)
        self.width = self.height = start_board_size
        self._board = [[self.VOID] * start_board_size for _ in range(start_board_size)]
        print("DEBUG: Board initialized", flush=True)
        print("OK - everything is good", flush=True)
        return (True)
    except ValueError as e:
        print(f"ERROR: START Invalid board size ({e})", flush=True)
        return (False)

def info(self, command):
    print(f"DEBUG: Received INFO command with args: {command}", flush=True)
    if len(command) != 3:
        print("ERROR: INFO Invalid arguments", flush=True)
        return (False)
    key, value = command[1], command[2]
    if not key or not value:
        print("ERROR: INFO Invalid key or value", flush=True)
        return (False)
    self._info[key] = value
    print(f"INFO: Set {key} to {value}", flush=True)
    return (True)

def rectstart(self, command):
    print("DEBUG: RECTSTART Command received:", command, flush=True)
    if len(command) < 2:
        print("ERROR: RECTSTART Missing dimensions", flush=True)
        return (False)
    try:
        width, height = map(int, command[1].split(','))
        print("DEBUG: RECTSTART Dimensions received:", width, height, flush=True)
        if width <= 0 or height <= 0:
            print("ERROR: RECTSTART Invalid size (must be positive integers)", flush=True)
            return (False)
        print("DEBUG: RECTSTART Initializing board with dimensions", width, height, flush=True)
        self.width = width
        self.height = height
        self._board = [[self.VOID for _ in range(self.width)] for _ in range(self.height)]
        self._turn = 0
        print("DEBUG: RECTSTART Board initialized successfully", flush=True)
        print("OK", flush=True)
        return (True)
    except ValueError:
        print("ERROR: RECTSTART Invalid input (not numbers)", flush=True)
        return (False)
    except Exception as e:
        print(f"ERROR: RECTSTART Unexpected error: {e}", flush=True)
        return (False)
    
def play(self, command):
    print("DEBUG: PLAY Command received:", command, flush=True)
    if len(command) < 2:
        print("ERROR: PLAY Missing position", flush=True)
        return (False)
    try:
        x, y = map(int, command[1].split(','))
        print("DEBUG: PLAY Coordinates received:", x, y, flush=True)
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("ERROR: PLAY Invalid position it's out of board", flush=True)
            return (False)
        if self._board[x][y] != self.VOID:
            print("ERROR: PLAY Invalid position it's already taken", flush=True)
            return (False)
        print("DEBUG: PLAY Placing marker at position", x, y, flush=True)
        self._board[x][y] = self.MATE
        self._turn += 1
        print("DEBUG: PLAY Move registered, turn updated to", self._turn, flush=True)
        print(f"{x},{y}", flush=True)
        return (True)
    except ValueError:
        print("ERROR: PLAY Invalid position (not a number)", flush=True)
        return (False)
    except IndexError:
        print("ERROR: PLAY Invalid position (out of board range)", flush=True)
        return (False)
    except Exception as e:
        print(f"ERROR: PLAY Unexpected error: {e}", flush=True)
        return (False)
    
def restart(self, command):
    print("DEBUG: RESTART Command received:", command, flush=True)
    if not hasattr(self, 'width') or not hasattr(self, 'height'):
        print("ERROR: RESTART Board dimensions not set", flush=True)
        return    
    print("DEBUG: RESTART Resetting the board", flush=True)
    self._board = [[self.VOID for _ in range(self.width)] for _ in range(self.height)]
    self._turn = 0
    self._info.clear()
    print("DEBUG: RESTART Board reset complete", flush=True)
    print("OK", flush=True)

def takeback(self, command):
    print("DEBUG: TAKEBACK Command received:", command, flush=True)
    if len(command) < 2:
        print("ERROR: TAKEBACK Missing position", flush=True)
        return (False)
    try:
        x, y = map(int, command[1].split(','))
        print("DEBUG: TAKEBACK Coordinates received:", x, y, flush=True)
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("ERROR: TAKEBACK Invalid position (out of board range)", flush=True)
            return (False)
        if self._board[x][y] == self.VOID:
            print("ERROR: TAKEBACK Position already empty", flush=True)
            return (False)
        print(f"DEBUG: TAKEBACK Removing marker at position ({x},{y})", flush=True)
        self._board[x][y] = self.VOID
        self._turn -= 1
        print("DEBUG: TAKEBACK Move undone, turn updated to", self._turn, flush=True)
        print("OK", flush=True)
        return (True)
    except ValueError:
        print("ERROR: TAKEBACK Invalid position (not numbers)", flush=True)
        return (False)
    except IndexError:
        print("ERROR: TAKEBACK Invalid position (out of board range)", flush=True)
        return (False)
    except Exception as e:
        print(f"ERROR: TAKEBACK Unexpected error: {e}", flush=True)
        return (False)

def display(self, command):
    print("DEBUG: DISPLAY Board state requested", flush=True)
    header = '     ' + '  '.join(f"{i}" for i in range(self.width))
    print(header, flush=True)
    print('   ' + '-' * (3 * self.width + 1), flush=True)
    for idx, row in enumerate(self._board):
        print(f"{idx:2} | " + '  '.join(str(cell) for cell in row), flush=True)
    print("DEBUG: DISPLAY Complete", flush=True)

def begin(self, command):
    print("DEBUG: BEGIN Command received", flush=True)
    self.VOID = 0
    self.OPPS = 2
    self.MATE = 1
    self._turn += 1
    result = self.exec_algo()
    return (result)

def turn(self, command):
    print("DEBUG: TURN Command received", flush=True)
    pos = command[1]
    try:
        width, height = map(int, pos.split(','))
        if not (0 <= width < self.width and 0 <= height < self.height):
            print(f"ERROR: TURN Invalid position ({width}, {height}) - Out of bounds", flush=True)
            return False
        if self._board[width][height] != self.VOID:
            print(f"ERROR: TURN Invalid position ({width}, {height}) - Already taken", flush=True)
            return False
        self._board[width][height] = self.OPPS
        self._turn += 1
        print(f"DEBUG: TURN Move applied at ({width}, {height}), Turn incremented to {self._turn}", flush=True)
        result = self.exec_algo()
        return (result)
    except ValueError as e:
        print(f"ERROR: TURN Invalid position format ({e})", flush=True)
        return (False)
    except Exception as e:
        print(f"ERROR: TURN Unexpected error: {e}", flush=True)
        return (False)

def board(self, command):
    print(f"DEBUG: BOARD Command received with args: {command}", flush=True)
    try:
        while True:
            line = input().strip()
            if line == "DONE":
                break
            x, y, tile = map(int, line.split(','))
            print(f"DEBUG: BOARD Parsed line: x={x}, y={y}, tile={tile}", flush=True)
            if not (0 <= x < self.width and 0 <= y < self.height and tile in [self.VOID, self.MATE, self.OPPS]):
                print("ERROR: BOARD Invalid position or tile value", flush=True)
                return (False)
            self._board[x][y] = tile
            print(f"DEBUG: BOARD Updated position ({x}, {y}) to {tile}", flush=True)
        self._turn += 1
        print(f"DEBUG: BOARD Update complete. Current turn: {self._turn}", flush=True)
        return self.exec_algo()
    except ValueError:
        print("ERROR: BOARD Invalid input format (must be x,y,tile)", flush=True)
        return (False)
    except Exception as e:
        print(f"ERROR: BOARD Unexpected error: {e}", flush=True)
        return (False)
