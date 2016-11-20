import pygame, sys,random,time
from pygame.locals import *
import constants

pygame.init()


height=768
width=1366
font=pygame.font.SysFont(None,28)
font1=pygame.font.SysFont(None,32)
font2=pygame.font.SysFont(None,20)
font3=pygame.font.SysFont(None,16)


def waitforplayer():
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
                                else:   
                                        return

                        
def endgame(score):
        surface.fill((0,0,0))
        if score > constants.__ALIEN_HIGH:
                constants.__ALIEN_HIGH = score
        end=pygame.Rect(305,0,740,740)
        endimg=pygame.image.load('endimg.png')
        endimg=pygame.transform.scale(endimg,(740,740))
        surface.blit(endimg,end)
        drawtext("HIGH SCORE:"+str(constants.__ALIEN_HIGH),font1,surface,450,550)
        drawtext("YOUR SCORE:"+str(score),font1,surface,450,580)
        drawtext('Press " Escape " to QUIT game',font2,surface,450,610)
        drawtext('         " p " to PLay Again',font2,surface,450,640)
        pygame.display.update()
        surface.fill(black)
        while True:
                for event in pygame.event.get():
                        if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type==KEYDOWN:
                                if event.key==K_ESCAPE:
                                        pygame.mixer.music.stop()
                                        return False
                                        pygame.quit()
                                        sys.exit()
                                if event.key==ord('p'):
                                        gameloop()


                                        
def drawtext(text,font,surface,x,y):
        textobj=font.render(text,1,(255,50,50))
        textrect=textobj.get_rect()
        textrect.topright=(x,y)
        surface.blit(textobj,textrect)


mainclock=pygame.time.Clock()
surface=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
pygame.display.set_caption('Save Earth')
bg=(255,255,255)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

        
def gameloop():
        blocks=[]
        blocksimg=[]
        bullets=[]
        score=0
        blockcounter=0
        newblock=50
        moveleft=False
        moveright=False
        fire=False
        jet=pygame.Rect(width//2-25,height-80,50,80)
        jetimage=pygame.image.load('plane.png')
        jetimagestr=pygame.transform.scale(jetimage,(50,80))
        jetimage2=pygame.image.load('plane2.png')
        jetimagestr2=pygame.transform.scale(jetimage2,(50,80))
        logo=pygame.Rect(305,0,50,50)
        logoimg=pygame.image.load('logo.png')
        logoimg=pygame.transform.scale(logoimg,(768,768))
        bl1=pygame.image.load('brick1.jpg')
        bl2=pygame.image.load('brick2.jpg')
        bl1imagestr=pygame.transform.scale(bl1,(40,40))
        bl2imagestr=pygame.transform.scale(bl2,(40,40)) 
        movespeed=12
        bulspeed=12
        sound=pygame.mixer.Sound('bullete.wav')
        pygame.mixer.music.load('background.wav')
        pygame.mixer.music.play(-1,0.0)
        musicplaying=True
        surface.blit(logoimg,logo)
        drawtext('Press any Key to start game..',font1,surface,450,550)
        drawtext("YOU HAVE 60 SECONDS  TO SAVE THE EARTH",font,surface,500,600)
        pygame.display.update()
        r = waitforplayer()
        if r == False:
                pygame.mixer.music.stop()
                return False
        surface.fill(black)
        strt=pygame.image.load('start.jpg')
        strt=pygame.transform.scale(strt,(740,740))
        surface.blit(strt,pygame.Rect(305,0,740,740))
        pygame.display.update()
        waitforplayer()
        surface.fill(bg)
        for i in range(15):
                blocks.append((pygame.Rect(random.randint(0,width-40),random.randint(40,height-200),40,40),random.randint(1,2)))
        a=time.time()
        count=0
        bullet_count=1000
        while True:
                for event in pygame.event.get():
                        if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type==KEYDOWN:
                                if event.key==K_LEFT or event.key==ord('a'):
                                        moveleft=True
                                if event.key==K_RIGHT or event.key==ord('d'):
                                        moveright=True
                                if event.key==K_UP or event.key==ord('w'):
                                        fire=True
                                if event.key==K_ESCAPE:
                                        r = endgame(score)
                                        if r == False:
                                                return False
                                        pygame.quit()
                                        sys.exit()
                        if event.type==KEYUP:
                                if event.key==K_LEFT or event.key==ord('a'):
                                        moveleft=False
                                if event.key==K_RIGHT or event.key==ord('d'):
                                        moveright=False
                                if event.key==K_UP or event.key==ord('w'):
                                        fire=False
                                if event.key==ord('m'):
                                        if musicplaying:
                                               pygame.mixer.music.stop()
                                        else:
                                                pygame.mixer.music.play(-1,0.0)
                                        musicplaying=not musicplaying
                                        
                blockcounter+=1
                if blockcounter>=newblock:
                        blockcounter=0
                        blocks.append((pygame.Rect(random.randint(0,width-40),random.randint(40,height-200),40,40),random.randint(1,2)))
                surface.fill(bg)
                bt=time.time()
                drawtext('Bullets : {0} Time :{1}s  Score: {2}'.format(bullet_count,int((bt-a)//1),score),font,surface,width,0)
                if moveleft and jet.left>0:
                        jet.left-=movespeed
                if moveright and jet.right<width:
                        jet.right+=movespeed
                if fire:
                        if bullet_count==0:
                                pass
                        else:
                                sound.play()
                                bullets.append(pygame.Rect(jet.left,jet.top-5,3,5))
                                bullets.append(pygame.Rect(jet.right-3,jet.top-5,3,5))
                                bullet_count-=1
                for i in range(len(bullets)):
                        (bullets[i]).bottom-=bulspeed
                for block in blocks:
                        for b in bullets:
                                if block[0].colliderect(b):
                                        if block[1]==1:
                                                score+=1
                                        else:
                                                score+=2
                                        if block in blocks:
                                                blocks.remove(block)
                                        bullets.remove(b)
                                        #score+=1
                for b in bullets:
                        if b.top<0:
                                bullets.remove(b)
                if fire==True:
                        surface.blit(jetimagestr2,jet)
                else:
                        surface.blit(jetimagestr,jet)
                count+=1
                if count==80:
                        count=0
                        for i in range(len(blocks)):
                                (blocks[i][0]).bottom+=40
                                if (blocks[i][0]).bottom>height:
                                        r = endgame(score)
                                        if r == False:
                                                return False        
                for bo in blocks:
                        t=[bl1imagestr,bl2imagestr]
                        surface.blit(t[bo[1]-1],bo[0])
                for i in range(len(bullets)):
                        pygame.draw.rect(surface,green,bullets[i])
                pygame.display.update()
                mainclock.tick(80)
                if int((bt-a)//1)==60:
                        break
        r = endgame(score)
        if r == False:
                return False

		
					
		
		


