import pygame




pygame.init()


gamewidth = 1200
gameheight =700 

win = pygame.display.set_mode((gamewidth,gameheight))

pygame.display.set_caption("First Game")
# pygame.display.set_mode(self.game_scaled,RESIZABLE)
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png')]
FireBallRight = [pygame.image.load('FR1.png'),pygame.image.load('FR2.png'),pygame.image.load('FR3.png'),pygame.image.load('FR4.png'),pygame.image.load('FR5.png'),pygame.image.load('FR6.png'),pygame.image.load('FR7.png'),pygame.image.load('FR8.png')]
FireBallLeft = [pygame.image.load('FL1.png'),pygame.image.load('FL2.png'),pygame.image.load('FL3.png'),pygame.image.load('FL4.png'),pygame.image.load('FL5.png'),pygame.image.load('FL6.png'),pygame.image.load('FL7.png'),pygame.image.load('FL8.png')]
bg = pygame.image.load('BeachBackground.jpg')
char = pygame.image.load('S1.png')

clock = pygame.time.Clock()
score = 0


class player(object):
    
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y - self.height
        self.vel = 8
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x, self.y, 28,25)

        
    def draw(self,win):
        if self.walkCount + 1 >= 7:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x, self.y, 28,25)
        #pygame.draw.rect(win, (255,0,0),self.hitbox,2)
                

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.ShotCount = 0
        self.vel = 10 * self.facing
        self.hitbox = (self.x +20, self.y, 36,16)

    def draw(self, win):
        if self.ShotCount + 1 > 9:
            self.ShotCount = 0
        #pygame.draw.circle(win, self.color,(self.x,self.y), self.radius) #this line will need to be removed after pictures are added
        if self.facing == -1:
            win.blit(FireBallLeft[self.ShotCount//3],(self.x,self.y))
            self.ShotCount += 1
            self.hitbox = (self.x, self.y, 36,16)
        elif self.facing == 1:
            win.blit(FireBallRight[self.ShotCount//3],(self.x,self.y))
            self.ShotCount += 1
            self.hitbox = (self.x +20, self.y, 36,16)
        #pygame.draw.rect(win, (255,0,0),self.hitbox,2)
        #pygame.draw.ellipse(win, (255,0,0), self.hitbox, 2)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png')]
    walkLeft = [pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png')]
    def __init__(self,x,y,width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y - self.height
        self.hitbox = (self.x, self.y, 35,30)
        self.start = 0
        self.end = gamewidth - self.hitbox[2]
        self.path = [self.start, self.end]
        self.walkCount = 0
        self.vel = 3
        self.health = 10
        self.visible = True
        
    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 12:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] -20, 50, 10))
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] -20, 50 - (50/10) * (10 - self.health),  10))
            self.hitbox = (self.x, self.y, 35,30)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        
            
                     
        
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0            

    def hit(self):
        if self.health > 0:
            self.health -=1
        else:
            self.visible = False
            print(pikachu.x)
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
def redrawGameWindow():
    
    win.blit(bg, (0,gameheight - bg.get_height()))
    text = font.render('Score: ' + str(score), 1, (0,255,0))
    win.blit(text, (0, 10))
    cat.draw(win)
    #if pikachu.health > 0:
    if pikachu.health < 1:
        restartButton.draw(win,(0,0,0))
    pikachu.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
    
#mainloop
font = pygame.font.SysFont('comicsans',30,True,True)
cat = player(50, gameheight, 20, 15)
pikachu = enemy(100,gameheight,64,64)
restartButton = button((0,255,0),150,225,250,100,'Restart')
restartGame = True
while restartGame:
    pikachu.health = 10
    pikachu.visible = True
    score = 0
    shootLoop = 0
    bullets = []
    run = True
    restartGame = False
    while run and not restartGame:
        clock.tick(18)



        if shootLoop > 0:
            shootLoop +=1
        if shootLoop >3:
            shootLoop = 0
            
        
        #pygame.time.delay(25)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restartButton.isOver(pos):
                    restartGame = True
                    print('clicked the button')
                    print(pikachu.health)

        for bullet in bullets:

            if bullet.hitbox[1] < pikachu.hitbox[1] + pikachu.hitbox[3] and bullet.hitbox[1]+bullet.hitbox[3] > pikachu.hitbox[1]:
                if bullet.hitbox[0] + bullet.hitbox[2] > pikachu.hitbox[0] and bullet.hitbox[0] < pikachu.hitbox[0] + pikachu.hitbox[2] and pikachu.visible:
                   pikachu.hit()
                   score += 1
                   bullets.pop(bullets.index(bullet))
            
            if bullet.x <500 and bullet.x >0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]and shootLoop == 0:
            if cat.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 10:
                if cat.left:
                    bullets.append(projectile(round(cat.x + cat.width //2)-50,round(cat.y + cat.height //2), 6, (150,0,0), facing))
                else:
                    bullets.append(projectile(round(cat.x + cat.width //2),round(cat.y + cat.height //2), 6, (150,0,0), facing))
            shootLoop = 1

        if keys[pygame.K_LEFT] and cat.x > cat.vel:
            cat.x -= cat.vel
            cat.left = True
            cat.right = False
            cat.standing = False
        elif keys[pygame.K_RIGHT] and cat.x < gamewidth - cat.width - cat.vel:
            cat.x += cat.vel
            cat.right = True
            cat.left = False
            cat.standing = False
        else:
            cat.standing = True
            cat.walkCount = 0
            
        if not(cat.isJump):
            #if keys[pygame.K_UP] and y > vel:
            #   y -= vel
            #if keys[pygame.K_DOWN] and y < gameheight - height - vel:
            #    y += vel
            if keys[pygame.K_UP]:
                cat.isJump = True
                #cat.right = False
                #cat.left = False
                cat.walkCount = 0
        else:
            if cat.jumpCount >= -10:
                neg = 1
                if cat.jumpCount < 0:
                    neg = -1
                cat.y -= (cat.jumpCount ** 2) *.5 * neg
                cat.jumpCount -= 1
            else:
                cat.isJump = False
                cat.jumpCount = 10
        if pikachu.health < 1:
            restartButton.draw(win,(0,0,0))
        redrawGameWindow()


pygame.quit()
    

                         
