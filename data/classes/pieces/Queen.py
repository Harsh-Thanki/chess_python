# Queen.py

import pygame

from data.classes.Piece import Piece

class Queen(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		# Load and scale the image for the queen
		img_path = 'data/imgs/' + color[0] + '_queen.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

		self.notation = 'Q'


	def get_possible_moves(self, board):
		output = []

		# Calculate the moves in the north direction
		moves_north = []
		for y in range(self.y)[::-1]:
			moves_north.append(board.get_square_from_pos(
				(self.x, y)
			))
		output.append(moves_north)

		# Calculate the moves in the northeast direction
		moves_ne = []
		for i in range(1, 8):
			if self.x + i > 7 or self.y - i < 0:
				break
			moves_ne.append(board.get_square_from_pos(
				(self.x + i, self.y - i)
			))
		output.append(moves_ne)

		# Calculate the moves in the east direction
		moves_east = []
		for x in range(self.x + 1, 8):
			moves_east.append(board.get_square_from_pos(
				(x, self.y)
			))
		output.append(moves_east)

		# Calculate the moves in the southeast direction
		moves_se = []
		for i in range(1, 8):
			if self.x + i > 7 or self.y + i > 7:
				break
			moves_se.append(board.get_square_from_pos(
				(self.x + i, self.y + i)
			))
		output.append(moves_se)

		# Calculate the moves in the south direction
		moves_south = []
		for y in range(self.y + 1, 8):
			moves_south.append(board.get_square_from_pos(
				(self.x, y)
			))
		output.append(moves_south)

		# Calculate the moves in the southwest direction
		moves_sw = []
		for i in range(1, 8):
			if self.x - i < 0 or self.y + i > 7:
				break
			moves_sw.append(board.get_square_from_pos(
				(self.x - i, self.y + i)
			))
		output.append(moves_sw)

		# Calculate the moves in the west direction
		moves_west = []
		for x in range(self.x)[::-1]:
			moves_west.append(board.get_square_from_pos(
				(x, self.y)
			))
		output.append(moves_west)

		# Calculate the moves in the northwest direction
		moves_nw = []
		for i in range(1, 8):
			if self.x - i < 0 or self.y - i < 0:
				break
			moves_nw.append(board.get_square_from_pos(
				(self.x - i, self.y - i)
			))
		output.append(moves_nw)

		return output
