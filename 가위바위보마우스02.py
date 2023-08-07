import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))

background = pg.image.load("bg.png")
background = pg.transform.scale(background,(600,600))

바위 = pg.image.load("바위.png")
바위 = pg.transform.scale(바위, (150, 150))

가위 = pg.image.load("가위.png")
가위 = pg.transform.scale(가위, (150, 150))

보 = pg.image.load("보.png")
보 = pg.transform.scale(보, (150, 150))

# 화면에 이미지 그리기
screen.blit(background, background.get_rect())

running = True
while running:

    가위위치 = screen.blit(가위, (50, 100))  # 가위 객체
    바위위치 = screen.blit(바위, (200, 100))  # 바위 객체
    보위치 = screen.blit(보, (350, 100))  # 보 객체

    # 외부 이벤트 감지하기
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        elif event.type == pg.MOUSEBUTTONDOWN:
            ### (1) 마우스로 가위 이미지를 클릭했을 때, "가위 클릭"을 출력해 주세요.
            if 가위위치.collidepoint(pg.mouse.get_pos()):
                print("가위 클릭")
            ### (2) 마우스로 바위 이미지를 클릭했을 때, "바위 클릭"을 출력해 주세요.
            elif 바위위치.collidepoint(pg.mouse.get_pos()):
                print("바위 클릭")
            ### (3) 마우스로 보 이미지를 클릭했을 때, "보 클릭"을 출력해 주세요.
            elif 보위치.collidepoint(pg.mouse.get_pos()):
                print("보 클릭")
            ### (4) 배경화면 이미지를 클릭했을 때, "배경화면 클릭"을 출력해 주세요.
            else:

                print("배경화면 클릭")
            
    pg.display.update()
pg.quit()