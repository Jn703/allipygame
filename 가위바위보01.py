import random

data = ["가위", "바위", "보"]

### (1) random.choice() 함수를 사용하여 엘리스 토끼의 값을 랜덤으로 결정해 주세요.
rabbit = random.choice(data)

# 여러분이 도도새의 입장이 되어 원하는 패를 입력해요.
dodo = input("가위, 바위, 보 중 한 가지를 골라 입력해 주세요. ")

print("\n===게임 결과===")

### (2) 조건문을 사용하여 승, 무, 패를 판단하고, 결과를 출력해 주세요.
if rabbit == "가위": # 엘리스토끼가 가위를 낸 경우
    if dodo == "가위":
        print("무승부!")
    elif dodo == "바위":
        print("승리!")
    elif dodo == "보":
        print("패배...")

elif rabbit == "바위": # 엘리스토끼가 바위를 낸 경우
    if dodo == "가위":
        print("패배...")
    elif dodo == "바위":
        print("무승부!")
    elif dodo == "보":

        print("승리!")
        
elif rabbit == "보": # 엘리스토끼가 보를 낸 경우
    if dodo == "가위":
        print("승리!")
    elif dodo == "바위":
        print("패배...")
    elif dodo == "보":
        print("무승부!")



print("엘리스 토끼가 낸 값: "+ rabbit + "   도도새가 낸 값: "+ dodo)