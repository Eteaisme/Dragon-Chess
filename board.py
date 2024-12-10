import pygame

white_pieces = ['rook','knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] 
white_location = [(0,0) , (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
blue_pieces = ['rook','knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] 
blue_location = [(0,7) , (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

BOARD_POS = [
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
    [(1), (2), (3), (4), (5), (6), (7), (8)],
]

class Board:
    @staticmethod
    def draw_board(screen):
        
        #Put board in the center of the screen
        square_size = min(screen.get_width(), screen.get_height()) // 8  # Ensure it fits the screen
        board_x = (screen.get_width() - (square_size * 8)) // 2
        board_y = (screen.get_height() - (square_size * 8)) // 2

        # Define the colors of the tiles
        light = (179, 231, 150)  
        dark = (116, 168, 98)    
        screen.fill("black")
        
        # Draw the chessboard
        for row in range(8):
            for col in range(8):
                # Alternate tile colors
                if (row + col) % 2 == 0:
                    color = light
                else:
                    color = dark

                # Draw each square, centered in the screen
                pygame.draw.rect(screen, color, (board_x + col * square_size, board_y + row * square_size, square_size, square_size))

        # Optional: Draw grid lines to separate squares
        grid_color = (0, 0, 0)  # Black grid lines
        for row in range(9):
            pygame.draw.line(screen, grid_color, (board_x, board_y + row * square_size), (board_x + (8 * square_size), board_y + row * square_size), 2)  # Horizontal lines
            pygame.draw.line(screen, grid_color, (board_x + row * square_size, board_y), (board_x + row * square_size, board_y + (8 * square_size)), 2)  # Vertical lines
            
    '''
    def setup_board():
'''
