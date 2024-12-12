import pygame, sys
from button import Button
from board import Board

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Chess Game")

# Load background image
BG = pygame.image.load("images/Background.png")
BG = pygame.transform.scale(BG, (1280, 720))

# Fonts
def font(size, font_name="Arial"):
    return pygame.font.SysFont(font_name, size)

# Options screen
def options():
    while True:
        screen.fill("white")
        mouse_pos = pygame.mouse.get_pos()

        # Back button
        back_button = Button(image=None, pos=(640, 460), text_input="BACK", font=font(75), base_color="White", hovering_color="Green")

        back_button.changeColor(mouse_pos)
        back_button.update(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    menu()

        pygame.display.update()

# Play function to start the chess game
def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen and draw the chessboard
        screen.fill("white")
        Board.board()

        pygame.display.update()

# Menu function
def menu():
    while True:
        # Set up menu background
        screen.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        # Title
        menu_text = font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))
        screen.blit(menu_text, menu_rect)

        # Buttons
        play_button = Button(image=pygame.image.load("images/Play.png"), pos=(640, 250), text_input="PLAY", font=font(75), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("images/Options.png"), pos=(640, 400), text_input="OPTIONS", font=font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("images/Quit.png"), pos=(640, 550), text_input="QUIT", font=font(75), base_color="#d7fcd4", hovering_color="White")
        
        # Update buttons
        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play()
                if options_button.checkForInput(mouse_pos):
                    options()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Start the menu
menu()
