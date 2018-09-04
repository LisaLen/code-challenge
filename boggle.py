#!/usr/bin/python

def make_board(str):
    board = list()
    row = -1
    for c in str:
        if c == " ":
            continue
        if c == "\n":
            row += 1
            board.append(list())
        else:
            board[row].append(c)
    return board

def neighbors(board, cell):
    n = list()
    x = cell[0]
    y = cell[1]
    if x > 0:
        n.append((x-1, y))   # WEST
    if x + 1 < len(board):
        n.append((x+1, y))   # EAST
    if y > 0:
        n.append((x, y-1))   # NORTH
    if y + 1 < len(board[0]):
        n.append((x, y+1))   # SOUTH
    return n

class Found(Exception):
    pass

def find_step(board, word, cell, path):
    # print(word, cell, path)

    if cell in path:
        return  # we have been here

    x = cell[0]
    y = cell[1]

    if not word:
        raise Found() # we are done!

    if word[0] != board[x][y]:
        return # no luck

    path.append(cell)

    for n in neighbors(board, cell):
        find_step(board, word[1:], n, path)

    path.pop()

    return  # we checked everything - not found
        
def find(board, word):
    path = list()
    try:
        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                find_step(board, word, (x, y), path)
    except:
        # print "FOUND!!!"
        pass
    return path

def path2str(p):
    if not p:
        return "Not found"
    t = p[0]
    s = "(" + str(t[0]) + "," + str(t[1])
    for t in p[1:]:
        s += " -> " + str(t[0]) + "," + str(t[1])
    s += ")"
    return s

board = make_board('''
  N C A N E
  O U I O P
  Z Q Z O N
  F A D P L
  E D E A Z
''')

words = ["NOON", "CANON", "POOP", "LIZA", "QUIZ"]

for w in words:
    print w + ": " + path2str(find(board, w))

# (0,3 -> 1,3 -> 2,3 -> 2,4) 

    
