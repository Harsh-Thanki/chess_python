import pygame

from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	# Fill the display with white color
	display.fill('white')
	# Draw the chessboard and pieces on the display
	board.draw(display)
	# Update the display
	pygame.display.update()


if __name__ == '__main__':
	running = True
	while running:
		# Get the mouse position
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					# Handle left mouse button click on the board
					board.handle_click(mx, my)

		# Check if either white or black is in checkmate
		if board.is_in_checkmate('black'):
			print('White wins!')
			running = False
		elif board.is_in_checkmate('white'):
			print('Black wins!')
			running = False

		# Draw the updated display
		draw(screen)
