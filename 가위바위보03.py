import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((600, 600))

# 이미지 객체 생성
background_img = pg.image.load("background.png")

rock = pg.image.load("rock.png")
rock = pg.transform.scale(rock, (150, 150))

scissors = pg.image.load("scissors.png")
scissors = pg.transform.scale(scissors, (150, 150))

paper = pg.image.load("paper.png")
paper = pg.transform.scale(paper, (150, 150))

click = pg.image.load("여기클릭.png")
click = pg.transform.scale(click, (150, 100))

# 화면에 이미지 그리기
screen.blit(background_img, background_img.get_rect())
scissors_pos = screen.blit(scissors, (50, 100))
rock_pos = screen.blit(rock, (200, 100))
paper_pos = screen.blit(paper, (350, 100))
click_pos = screen.blit(click, (400, 0))

RSP = [rock, scissors, paper]

### (1) RSP 리스트를 활용하여 랜덤 값을 가져와 random_computer 변수에 저장해 주세요.
random_computer = random.choice(RSP)

running = True
while running:

    # 외부 이벤트 감지하기
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:

            if click_pos.collidepoint(pg.mouse.get_pos()):
    
                ### (2) 이미지를 클릭했을 때 랜덤으로 결정된 컴퓨터의 손 모양을 출력해 주세요.
                if random_computer == rock:
                    print("상대방의 손 : 바위")
                if random_computer == scissors:
                    print("상대방의 손 : 가위")
                if random_computer == paper:
                    print("상대방의 손 : 보")
                
                
    pg.display.update()

            