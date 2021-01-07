# author: Reed Warren
# date: December 8, 2020
# file: board.py is used tictac.py
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        # the winner's sign O or X
        self.winner = ""

    def get_size(self):
        # optional, return the board size (an instance size)
        return self.size

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        bore = self.board
        win_con = [[bore[0], bore[1], bore[2]], [bore[3], bore[4], bore[5]], [bore[6], bore[7], bore[8]],
                   [bore[0], bore[3], bore[6]], [bore[1], bore[4], bore[7]], [bore[2], bore[5], bore[8]],
                   [bore[0], bore[4], bore[8]], [bore[2], bore[4], bore[6]]]
        if ['X', 'X', 'X'] in win_con:
            return 'X'
        if ['O', 'O', 'O'] in win_con:
            return 'O'

    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        self.board[cell] = sign

    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        if self.board[cell] == self.sign:
            return True

    def isdone(self):
        done = False
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        if self.get_winner() == 'X' or self.get_winner() == 'O' or not self.sign in self.board:
            done = True
        return done


    def show(self):
        bore = self.board
        # draw the board
        print(f'''
   A   B   C 
 +---+---+---+
1| {bore[0]} | {bore[1]} | {bore[2]} |
 +---+---+---+
2| {bore[3]} | {bore[4]} | {bore[5]} |
 +---+---+---+
3| {bore[6]} | {bore[7]} | {bore[8]} |
 +---+---+---+

''')
