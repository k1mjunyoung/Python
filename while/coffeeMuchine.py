from bdb import Breakpoint


coffee = 10

while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피 판매")
        coffee -= 1
    elif money > 300:
        print("커피 판매, %d원 반환" % (money-300))
        coffee -= 1
    else:
        print("판매 실패, %d원 반환" % money)

    if coffee == 0:
        print("커피 매진")
        break