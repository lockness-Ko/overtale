# import the pygame module, so you can use it
import pygame
import os
# define a main function
def main():
    xpos = 0
    ypos = 0
    px=400
    py=400
    won=False
    # initialize the pygame module
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('You Won!', False, (255, 255, 255))
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("oVeRtAlE")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500,500))
    image = pygame.image.load("hm.jpg")
    image = pygame.transform.scale(image, (100, 100))
    paper = pygame.image.load("paper.jpg")
    paper = pygame.transform.scale(paper, (100,100))
    # define a variable to control the main loop
    running = True
    music = os.path.join("D:\overtale", 'bruh.wav')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    # main loop
    while running:
        if won != True:
            screen.blit(image, (xpos,ypos))
            screen.blit(paper, (px,py))
            pygame.display.flip()
            pygame.draw.rect(screen, [0,0,0], [0,0,500,500],0)
            if xpos>300 and ypos < 300:
                won=True
        else:
            print(xpos)
            screen.blit(textsurface,(200,200))
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            try:
                print(event.key)
                if (event.key == 276):
                    xpos-=15
                elif (event.key == 275):
                    xpos+=15
                elif (event.key == 273):
                    ypos-=15
                elif (event.key == 274):
                    ypos+=15
            except Exception as ex:
                pass
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()