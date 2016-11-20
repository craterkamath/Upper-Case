
import pygame, time, sys, bouncer_singleplayer, vis, Game_final
from constants import *
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("UPPERCASE")

def drawtext(text,font,surface,x,y):
        textobj=font.render(text,True,WHITE)
        textrect=textobj.get_rect()
        textrect.centerx = x
        textrect.centery = y
        surface.blit(textobj,textrect)
                        
def drawtext1(text,font,surface,x,y):
        textobj=font.render(text,True,BLACK,YELLO)
        textrect=textobj.get_rect()
        textrect.centerx = x
        textrect.centery = y
        surface.blit(textobj,textrect)
        return(textrect)

window.fill(BLACK)

font=pygame.font.SysFont(None,25)
font2=pygame.font.SysFont(None,60)

drawtext('T E A M',font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//4)
drawtext(TEAM_NAME,font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
drawtext('P R E S E N T S',font2,window,WINDOWWIDTH//2,3*(WINDOWHEIGHT//4))
pygame.display.update()

t1 = time.time()
while True:
    t2 = time.time()
    if t2-t1 >=3:
            break


def bouncer_main():
    window.fill(BLACK)
    drawtext("collecting bouncers....",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    t1 = time.time()
    while True:
            t2 = time.time()
            if t2-t1 >=2:
                    break
    window.fill(BLACK)
    drawtext("creating Arena ....",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    t1 = time.time()
    while True:
            t2 = time.time()
            if t2-t1 >=2:
                    break
    window.fill(BLACK)
    game1b = drawtext1("CONTINUE",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                m_x = event.pos[0]
                m_y = event.pos[1]
                if game1b.collidepoint(m_x,m_y):
                    zeb = bouncer_singleplayer.start()
                    if zeb == False:

                            display_main_open()

def snake_main():
    window.fill(BLACK)
    drawtext("creating snake and foods....",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    t1 = time.time()
    while True:
            t2 = time.time()
            if t2-t1 >=2:
                    break
    window.fill(BLACK)
    drawtext("creating Arena ....",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    t1 = time.time()
    while True:
            t2 = time.time()
            if t2-t1 >=2:
                    break
    window.fill(BLACK)
    game1b = drawtext1("CONTINUE",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                m_x = event.pos[0]
                m_y = event.pos[1]
                if game1b.collidepoint(m_x,m_y):
                    zeb = vis.instructions()
                    if zeb == False:
                            display_main_open()

def alien_main():
    window.fill(BLACK)
    drawtext("creating vicious aliens....",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    t1 = time.time()
    while True:
            t2 = time.time()
            if t2-t1 >=2:
                    break
    window.fill(BLACK)
    drawtext("creating fight Arena ....",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    t1 = time.time()
    while True:
            t2 = time.time()
            if t2-t1 >=2:
                    break
    window.fill(BLACK)
    game1b = drawtext1("CONTINUE",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                m_x = event.pos[0]
                m_y = event.pos[1]
                if game1b.collidepoint(m_x,m_y):
                    zeb = Game_final.gameloop()
                    if zeb == False:
                            display_main_open()

    

def display_main_open():   
    window.fill(BLACK)
    game1 = drawtext1("FIRE BOUNCER",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2-100)
    game2 = drawtext1("ALIEN INVASION",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2)
    game3 = drawtext1("SNAKE MANIA",font2,window,WINDOWWIDTH//2,WINDOWHEIGHT//2+100)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                m_x = event.pos[0]
                m_y = event.pos[1]
                
                if game1.collidepoint(m_x,m_y):
                    bouncer_main()
                       
                elif game2.collidepoint(m_x,m_y):
                    alien_main()
                    
                elif game3.collidepoint(m_x,m_y):
                    snake_main()
        

display_main_open()   






