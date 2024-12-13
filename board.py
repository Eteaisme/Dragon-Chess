import pygame

screen = pygame.display.set_mode((750, 600))

def get_piece_data():
    # Define the white pieces and their locations
    w_pieces = ['dragon', 'rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'dragon', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    w_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)]

    # Define the black pieces and their locations
    b_pieces = ['dragon', 'rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'dragon', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    b_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6)]

    return w_pieces, w_locations, b_pieces, b_locations

def load_piece_images():
    w_king = pygame.transform.scale(pygame.image.load('Pieces/w_king.png'), (70, 70))
    w_queen = pygame.transform.scale(pygame.image.load('Pieces/w_queen.png'), (70, 70))
    w_rook = pygame.transform.scale(pygame.image.load('Pieces/w_rook.png'), (70, 70))
    w_bishop = pygame.transform.scale(pygame.image.load('Pieces/w_bishop.png'), (70, 70))
    w_knight = pygame.transform.scale(pygame.image.load('Pieces/w_knight.png'), (70, 70))
    w_pawn = pygame.transform.scale(pygame.image.load('Pieces/w_pawn.png'), (70, 70))
    w_dragon = pygame.transform.scale(pygame.image.load('Pieces/w_dragon.png'), (70, 70))

    b_king = pygame.transform.scale(pygame.image.load('Pieces/b_king.png'), (70, 70))
    b_queen = pygame.transform.scale(pygame.image.load('Pieces/b_queen.png'), (70, 70))
    b_rook = pygame.transform.scale(pygame.image.load('Pieces/b_rook.png'), (70, 70))
    b_bishop = pygame.transform.scale(pygame.image.load('Pieces/b_bishop.png'), (70, 70))
    b_knight = pygame.transform.scale(pygame.image.load('Pieces/b_knight.png'), (70, 70))
    b_pawn = pygame.transform.scale(pygame.image.load('Pieces/b_pawn.png'), (70, 70))
    b_dragon = pygame.transform.scale(pygame.image.load('Pieces/b_dragon.png'), (70, 70))

    return [w_dragon, w_king, w_queen, w_bishop, w_knight, w_rook, w_pawn], [b_dragon, b_king, b_queen, b_bishop, b_knight, b_rook, b_pawn]

w_pieces, w_locations, b_pieces, b_locations = get_piece_data()

w_images, b_images = load_piece_images()

piece_list = ['dragon', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn']

class Board:
    @staticmethod
    def draw_board(screen):
        
        #Put board in the center of the screen
        square_size = min(screen.get_width(), screen.get_height()) // 8  # Ensure it fits the screen
        board_x = (screen.get_width() - (square_size * 10))
        board_y = (screen.get_height() - (square_size * 8))

        # Define the colors of the tiles
        light = (179, 231, 150)  
        dark = (116, 168, 98)    
        screen.fill("black")
        
        # Draw the chessboard
        for row in range(8): # 8 rows
            for col in range(10): # 10 columns
                # Alternate tile colors
                if (row + col) % 2 == 0:
                    color = light
                else:
                    color = dark

                # Draw each square, centered in the screen
                pygame.draw.rect(screen, color, (board_x + col * square_size, board_y + row * square_size, square_size, square_size))

        # Optional: Draw grid lines to separate squares
        grid_color = (0, 0, 0)  # Black grid lines
        for row in range(9): # Horizontal lines (8 rows require 9 lines)
            pygame.draw.line(screen, grid_color, (board_x, board_y + row * square_size), (board_x + (10 * square_size), board_y + row * square_size), 2)
        for col in range(11): # Vertical lines (10 columns require 11 lines)
            pygame.draw.line(screen, grid_color, (board_x + col * square_size, board_y), (board_x + col * square_size, board_y + (8 * square_size)), 2)

    @staticmethod
    def draw_pieces(screen, w_locations, b_locations):
        square_size = min(screen.get_width(), screen.get_height()) // 8  # Ensure it fits the screen

        # Draw white pieces
        for i in range(len(w_pieces)):
            index = piece_list.index(w_pieces[i])
            # Center each piece within its corresponding square
            x_pos = w_locations[i][0] * square_size + (square_size // 2 - w_images[index].get_width() // 2)
            y_pos = w_locations[i][1] * square_size + (square_size // 2 - w_images[index].get_height() // 2)
            screen.blit(w_images[index], (x_pos, y_pos))

        # Draw blue pieces
        for i in range(len(b_pieces)):
            index = piece_list.index(b_pieces[i])
            # Center each piece within its corresponding square
            x_pos = b_locations[i][0] * square_size + (square_size // 2 - b_images[index].get_width() // 2)
            y_pos = b_locations[i][1] * square_size + (square_size // 2 - b_images[index].get_height() // 2)
            screen.blit(b_images[index], (x_pos, y_pos))