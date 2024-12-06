import pygame

pygame.init()

def darkColours(num):
    match num:
        case 0: ## black
            return (0, 0, 0)
        case 1: ## brown
            return (100, 65, 23)
        case 2: ## green
            return (0, 128, 0)

def lightColours(num):
    match num:
        case 0: ## white
            return (255,255,255)
        case 1: ## light gray
            return (211, 211, 211)
        case 2: ## very light blue
            return (173, 216, 230)

tileSize = 100

windowWidth =  tileSize*10
windowHeight = tileSize*8
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Dragon Chess')

## create the tiles

class chessBoard:

    def __init__(self, x, y, width, height, lightNum, darkNum):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.absX = x * width
        self.absY = y * height
        self.absPos = (self.absX, self.absY)
        self.pos = (x, y)
        if (x + y) % 2 == 0:
            self.colour = 'light'
        else:
            self.colour = 'dark'
        if self.colour == 'light':
            self.drawColour = lightColours(lightNum)
            self.hightlightColour = lightColours(lightNum) ## - (25, 25, 25)
        else:
            self.drawColour = darkColours(darkNum)
            self.hightlightColour = darkColours(darkNum) ## + (25, 25, 25)
        self.occupyingPiece = None
        self.coord = self.getCoords()
        self.highlight = False
        self.rect = pygame.Rect(
            self.absX,
            self.absY,
            self.width,
            self.height
        )

    ## get coordinates of the tile
    def getCoords(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)
    
    def drawBoard(self, window):
        ## draw tiles as light, dark or highlighted
        if self.highlight:
            pygame.draw.rect(window, self.hightlightColour, self.rect)
        else:
            pygame.draw.rect(window, self.drawColour, self.rect)
        
        ## add chess piece sprites
        if self.occupyingPiece != None:
            centeringRect = self.occupyingPiece.img.getRect()
            centeringRect.center = self.rect.center
            window.blit(self.occupyingPiece.img, centeringRect.topleft)

