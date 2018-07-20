import pygame as py
import time
import random

py.init()

display_width = 900
display_height = 700

black = (0,0,0)
white = (255,255,255)
blue= (0,0,255)
red = (200,0,0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
car_width = 100

gameDisplay = py.display.set_mode((display_width,display_height))
py.display.set_caption('CAR RACE GAME')
clock = py.time.Clock()

carImg = py.image.load('car1.jpeg')

def things_dodge(count):
    font = py.font.SysFont(None, 25)
    text = font.render("SCORE: "+str(count), True, white)
    gameDisplay.blit(text, (0,0))
    

def things(thingx, thingy, thingw, thingh, color):
    py.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = py.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    py.display.update()

    time.sleep(1)

    gameloop()
    

def crash():
    largeText = py.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects("crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

        
        button("Play again", 300, 450, 100, 50, green, bright_green, gameloop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        py.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = py.mouse.get_pos()
    click = py.mouse.get_pressed()

    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        py.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        py.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = py.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2))), (y+(h/2))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    py.quit()
    quit()

        
def game_intro():

    intro = True

    while intro:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

        gameDisplay.fill(white)
        largeText = py.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("CAR GAME", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO", 300, 450, 100, 50, green, bright_green, gameloop)
        button("EXIT", 550, 450, 100, 50, red, bright_red, quitgame)
        py.display.update()
        clock.tick(15)
    

def gameloop():
    x = (display_width * 0.40)
    y = (display_height * 0.7)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    Score = 0

    gameExit = False

    while not gameExit:

        for event in py.event.get():
            if event.type == py.QUIT:
               py.quit()
               quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    x_change = -5
                if event.key == py.K_RIGHT:
                    x_change = 5
            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(black)

        things(thing_startx, thing_starty, thing_width, thing_height, white)
        thing_starty += thing_speed
        car(x,y)
        things_dodge(Score)

        # for boundry
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            Score += 1
            thing_speed += 1
            thing_width += (Score * 2)

            
        if y < thing_starty+thing_height:
            print('SAFE')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width:
               print('DAMAGED')
               crash()
    
        py.display.update()
        clock.tick(100)

game_intro()
gameloop()
py.quit()
quit()



    




