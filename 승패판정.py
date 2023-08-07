import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((600, 600))
# 이미지 객체 생성
background_img = pg.image.load("bg.png")
background_img = pg.transform.scale(background_img,(600,600))

rock = pg.image.load("바위.png")
rock = pg.transform.scale(rock, (150, 150))

scissors = pg.image.load("가위.png")
scissors = pg.transform.scale(scissors, (150, 150))

paper = pg.image.load("보.png")
paper = pg.transform.scale(paper, (150, 150))

# 화면에 이미지 그리기
screen.blit(background_img, background_img.get_rect())
scissors_pos = screen.blit(scissors, (50, 100))
rock_pos = screen.blit(rock, (200, 100))
paper_pos = screen.blit(paper, (350, 100))

RSP = [rock, scissors, paper]

# 컴퓨터가 낼 손을 랜덤으로 결정
random_computer = random.choice(RSP)

running = True

while running:
    
    # 외부 이벤트 감지하기
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running= False
        elif event.type == pg.MOUSEBUTTONDOWN:

            #hand = None
            
            # 가위 이미지를 클릭한 경우
            if scissors_pos.collidepoint(pg.mouse.get_pos()):
                screen.blit(scissors, (80, 320))
                screen.blit(random_computer, (350, 320))


                ### (1) 가위 이미지를 클릭했을 때의 게임 결과를 출력하는 코드를 작성해 주세요.
                if random_computer == rock:
                    print("패배...")
                elif random_computer == scissors:
                    print("무승부!")
                else:

                    print("승리!")
                
            # 바위 이미지를 클릭한 경우
            elif rock_pos.collidepoint(pg.mouse.get_pos()):
                screen.blit(rock, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                ### (2) 바위 이미지를 클릭했을 때의 게임 결과를 출력하는 코드를 작성해 주세요.
                if random_computer == rock:
                    print("무승부!")
                elif random_computer == scissors:
                    print("승리!")
                else:
                    print("패배...")
            
            # 보 이미지를 클릭한 경우
            elif paper_pos.collidepoint(pg.mouse.get_pos()):
                screen.blit(paper, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                ### (3) 보 이미지를 클릭했을 때의 게임 결과를 출력하는 코드를 작성해 주세요.
                if random_computer == rock:
                    print("승리!")
                elif random_computer == scissors:
                    print("패배...")
                else:
                    print("무승부!")
                
    pg.display.update()
pg.quit()