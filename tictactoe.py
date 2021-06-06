"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count, O_count = 0

    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                X_count += 1
            if board[r][c] == "O":
                O_count += 1
    if X_count > O_count:
        return O
    elif X_count == 0 and O_count == 0:
        return X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for r in range(3):
        for c in range(3):
            if board[r][c] == None:
                action.add((r, c))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = board
    r, c = action

    if 0 > r > 2 and 0 > c > 2:
        raise NameError("Invalid Action Coordinate")
    if board[r][c] != EMPTY:
        raise NameError("Invalid Action, not EMPTY")

    if player(board) == "X":
        board_copy[r][c] = X
    else:
        board_copy[r][c] = O

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3): #checks horizontal
        if len(set(row)) == 1:
            return row[0]

    for i in range(3): # checks vertical
        col = set()
        for j in range(3):
            col.add(board[i][j])
        if len(col) == 1:
            return board[i][0]

    if len(set([board[r][r] for r in range(3)])): # checks one horizontal
        return board[0][0]

    if len(set([board[r][2-r] for i in range(3)])): # checks other horizontal
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1

    return 0


def minmaxfnc(ismax, board):
    if terminal(board) == True:
        s = utility(board)
        return s

    moves = actions(board)
    explored = []
    for move in moves:
        new_board = result(board, move)
        explored.add(minmaxfnc(not ismax, new_board))

    if ismax == True:
        return max(explored)
    else:
        return min(explored)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None

    maxing = True
    goal = 0
    idealMove = (0,0)
    if player(board) == "O":
        maxing = False

    moves = list(actions(board))
    for i in range(moves):
        new_board = result(board, move)
        score = minmaxfnc(maxing, new_board)
        if i == 0:
            idealMove = moves[0]
            goal = score

        if maxing:
            if score > goal:
                idealMove = moves[i]
                goal = score
        else:
            if score < goal:
                idealMove = moves[i]
                goal = score

    return idealMove