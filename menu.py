import pygame, sys
from button import Button

pygame.init()

# Define the screen size and caption
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Background image
BG = pygame.image.load("images/Background.png")
BG = pygame.transform.scale(BG, (1280, 720))

# Function to get system font
def font(size, font_name="Arial"):
    return pygame.font.SysFont(font_name, size)

def play():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        play_back = Button(image=None, pos=(640, 460),text_input="BACK", font=font(75), base_color="White", hovering_color="Green")

        play_back.changeColor(mouse_pos)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(mouse_pos):
                    menu()
                    
        pygame.display.update()
    
def options():
    while True:
        mouse_pos= pygame.mouse.get_pos()

        screen.fill("white")
        options_back = Button(image=None, pos=(640, 460),text_input="BACK", font=font(75), base_color="Black", hovering_color="Green")

        options_back.changeColor(mouse_pos)
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(mouse_pos):
                    menu()

        pygame.display.update()

def menu():
    while True:
        screen.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("images/Play.png"), pos=(640, 250), text_input="PLAY", font= font(75), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("images/Options.png"), pos=(640, 400), text_input="OPTIONS", font= font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("images/Quit.png"), pos=(640, 550), text_input="QUIT", font= font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menu_text, menu_rect )

        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

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

menu()
