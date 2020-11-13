import sys
import os

prompt = """1. 파일 읽기
2. 파일 쓰기
3. 파일 삭제
4. 파일 전체 삭제
5. 종료"""


# 1. 읽기 (읽고 싶은 파일을 선택 할 수 있게 구현하기.)
def readFile():
    print("\n파일 읽기!\n")
    print(os.listdir(os.getcwd()), '\n')
    fname = input('파일명을 입력해 파일을 선택하세요 :')

    if os.path.isfile(fname):
        file = open(fname, 'r', encoding='utf-8')
        print('\n', file.read(), '\n')
    else:
        print('\n\t파일명을 다시 확인해주세요!!\n')


# 2. 쓰기 (파일명을 입력받는데, 중복이 되면 안됨. 중복이되면 다시 입력 할 수 있게끔,
# 또는 새로쓰게하거나, 이어쓰거나)
# 무한루프로 계속 파일 작성 할 수 있게 구현하기. /exit > 종료 > 저장
def writeFile():
    print("\n파일 쓰기!\n")
    arr = []
    file_name = input("\"뒤로가기\"를 입력하면 메뉴창으로 이동합니다\" \n제목 :")
    if os.path.isfile(file_name):
        print("\n\t같은 파일명을 갖고 있는 파일이 존재합니다.\n\t파일명을 바꿔주세요.\n")
        return
    elif file_name == "뒤로가기":
        return

    print("""(작성을 완료 하려면 "/끝"을 입력하세요!!)\n""")
    while True:
        string = input()
        if string == "/끝":
            break
        arr.append(string + '\n')

    file = open(file_name, "w")
    file.writelines(arr)
    file.close()


# 3. 삭제 () (파일 목록 > 삭제 > 파일 선택 > 파일 삭제)
def removeFile():
    print("\n파일 삭제!\n")
    print(os.listdir(os.getcwd()))
    file_name = input("\n어떤 파일을 삭제 하시겠습니까? :")
    if os.path.isfile(file_name):
        os.remove(file_name)
        print('\t', "\"", file_name, "\"파일이 삭제 되엇습니다!\n")
    else:
        print('\n\t파일명을 다시 확인해주세요!!\n')


# 4. clear (파일 전체 삭제)
def removeFileAll():
    print("\n파일 전체 삭제!\n")
    for i in os.listdir(os.getcwd()):
        os.remove(i)


# 5. 종료
def exit():
    print("\n종료!\n")
    sys.exit(0)


if not os.path.isdir("../test_dir/파일"):
    os.mkdir("../test_dir/파일")
os.chdir("../test_dir/파일")  # 디렉토리를 바꿔줌
print("현재 :", os.getcwd())
# 리스트에 파일들을 담놓고 컨트롤 할 수 있다.
while True:

    print(prompt)
    number = int(input("숫자 입력 :"))
    if number == 1:
        readFile()
    elif number == 2:
        writeFile()
    elif number == 3:
        removeFile()
    elif number == 4:
        removeFileAll()
    elif number == 5:
        exit()
