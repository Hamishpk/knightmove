import math

board = [[0, 1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29, 30, 31],
        [32, 33, 34, 35, 36, 37, 38, 39],
        [40, 41, 42, 43, 44, 45, 46, 47],
        [48, 49, 50, 51, 52, 53, 54, 55],
        [56, 57, 58, 59, 60, 61, 62, 63]]


def getsquares(square):
    row = math.floor(square/8)
    col = square % 8
    connections = []
    moves = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]

    for i in moves:

        if row + i[0] >= 0 and row + i[0] < 8 and col + i[1] >= 0 and col + i[1] < 8:
            connections.append(board[row + i[0]][col + i[1]])

    return connections

def bfs(src, dest):
    moves = [-1] * 64
    visited = [False] * 64

    queue = []
    queue.append(src)
    visited[src] = True
    moves[src] = 0

    while queue:
        node = queue.pop(0)
        connections = getsquares(node)
        for i in connections:
            if visited[i] == False:
                queue.append(i)
                moves[i] = moves[node] + 1
                visited[i] = True

    return moves[dest]


print(bfs(0, 0))
