import pygame as pg
pg.init()
screen=pg.display.set_mode((600,600))
pg.display.set_caption("엘리스 토끼의 파이게임")
background =pg.image.load("bg.png")
background= pg.transform.scale(background,(600,600))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, background.get_rect())
    pg.display.update()

pg.quit()

  
'''import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
pg.display.set_caption("엘리스 토끼의 파이게임")

background = pg.image.load("bg.png")
background = pg.transform.scale(background, (600, 600))  # 이미지 크기 조정

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pg.display.update()

pg.quit()
'''