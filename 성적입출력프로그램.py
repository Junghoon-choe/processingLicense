class Product:
    cnt = 0  # 클래스 변수. 제품의 개수 카운팅

    def __init__(self, name, price, amount):  # 객체가 생성 될때마다 호출된다.
        Product.cnt += 1  # 중복되지 않게 카운트해준다.
        self.num = Product.cnt
        self.name = name
        self.price = price
        self.amount = amount

    def printProduct(self):
        print('num:', self.num)
        print('name:', self.name)
        print('price:', self.price)
        print('amount:', self.amount)


class Dao:  # 저장소 : 저장, 검색, 수정, 삭제
    def __init__(self):  # 생성자로 리스트를 사용했다.
        self.prod = []

    def insert(self, p):  # 프로덕트
        print('제품추가. p는 Product 객체')
        self.prod.append(p)  # 파라메터로 받아온 프로덕트 객체를 추가해준다.

    def select(self, num):  # 제품번호로 검색하여 그 위치를 반환해준다.
        for idx, p in enumerate(self.prod):  # 반복문으로 제품의 인덱스와 내용을 가져올수 있게 선언해준다.
            if num == p.num:  # 파라메터값으로 받아온 숫자와 제품의 번호와 같으면
                return idx, p  # 해당 인덱스를 리턴으로 반환해준다.

    def update(self, p):  # 제품 가격만 수정
        print('제품 p를 번호로 찾아서 새 정보로 수정')  # 제품이 있는가 확인하고, 있다면 수정이 가능하게 구현,
        res = self.select(p.num)
        if res != None:
            res[1].price = p.price
        else:
            print("없는 제품")

    def delete(self, num):
        print('제품 번호로 찾아서 삭제')
        res = self.select(num)
        if res != None:
            del self.prod[res[0]]
        else:
            print("없는 제품")

    def selectAll(self):
        return self.prod


class Service:
    def __init__(self):
        self.dao = Dao()

    def addProduct(self):
        print('제품명, 가격, 수량 입력받아 Product객체 생성 후 dao.insert()로 추가')
        name = input("제품명 :")
        price = int(input("가격 :"))
        a = int(input("수랑 :"))

        self.dao.insert(Product(name, price, a))

    def getProduct(self):
        print('검색할 번호 입력받아 dao.select()로 검색')
        num = int(input("num :"))  # 제품 입력받아서
        res = self.dao.select(num)  # dao에서 찾을 수 있도록 .
        # 제품이 있는지 확인.
        if res == None:
            print('없는 제품')
        else:
            res[1].printProduct()

    def editProduct(self):
        print('수정할 제품 번호와 새 가격 입력받아 dao.update()로 수정')
        num = int(input("num :"))  # 제품 입력받아서
        price = int(input("new price :"))
        p = Product('', price, 0)
        p.num = num
        self.dao.update(p)

    def delProduct(self):
        print('삭제할 제품 번호 입력받아 dao.delete()로 삭제')
        num = int(input("num :"))  # 제품 입력받아서
        self.dao.delete(num)

    def printAll(self):
        print('dao.selectAll()로 전체 검색한 결과 출력')
        datas = self.dao.selectAll()
        for p in datas:
            p.printProduct()


prompt = """1. 추가
2. 검색
3. 수정
4. 삭제
5. 전체목록
6. 종료"""


class Menu:
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            print(prompt)
            nummber = int(input("숫자 입력 :"))
            if nummber == 1:
                self.service.addProduct()
            elif nummber == 2:
                self.service.getProduct()
            elif nummber == 3:
                self.service.editProduct()
            elif nummber == 4:
                self.service.delProduct()
            elif nummber == 5:
                self.service.printAll()
            elif nummber == 6:
                break


def main():
    m = Menu()
    m.run()


main()