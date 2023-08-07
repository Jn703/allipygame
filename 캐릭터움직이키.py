import pygame as pg
pg.init()
screen=pg.display.set_mode((600,600))
pg.display.set_caption("엘리스 토끼의 파이게임")
배경 =pg.image.load("bg.png")
배경= pg.transform.scale(배경,(600,600))
토끼= pg.image.load("토끼.png")
토끼= pg.transform.scale(토끼,(100,100))
토끼좌표= 토끼.get_rect()
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key==pg.K_RIGHT:
                토끼좌표.x +=5
            elif event.key== pg.K_LEFT:
                토끼좌표.x -=5
            elif event.key== pg.K_UP:
                토끼좌표.y -= 5
                
            elif event.key== pg.K_DOWN:
                토끼좌표.y +=5
    screen.blit(배경, 배경.get_rect())
    screen.blit(토끼, 토끼좌표)
    pg.display.update()
print("게임종료")
pg.quit()

