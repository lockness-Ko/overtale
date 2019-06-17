# import the pygame module, so you can use it
import pygame
import os
# define a main function
def main():
    xpos = 50
    ypos = 50
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("oVeRtAlE")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500,500))
    image = pygame.image.load("hm.jpg")
    image = pygame.transform.scale(image, (200, 200))
    # define a variable to control the main loop
    running = True
    music = os.path.join("D:\overtale", 'bruh.wav')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    # main loop
    while running:
        screen.blit(image, (xpos,ypos))
        pygame.display.flip()
        pygame.draw.rect(screen, [0,0,0], [0,0,500,500],0)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            try:
                if (event.key == pygame.K_LEFT):
                    xpos-=15
                elif (event.key == pygame.K_RIGHT):
                    xpos+=15
                elif (event.key == pygame.K_UP):
                    ypos-=15
                elif (event.key == pygame.K_DOWN):
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