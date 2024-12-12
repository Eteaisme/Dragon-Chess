import pygame
screen = pygame.display.set_mode((1280, 720))
w_pieces = ['rook','knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] 
w_location = [(0,0) , (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
b_pieces = ['rook','knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] 
b_location = [(0,7) , (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
cap_white = []
cap_blue = []

# For turns, ex: blue's turn or white's turn
turn = 0
valid_moves= []
selection = 100

#Load the pieces on to the board
#queen
w_queen = pygame.image.load("images/w_queen.png")
w_queen = pygame.transform.scale(w_queen, (65, 65))
b_queen = pygame.image.load("images/b_queen.png")
b_queen = pygame.transform.scale(b_queen, (65, 65))
# king
w_king = pygame.image.load("images/w_king.png")
w_king = pygame.transform.scale(w_king, (65, 65))
b_king = pygame.image.load("images/b_king.png")
b_king = pygame.transform.scale(b_king, (65, 65))
# rook
w_rook = pygame.image.load("images/w_rook.png")
w_rook = pygame.transform.scale(w_rook, (65, 65))
b_rook = pygame.image.load("images/b_rook.png")
b_rook = pygame.transform.scale(b_rook, (65, 65))
# bishop
w_bishop = pygame.image.load("images/w_bishop.png")
w_bishop = pygame.transform.scale(w_bishop, (65, 65))
b_bishop = pygame.image.load("images/b_bishop.png")
b_bishop = pygame.transform.scale(b_bishop, (65, 65))
# knight
w_knight = pygame.image.load("images/w_knight.png")
w_knight = pygame.transform.scale(w_knight, (65, 65))
b_knight = pygame.image.load("images/b_knight.png")
b_knight = pygame.transform.scale(b_knight, (65, 65))
# pawn
w_pawn = pygame.image.load("images/w_pawn.png")
w_pawn = pygame.transform.scale(w_pawn, (65, 65))
b_pawn = pygame.image.load("images/b_pawn.png")
b_pawn = pygame.transform.scale(b_pawn, (65, 65))


w_images = [w_pawn, w_knight, w_bishop, w_rook, w_queen, w_king]
b_images = [b_pawn, b_knight, b_bishop, b_rook, b_queen, b_king]
piece_list = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king', 'knight']


class Board:
    def draw_board(screen):
        global square_size, board_x, board_y
        # Calculate the size and position of the board
        square_size = min(screen.get_width(), screen.get_height()) // 8
        board_x = (screen.get_width() - (square_size * 8)) // 2
        board_y = (screen.get_height() - (square_size * 8)) // 2

        light = (179, 231, 150)
        dark = (116, 168, 98)
        screen.fill("black")

        # Draw the chessboard
        for row in range(8):
            for col in range(8):
                color = light if (row + col) % 2 == 0 else dark
                pygame.draw.rect(screen, color, 
                                 (board_x + col * square_size, board_y + row * square_size, square_size, square_size))

    def draw_pieces():
        # Draw white pieces
        for i in range(len(w_pieces)):
            index = piece_list.index(w_pieces[i])
            x = board_x + w_location[i][0] * square_size + 10
            y = board_y + w_location[i][1] * square_size + 10
            screen.blit(w_images[index], (x, y))
            if turn < 2 and selection == i:
                pygame.draw.rect(screen, 'red', (x - 10, y - 10, square_size, square_size), 3)

        # Draw black pieces
        for i in range(len(b_pieces)):
            index = piece_list.index(b_pieces[i])
            x = board_x + b_location[i][0] * square_size + 10
            y = board_y + b_location[i][1] * square_size + 10
            screen.blit(b_images[index], (x, y))
            if turn >= 2 and selection == i:
                pygame.draw.rect(screen, 'blue', (x - 10, y - 10, square_size, square_size), 3)

    def board():
        Board.draw_board(screen)
        Board.draw_pieces()
        global turn, selection, valid_moves
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Convert mouse position to board coordinates
                x = (event.pos[0] - board_x) // square_size
                y = (event.pos[1] - board_y) // square_size
                coor = (x, y)

                if 0 <= x < 8 and 0 <= y < 8:  # Ensure click is on the board
                    if turn <= 1 and coor in w_location:
                        selection = w_location.index(coor)
                        if turn == 0:
                            turn = 1
                    elif turn > 1 and coor in b_location:
                        selection = b_location.index(coor)
                        if turn == 2:
                            turn = 3
                    # Handle valid moves
                    if coor in valid_moves and selection != 100:
                        if turn <= 1:
                            w_location[selection] = coor
                        else:
                            b_location[selection] = coor
                        # Reset selection and handle turn switching
                        selection = 100
                        valid_moves = []
                        turn = (turn + 1) % 4
