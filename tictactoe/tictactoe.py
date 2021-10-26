"""
Tic Tac Toe Player
"""
import math
import sys
sys.setrecursionlimit(100000)

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
    if sum(x.count('X') for x in board) == sum(x.count('O') for x in board):
        return "X"
    return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    output = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(board[i][j])
        output.append(temp)

    output[action[1]][action[1]] = player(board)
    return output


def winner(board):
    """
    Returns the winner of the game, if there is one.

    for i in range(3):
        try:
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
        except:
            print(i)

    if board[0][0] == board[1][1] == board[1][1]:
        return board[1][1]
    elif board[0][1] == board[1][1] == board[2][0]:
        return board[0][2]
    return False
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "0":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    for action in actions(board):
        test = calcValue(result(board, action))
        best_value = 10
        if test < best_value:
            best_value = test
            best_action = action
    return (1, 1)
    """
    print(actions(board)[0])
    return(actions(board)[0])


def calcValue(board):
    if terminal(board):
        return utility(board)
    for action in actions(board):
        test = calcValue(result(board, action))
        if test < 0:
            best_value = test
    return best_value
