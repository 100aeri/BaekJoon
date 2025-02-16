import sys

n, m = list(map(int, input().split()))
board = [list(input()) for _ in range(n)]
chess_w = [['W' if (i+j)%2==0 else 'B' for i in range(8)] for j in range(8)]
chess_b = [['B' if (i+j)%2==0 else 'W' for i in range(8)] for j in range(8)]
min_paint = sys.maxsize

# def repaint(lst):
#     repaints_w, repaints_b = 0, 0
#     for i in range(8):
#         for j in range(8):
#             if lst[i][j] != chess_w[i][j]: repaints_w += 1
#             if lst[i][j] != chess_b[i][j]: repaints_b += 1
#     return min(repaints_w, repaints_b)

# for i in range(n-7):
#     for j in range(m-7):
#         cutted_board = []
#         for ii in range(i, i+8):
#             cutted_board.append(board[ii][j:j+8])
#         min_paint = min(min_paint, repaint(cutted_board))

for i in range(n-7):
    for j in range(m-7):
        repaints_w, repaints_b = 0, 0

        for ii in range(8):
            for jj in range(8):
                if board[i+ii][j+jj] != chess_w[ii][jj]: repaints_w += 1
                if board[i+ii][j+jj] != chess_b[ii][jj]: repaints_b += 1

        min_paint = min(min_paint, repaints_w, repaints_b)

print(min_paint)        