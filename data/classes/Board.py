# Board.py

import pygame
from data.classes.Square import Square
from data.classes.pieces.Rook import Rook
from data.classes.pieces.Bishop import Bishop
from data.classes.pieces.Knight import Knight
from data.classes.pieces.Queen import Queen
from data.classes.pieces.King import King
from data.classes.pieces.Pawn import Pawn

# Game state checker
class Board:
    def __init__(self, width, height):
        self.width = width  # Width of the board
        self.height = height  # Height of the board
        self.tile_width = width // 8  # Width of each tile on the board
        self.tile_height = height // 8  # Height of each tile on the board
        self.selected_piece = None  # The currently selected chess piece (if any)
        self.turn = 'white'  # Current turn ('white' or 'black')
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],  # Initial configuration of black pieces
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],  # Initial configuration of black pawns
            ['','','','','','','',''],  # Empty row
            ['','','','','','','',''],  
            ['','','','','','','',''],  
            ['','','','','','','',''],  
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],  # Initial configuration of white pawns
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],  # Initial configuration of white pieces
        ]  # Current configuration of the board
        self.squares = self.generate_squares()  # List of Square objects representing each tile on the board
        self.setup_board()  # Set up the board with initial configurations
