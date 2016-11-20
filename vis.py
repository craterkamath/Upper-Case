import pygame, random, sys,time, constants
from constants import *

from pygame.locals import *

def collide(x1, x2, y1, y2, w1, w2, h1, h2):

        if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
                return True

        else:
                return False
def drawtext(text,font,surface,x,y):
        textobj=font.render(text,True,WHITE)
        textrect=textobj.get_rect()
        textrect.centerx = x
        textrect.centery = y
        surface.blit(textobj,textrect)

def die(screen, score):
        if score > constants.__SNAKE_HIGH:
                constants.__SNAKE_HIGH = score
        surface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
        window_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
        f=pygame.font.SysFont('Arial', 50)
        drawtext("HIGH SCORE:"+str(constants.__SNAKE_HIGH),f,surface,500,200)
        drawtext("YOUR SCORE:"+str(score),f,surface,500,250)
        drawtext('Press " Escape " to QUIT game',f,surface,500,300)
        drawtext('         " p " to PLay Again',f,surface,500,350)
        pygame.display.update()
        surface.fill(BLACK)
        while True:
                for event in pygame.event.get():
                        if event.type==QUIT:
                                return False
                                pygame.quit()
                                sys.exit()
                        if event.type==KEYDOWN:
                                if event.key==K_ESCAPE:
                                        pygame.mixer.music.stop()
                                        return False
                                        pygame.quit()
                                        sys.exit()
                                if event.key==ord('p'):
                                        play()
                                        
def instructions():
        window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
        window_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
        open_img = pygame.image.load('instructions_V.png')
        open_img = pygame.transform.scale(open_img , (WINDOWWIDTH,WINDOWHEIGHT))
        window.blit(open_img,window_rect)
        pygame.display.update()
        while True:
                for event in pygame.event.get():
                        if event.type==KEYDOWN:
                                if event.key==K_ESCAPE:
                                        pygame.mixer.music.stop()
                                        return False
                                        pygame.quit()
                                        sys.exit()
                                if event.key==ord('p'):
                                        zeb1 = play()
                                        if zeb1 == False:
                                                return False

        

def play():
        
        pickUpSound = pygame.mixer.Sound('b.wav')
        pygame.mixer.music.load('b.wav')
        pygame.mixer.music.play(-1, 0.0)
        musicPlaying = True
        a=5
        b=4*a
        xs = [290, 290, 290, 290, 290]
        ys = [290, 270, 250, 230, 210]
        dirs = 0
        score = 0
        applepos = (random.randint(0, 1350), random.randint(0, 750))
        pygame.init()
        s=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
        pygame.display.set_caption('Snake')
        appleimage = pygame.Surface((10, 10))                           #dimensions of the cube
        appleimage.fill((0, 0, 255))
        img = pygame.Surface((20, 20))                                  #dimensions of the snake
        img.fill((255, 0, 0))
        f = pygame.font.SysFont('Arial', 20)
        clock = pygame.time.Clock()
        tim = False

        while True:
            
                        clock.tick(4*a)
        
                        for e in pygame.event.get():

                                if e.type == QUIT:

                                        sys.exit(0)     

                                elif e.type == KEYDOWN:

                                        if e.key==K_SPACE: a=a*3

                                        if e.key==K_ESCAPE:
                                            r = die(s,score)
                                            if r == False:
                                                    return False
                                            pygame.quit()

                                            sys.exit()

                                        if e.key == K_UP and dirs != 0:dirs = 2

                                        elif e.key == K_DOWN and dirs != 2:dirs = 0

                                        elif e.key == K_LEFT and dirs != 1:dirs = 3

                                        elif e.key == K_RIGHT and dirs != 3:dirs = 1

                                elif e.type == KEYUP:

                                        if e.key==K_SPACE: a=a/3
                

                        i = len(xs)-1

                        while i >= 2:

                                if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
                                         r = die(s, score)
                                         if r == False:
                                                 return False

                                i-= 1
                        if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
                                score+=1
                                xs.append(700)
                                ys.append(700)
                                applepos=(random.randint(0,590),random.randint(0,590))
                        if xs[0] < 0:
                                xs[0] = 1350

                        if xs[0] > 1350:
                                xs[0] =  0
                        
                        if ys[0] < 0 :
                                ys[0] = 750
                        if ys[0] > 750:
                                ys[0] = 0

                        
                        i = len(xs)-1
                        while i >= 1:
                                xs[i] = xs[i-1];ys[i] = ys[i-1]
                                i -= 1
                        if dirs==0:ys[0] += 20
                        elif dirs==1:xs[0] += 20
                        elif dirs==2:ys[0] -= 20
                        elif dirs==3:xs[0] -= 20        
                        s.fill((255, 255, 255)) 
                        for i in range(0, len(xs)):
                                s.blit(img, (xs[i], ys[i]))
                        s.blit(appleimage, applepos)
                        l=f.render("Press ESC to quit                                                                           Score : "+str(score), True, ( 0, 0, 255))
                        t=f.render("Press ESC to quit                                                                           Score : "+str(score), True, ( 0, 0, 255))
                        s.blit(t, (10, 10))
                        pygame.display.update()

                                         


