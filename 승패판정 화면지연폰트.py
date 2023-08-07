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

RSP = [rock ,scissors, paper]

# 컴퓨터가 낼 손을 랜덤으로 결정
random_computer = random.choice(RSP)

# 폰트 객체 생성
font_path = "C:/Windows/Fonts/malgun.ttf"
font = pg.font.Font(font_path, 60)

# 승.무.패에 대한 Surface 객체 생성
text_surface_win = font.render("승리!", True, (0, 255, 0), None)
text_surface_lose = font.render("패배...", True, (255, 0, 0), None)
text_surface_tie = font.render("무승부!", True, (0, 0, 0), None)

running = True


while running:
    
    # 화면에 이미지 그리기
    screen.blit(background_img, background_img.get_rect())
    scissors_pos = screen.blit(scissors, (50, 100))
    rock_pos = screen.blit(rock, (200, 100))
    paper_pos = screen.blit(paper, (350, 100))
    
    # 외부 이벤트 감지하기
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running= False
        elif event.type == pg.MOUSEBUTTONDOWN:
        
            # 가위 이미지를 클릭한 경우
            if scissors_pos.collidepoint(pg.mouse.get_pos()):
                screen.blit(background_img, background_img.get_rect())
                
                screen.blit(scissors, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                if random_computer == rock:
                    screen.blit(text_surface_lose, (200, 150))
                elif random_computer == scissors:
                    screen.blit(text_surface_tie, (200, 150))
                else:
                    screen.blit(text_surface_win, (200, 150))
                
                pg.display.update()
                pg.time.wait(3000)
                #running = False
                random_computer = random.choice(RSP)
                
            # 바위 이미지를 클릭한 경우
            elif rock_pos.collidepoint(pg.mouse.get_pos()):
                screen.blit(background_img, background_img.get_rect())
                
                screen.blit(rock, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                if random_computer == rock:
                    screen.blit(text_surface_tie, (200, 150))
                elif random_computer == scissors:
                    screen.blit(text_surface_win, (200, 150))
                else:
                    screen.blit(text_surface_lose, (200, 150))
                
                pg.display.update()
                pg.time.wait(3000)
                #running = False
                random_computer = random.choice(RSP)
                
            # 보 이미지를 클릭한 경우
            elif paper_pos.collidepoint(pg.mouse.get_pos()):
                screen.blit(background_img, background_img.get_rect())
                
                screen.blit(paper, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                if random_computer == rock:
                    screen.blit(text_surface_win, (200, 150))
                elif random_computer == scissors:
                    screen.blit(text_surface_lose, (200, 150))
                else:
                    screen.blit(text_surface_tie, (200, 150))
                
                pg.display.update()
                pg.time.wait(3000)
                #running = False
                random_computer = random.choice(RSP)
                
    pg.display.update()
    
pg.quit()