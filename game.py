import pygame, sys
from board import Board
from board import get_piece_data

pygame.init()
screen = pygame.display.set_mode((750, 600))
timer = pygame.time.Clock()
fps = 30

w_pieces, w_locations, b_pieces, b_locations = get_piece_data()

## function to check all pieces valid options on the board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        """
        if piece == 'dragon':
            moves_list = check_dragon(location, turn)
        """
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

## check valid moves for only selected piece
def check_valid_moves():
    if gameloop.turn_step < 2:
        options_list = gameloop.w_options
    else:
        options_list = gameloop.b_options
    valid_options = options_list[gameloop.selection]
    return valid_options

## draw valid moves on screen
def draw_valid(moves):
    for i in range(len(moves)):
        pygame.draw.rect(screen, (150, 150, 150), (moves[i][0] * 100 + 35, moves[i][1] * 100 + 35), 70)
"""
def check_dragon(position,colour):
"""

## check valid pawn moves
def check_pawn(position, colour):
    moves_list = []
    if colour == 'white':
        if (position[0], position[1] + 1) not in w_locations and (position[0], position[1] + 1) not in b_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in w_locations and (position[0], position[1] + 2) not in b_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in b_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in b_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in w_locations and (position[0], position[1] - 1) not in b_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in w_locations and (position[0], position[1] - 2) not in b_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in w_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in w_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_knight(position, colour):
    moves_list = []
    possible_moves = [
        (position[0] + 2, position[1] + 1), (position[0] + 2, position[1] - 1),
        (position[0] - 2, position[1] + 1), (position[0] - 2, position[1] - 1),
        (position[0] + 1, position[1] + 2), (position[0] + 1, position[1] - 2),
        (position[0] - 1, position[1] + 2), (position[0] - 1, position[1] - 2)
    ]

    for move in possible_moves:
        if 0 <= move[0] < 10 and 0 <= move[1] < 8:  # Stay within bounds
            if colour == 'white' and move not in w_locations:
                moves_list.append(move)
            if colour == 'black' and move not in b_locations:
                moves_list.append(move)
    return moves_list

def check_rook(position, colour):
    moves_list = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for direction in directions:
        for i in range(1, 10):
            move = (position[0] + i * direction[0], position[1] + i * direction[1])
            if 0 <= move[0] < 10 and 0 <= move[1] < 8:
                if colour == 'white':
                    if move in w_locations:
                        break
                    moves_list.append(move)
                    if move in b_locations:
                        break
                if colour == 'black':
                    if move in b_locations:
                        break
                    moves_list.append(move)
                    if move in w_locations:
                        break
    return moves_list


def check_bishop(position, colour):
    moves_list = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for direction in directions:
        for i in range(1, 10):
            move = (position[0] + i * direction[0], position[1] + i * direction[1])
            if 0 <= move[0] < 10 and 0 <= move[1] < 8:
                if colour == 'white':
                    if move in w_locations:
                        break
                    moves_list.append(move)
                    if move in b_locations:
                        break
                if colour == 'black':
                    if move in b_locations:
                        break
                    moves_list.append(move)
                    if move in w_locations:
                        break
    return moves_list

def check_queen(position, colour):
    return check_rook(position, colour) + check_bishop(position, colour)

def check_king(position, colour):
    moves_list = []
    possible_moves = [
        (position[0] + 1, position[1]), (position[0] - 1, position[1]),
        (position[0], position[1] + 1), (position[0], position[1] - 1),
        (position[0] + 1, position[1] + 1), (position[0] + 1, position[1] - 1),
        (position[0] - 1, position[1] + 1), (position[0] - 1, position[1] - 1)
    ]

    for move in possible_moves:
        if 0 <= move[0] < 10 and 0 <= move[1] < 8:  # Stay within bounds
            if colour == 'white' and move not in w_locations:
                moves_list.append(move)
            if colour == 'black' and move not in b_locations:
                moves_list.append(move)
    return moves_list

valid_moves = []
w_captured_pieces = []
b_captured_pieces = []
selection = 100
turn_step = 0
## main game loop
def gameloop():
    global turn_step, selection, w_captured_pieces, b_captured_pieces
    global w_options, b_options, valid_moves
    b_options = check_options(b_pieces, b_locations, 'blue')
    w_options = check_options(w_pieces, w_locations, 'white')
    while True:
        timer.tick(fps)

        # Clear screen and draw the chessboard
        screen.fill("white")
        Board.draw_board(screen)
        Board.draw_pieces(screen, w_locations, b_locations)
        if selection != 100:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(f"Mouse clicked at: {event.pos}")
                x_coord = event.pos[0] // 100
                y_coord = event.pos[1] // 100
                print(f"Calculated board coordinates: ({x_coord}, {y_coord})")
                click_coords = (x_coord, y_coord)
                if turn_step <= 1:
                    if click_coords in w_locations:
                        print(f"White piece selected at {click_coords}")
                        selection = w_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        w_locations[selection] = click_coords
                    if click_coords in b_locations:
                        b_piece = b_locations.index(click_coords)
                        w_captured_pieces.append(b_locations[b_piece])
                        b_pieces.pop(b_piece)
                        b_locations.pop(b_piece)
                    b_options = check_options(b_pieces, b_locations, 'blue')
                    w_options = check_options(w_pieces, w_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                if turn_step > 1:
                    if click_coords in b_locations:
                        print(f"Black piece selected at {click_coords}")
                        selection = b_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100:
                        b_locations[selection] = click_coords
                    if click_coords in b_locations:
                        w_piece = w_locations.index(click_coords)
                        b_captured_pieces.append(w_locations[w_piece])
                        w_pieces.pop(w_piece)
                        w_locations.pop(w_piece)
                    b_options = check_options(b_pieces, b_locations, 'blue')
                    w_options = check_options(w_pieces, w_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        print(f"Turn step: {turn_step}, Selection: {selection}, Valid moves: {valid_moves}")
        pygame.display.update()