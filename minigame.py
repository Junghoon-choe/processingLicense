import PySimpleGUI as ui

global w

# w = ui.Text("테스트야")
#
# ui.Window(title="Game", layout=[[w]], margins=(800, 500)).read()

import random


#
# # 문제 풀기
# def solve_test():
#     check = [False] * 20
#     for i in range(0, 20):
#         while True:
#             # 20개 랜덤으로 돌려서 num에 저장
#             num = random.randrange(0, 20)
#             if check[num] == False:
#                 check[num] = True
#                 break
#         u = open('{}번.txt'.format(num), 'r', encoding='utf-8')
#         # 5번째줄까지만 보여줌
#         for i in range(5):
#             line = u.readline()
#             print(line)
#
#         answer = int(input("answer:"))
#
#     u.close()
#
#
# solve_test()


# 문제 쫙 보여주는 함수
def check_test():
    check = [False] * 20
    print("========================================정답확인=========================================")
    for i in range(0, 20):
        while True:
            num = random.randrange(0, 20)
            if check[num] == False:
                check[num] = True
                break
        u = open('{}번.txt'.format(num), 'r', encoding='utf-8')
        str1 = u.read()
        print(str1)

    u.close()


check_test()
