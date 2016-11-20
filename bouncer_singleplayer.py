import pygame, sys, time , random, constants
from pygame.locals import *
from constants import *

pygame.init()


window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("bouncing fire")

left = 0
top = 0
bottom = 0
right = 0

sound = pygame.mixer.Sound('bullete.wav')
font = pygame.font.SysFont(None,25)
font1 = pygame.font.SysFont(None,80)
window_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)

def endgame(score):
        
        window.fill(BLACK)
        window_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
        endimg1 = pygame.image.load('endimg1_S.png')
        endimg1 = pygame.transform.scale(endimg1 , (WINDOWWIDTH,WINDOWHEIGHT))
        window.blit(endimg1,window_rect)                
        if score > constants.__BOUNCE_HIGH:
                constants.__BOUNCE_HIGH = score
                
        drawtext('HIGH SCORE:  '+str(constants.__BOUNCE_HIGH),font,window,WINDOWWIDTH//2+100,WINDOWHEIGHT//2-100)
        drawtext('YOUR SCORE:  '+str(score),font,window,WINDOWWIDTH//2+100,WINDOWHEIGHT//2)
        drawtext('Press " Escape " to QUIT game',font,window,WINDOWWIDTH-80,WINDOWHEIGHT-100)
        drawtext('press " p " to Play Again',font,window,WINDOWWIDTH-80,WINDOWHEIGHT-50)
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
                                        game()
                                        

def drawtext(text,font,surface,x,y):
        textobj=font.render(text,1,WHITE)
        textrect=textobj.get_rect()
        textrect.topright=(x,y)
        surface.blit(textobj,textrect)

def create_random_boxes():
        l_bouncer_rect = []
        for i in range(BOXES//2):
                x = random.randrange(200,WINDOWWIDTH//2 )
                y = random.randrange(0,WINDOWHEIGHT - 120)
                
                l_bouncer_rect.append(pygame.Rect(x,y,4,120))
        for i in range(BOXES//2):
                x = random.randrange(WINDOWWIDTH//2,WINDOWWIDTH - 200 )
                y = random.randrange(0,WINDOWHEIGHT - 120)
                
                l_bouncer_rect.append(pygame.Rect(x,y,4,120))
        return l_bouncer_rect
                
                                        
def collision_player1(player_1,bouncer_rect):
        if bouncer_rect['rect'].colliderect(player_1): 
                if bouncer_rect['dir'] == TOPLEFT :
                    bouncer_rect['dir'] = TOPRIGHT
                if bouncer_rect['dir']  == DOWNLEFT:
                    bouncer_rect['dir'] = DOWNRIGHT
                sound.play()
        return bouncer_rect

def collision_player2(player_2,bouncer_rect,score):
        if bouncer_rect['rect'].colliderect(player_2):
                if bouncer_rect['dir'] == TOPRIGHT :
                    bouncer_rect['dir'] = TOPLEFT
                if bouncer_rect['dir']  == DOWNRIGHT:
                    bouncer_rect['dir'] = DOWNLEFT
                score += 1
                sound.play()
        return bouncer_rect,score

def normal_movement(bouncer_dic):
        if( bouncer_dic['rect'].top < 0 ):
            if( bouncer_dic['dir'] == TOPLEFT):
                bouncer_dic['dir'] = DOWNLEFT
            if( bouncer_dic['dir'] == TOPRIGHT):
                bouncer_dic['dir'] = DOWNRIGHT
        if( bouncer_dic['rect'].bottom > WINDOWHEIGHT ):
            if( bouncer_dic['dir'] == DOWNLEFT):
                bouncer_dic['dir'] = TOPLEFT
            if( bouncer_dic['dir'] == DOWNRIGHT):
                bouncer_dic['dir'] = TOPRIGHT
    
        if( bouncer_dic['dir'] == TOPLEFT ):
            bouncer_dic['rect'].left -= MOVESPEED
            bouncer_dic['rect'].top -= MOVESPEED
    
        if( bouncer_dic['dir'] == TOPRIGHT ):
            bouncer_dic['rect'].right += MOVESPEED
            bouncer_dic['rect'].top -= MOVESPEED
    
        if( bouncer_dic['dir'] == DOWNLEFT ):
            bouncer_dic['rect'].left -= MOVESPEED
            bouncer_dic['rect'].top += MOVESPEED
    
        if( bouncer_dic['dir'] == DOWNRIGHT ):
            bouncer_dic['rect'].left += MOVESPEED
            bouncer_dic['rect'].top += MOVESPEED
    
        return bouncer_dic

def collision(player_2,bouncer_rect):
        
        if True:
                if bouncer_rect['dir'] == TOPRIGHT :
                        if bouncer_rect['rect'].colliderect(player_2):
                                bouncer_rect['dir'] = TOPLEFT
                                bouncer_rect['rect'].left -= MOVESPEED
                                bouncer_rect['rect'].top -= MOVESPEED
                                sound.play()
                                
                if bouncer_rect['dir']  == DOWNRIGHT:
                        if bouncer_rect['rect'].colliderect(player_2):
                                bouncer_rect['dir'] = DOWNLEFT
                                bouncer_rect['rect'].left -= MOVESPEED
                                bouncer_rect['rect'].top += MOVESPEED
                                sound.play()
                                
                                
                if bouncer_rect['dir'] == TOPLEFT :
                        if bouncer_rect['rect'].colliderect(player_2):
                                bouncer_rect['dir'] = TOPRIGHT
                                bouncer_rect['rect'].right += MOVESPEED
                                bouncer_rect['rect'].top -= MOVESPEED
                                sound.play()
                                
                if bouncer_rect['dir']  == DOWNLEFT:
                        if bouncer_rect['rect'].colliderect(player_2):
                                bouncer_rect['dir'] = DOWNRIGHT
                                bouncer_rect['rect'].left += MOVESPEED
                                bouncer_rect['rect'].top += MOVESPEED
                                sound.play()
                
        return bouncer_rect


def ball_graphics(c):

        if c <= FLOPS:
                        ball = pygame.image.load('bouncer_ball_pic1.png')
                        ball_im = pygame.transform.scale(ball , (30,30))
        elif c <= 2*FLOPS:
                        ball = pygame.image.load('bouncer_ball_pic2.png')
                        ball_im = pygame.transform.scale(ball , (30,30))
        else:
                        ball = pygame.image.load('bouncer_ball_pic3.png')
                        ball_im = pygame.transform.scale(ball , (30,30))
        return ball_im


def game():
        score = 0
        zeb2 = True
        zeb3 = True
        
        top_1 = False
        c = 0
        top_2 = False
        down_1 = False
        down_2 = False    
        bouncer_dic = {'rect': pygame.Rect(WINDOWWIDTH//2,WINDOWHEIGHT//2, 30,30),'dir': random.choice([TOPLEFT,TOPRIGHT,DOWNLEFT,DOWNRIGHT])}
        player_1 = pygame.Rect(5,WINDOWHEIGHT//2,PLAYER_WIDTH,PLAYER_HEIGHT)
        player_2 = pygame.Rect(WINDOWWIDTH-10,WINDOWHEIGHT//2,PLAYER_WIDTH,PLAYER_HEIGHT)
        rand_rec = 0
        loop_cnt = 0
        rect_ls = create_random_boxes()
        clock = pygame.time.Clock()
        while True:
                clock.tick(1000)
                rand_rec += 1
                
                if c>15*FLOPS:
                        c=0
                if rand_rec > 200*FLOPS:
                        rand_rec = 0
                        rect_ls = create_random_boxes()
                window.fill(BLACK)
                for rect in rect_ls:
                        bouncer_dic = collision(rect , bouncer_dic)
                
                if(bouncer_dic['rect'].left < 50):
                    bouncer_dic = collision_player1(player_1,bouncer_dic)

                if(bouncer_dic['rect'].right > WINDOWWIDTH - 50):
                    bouncer_dic,score = collision_player2(player_2,bouncer_dic,score)
                 
			
                if ((player_1.top >= 0 ) and (player_1.bottom <= WINDOWHEIGHT)):
                    for event in pygame.event.get():
                
                        if event.type == KEYDOWN:
                            if event.key  == ord('w'):
                                top_1 = True
                                down_1 = False
                            if event.key  == ord('s'):
                                down_1 = True
                                top_1 = False
                            if event.key  == K_UP:
                                top_2 = True
                                down_2 = False
                            if event.key  == K_DOWN:
                                down_2 = True
                                top_2 = False
                            '''if event.key == K_ESCAPE:
                                r = endgame(score)
                                if r == False:
                                        pygame.mixer.music.stop()
                                        return False'''
                        if event.type == KEYUP:
                            top_1 = False
                            top_2 = False
                            down_1 = False
                            down_2 = False
                            if event.key == K_ESCAPE:
                                r = endgame(score)
                                if r == False:
                                        pygame.mixer.music.stop()
                                        return False
               
                if top_1:
                    player_1.top -= MOVESPEED_PLAYER
                if down_1:
                    player_1.bottom += MOVESPEED_PLAYER
                if top_2:
                    player_2.top -= MOVESPEED_PLAYER
                if down_2:
                    player_2.bottom += MOVESPEED_PLAYER
                if player_1.top < 0 :
                    player_1.top = 0
                if player_1.bottom > WINDOWHEIGHT:
                    player_1.bottom = WINDOWHEIGHT
            
                if player_2.top < 0 :
                    player_2.top = 0
                if player_2.bottom > WINDOWHEIGHT:
                    player_2.bottom = WINDOWHEIGHT        

                if bouncer_dic['rect'].left < 1 :
                        bouncer_dic = {'rect': pygame.Rect(WINDOWWIDTH//2,WINDOWHEIGHT//2, 30,30),'dir': random.choice([TOPLEFT,TOPRIGHT,DOWNLEFT,DOWNRIGHT])}
                        
                                              
                if bouncer_dic['rect'].right > WINDOWWIDTH-1 :
                        zeb3 = endgame(score)

                if zeb3 == False:
                        return False
                window.blit(ball_graphics(c) , bouncer_dic['rect'])
                bouncer_dic = normal_movement(bouncer_dic)
                away_ls = [ TOPRIGHT , DOWNRIGHT ]
                if bouncer_dic['rect'].left < WINDOWWIDTH//3 and bouncer_dic['dir'] not in away_ls :
                        if player_1.top  > bouncer_dic['rect'].top :
                                if player_1.top >= bouncer_dic['rect'].top-10:
                                        player_1.top -= MOVESPEED_COMPUTER
                        elif player_1.top < bouncer_dic['rect'].top :
                                if player_1.top <= bouncer_dic['rect'].top-10:
                                        player_1.top += MOVESPEED_COMPUTER
                for rectangle in rect_ls:
                        pygame.draw.rect(window, YELLO , rectangle)

                pygame.draw.rect(window, BLUE , player_1)
                pygame.draw.rect(window, GREEN , player_2)
                pygame.display.update()
                
                

def instructions():
        window.fill(BLACK)
        open_img = pygame.image.load('instructions_S.png')
        open_img = pygame.transform.scale(open_img , (WINDOWWIDTH,WINDOWHEIGHT))
        window.blit(open_img,window_rect)
        pygame.display.update()
        while True:
                for event in pygame.event.get():
                        if event.type==KEYDOWN:
                                if event.key==K_ESCAPE:
                                        return False
                                        pygame.quit()
                                        sys.exit()
                                if event.key==ord('p'):
                                        zeb1 = game()
                                        if zeb1 == False:
                                                return False

def start():
        pygame.mixer.music.load('background.wav')
        pygame.mixer.music.play(-1,0.0)
        window.fill(BLACK)
        open_img = pygame.image.load('open_img.png')
        open_img = pygame.transform.scale(open_img , (WINDOWWIDTH,WINDOWHEIGHT))
        window.blit(open_img,window_rect)
        drawtext('Press " Escape " to QUIT game',font,window,WINDOWWIDTH-80,WINDOWHEIGHT-100)
        drawtext('press " p " to Play',font,window,WINDOWWIDTH-80,WINDOWHEIGHT-50)
        pygame.display.update()
        while True:
                for event in pygame.event.get():
                        if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type==KEYDOWN:
                                if event.key==K_ESCAPE:
                                        return False
                                        pygame.quit()
                                        sys.exit()
                                if event.key==ord('p'):
                                        zeb = instructions()
                                        if zeb == False:
                                                return zeb
                                    

