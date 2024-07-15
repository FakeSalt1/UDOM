from pygame import*
from random import randint, choice
import time as timer


window_width = 555
window_height = 855
window = display.set_mode((window_width,window_height))

bg = transform.scale(image.load("Football_field.png"),(window_width,window_height))
fps = 60
font.init()
style = font.SysFont(None,50)
game = True
finnish = False

isResetBallPosition = False




class Character(sprite.Sprite):
    def __init__(self,filename,size_x,size_y,pos_x,pos_y, speed):
        super().__init__()
        self.filename = filename
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.image = transform.scale(image.load(self.filename),(self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(Character):
    def __init__(self,filename,size_x,size_y,pos_x,pos_y, speed,score):
        self.score = score
        super().__init__(filename,size_x,size_y,pos_x,pos_y, speed)
class BAlls(Character):
    def __init__(self,filename,size_x,size_y,pos_x,pos_y, speed,score):
        super().__init__(filename,size_x,size_y,pos_x,pos_y, speed)
        self.speed_x = speed * choice([1,-1])   
        self.speed_y = speed * choice([1,-1])  
        self.angle = 0
        self.rotate_speed = 100
        self.rotate_image = self.image
        self.rotate_rect = self.rotate_image.get_rect(center = (self.rect.x,self.rect.y)) 

    def update(self):
        if  self.rect.y > window_height-self.size_y:
            self.speed_y *= -1
        if  self.rect.y < 0:
            self.speed_y *= -1
        if self.rect.x > window_width-self.size_x:
            self.speed_x *= -1
        if self.rect.x < 0:
            self.speed_x *= -1

        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
    def rotate(self):
        self.angle += self.rotate_speed
        self.rotate_image = transform.rotate(self.image,self.angle)
        self.rotate_rect = self.rotate_image.get_rect(center =(self.rect.x, self.rect.y))
    def draw(self):
        window.blit(self.rotate_image,(self.rotate_rect.x, self.rotate_rect.y))
        draw.rect(window,(255,0,0),self.rect,2)


player1 = Player("rect.jpg",100,100,100,100,10,1)
player2 = Player("rect.jpg",100,100,100,755,10,1)
ball = BAlls("ufo.png",100,100,400,700,5,1)

clock = time.Clock()
while game:


    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(fps)
    window.blit(bg,(0,0))
    player1.draw()
    player2.draw()
    ball.draw()
    ball.rotate()
    text = style.render("Points P1:" + str(player1.score), True,(255,255,255))
    window.blit(text,(0,100))
    text = style.render("Points P2:" + str(player2.score), True,(255,255,255))
    window.blit(text,(0,200))
    if finnish == False:
        ball.update()
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]and player1.rect.x >50:
            player1.rect.x -= player1.speed
        if keys_pressed[K_d]and player1.rect.x <505: 
            player1.rect.x += player1.speed
            
        if keys_pressed[K_LEFT]and player1.rect.x >50:
            player2.rect.x -= player2.speed

        if keys_pressed[K_RIGHT]and player1.rect.x <505:
            player2.rect.x += player2.speed
        collide = sprite.collide_rect(player1, ball)
        if (collide):
            ball.speed_y *= -1
            isResetBallPosition = True
        collide = sprite.collide_rect(player2, ball)
        if (collide):
            ball.speed_y *= -1
            isResetBallPosition = True
        if isResetBallPosition:
            ball.rect.x =575
            ball.rect.x =275

        if ball.rect.y > window_height-ball.size_y:
            player1.score += 1
        if ball.rect.y < 0:
            player2.score += 1

        if player1.score > 5 :
            finnish = True
        if player2.score > 5 :
            finnish = True
    else:
        if player2.score > 5:
            text = style.render("PLAYER 2 WINS", True,(255,255,255))
            window.blit(text,(250,400))
        if player1.score > 5:
            text = style.render("PLAYER 1 WINS", True,(255,255,255))
            window.blit(text,(250,400))
    