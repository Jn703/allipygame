import pygame as pg
pg.init()
screen=pg.display.set_mode((600,600))
pg.display.set_caption("엘리스 토끼의 파이게임")
background =pg.image.load("bg.png")
background= pg.transform.scale(background,(600,600))
rabbit= pg.image.load("토끼.png")
rabbit= pg.transform.scale(rabbit,(100,100))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, background.get_rect())
    screen.blit(rabbit, rabbit.get_rect())
    pg.display.update()
print("게임종료")
pg.time.sleep(1)
pg.quit()
