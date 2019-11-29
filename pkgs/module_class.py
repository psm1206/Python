#08module_class.py
#SDK, JDK // Development toolKit : DK를 기반으로 프로그램을 쌓을 수 있음.
#OOP(Oject Oriented Program) : 객체 지향 프로그램
# 존재하는 것 중에 Language로 표현할 수 있는 것들 ex. 김태희가 죽자고 예쁘다. // 김태희, 예쁘다는 표현할 수 있겠지만 죽자고는 표현할 수가 없다..
# 클래스 / 변수 : 값 / 메서드(함수) : 동작
# 인스턴스: 객체가 주소를 갖는 것 = 메모리에 올라오는 것
# 파이썬은 메모리라는 말 대신에 네임 스페이스라는 말을 사용함.
from pkgs.module_parent import ParentClass
    #CalcClass() 여기 괄호 안에 부모 클래스명 적어주면 상속!
class CalcClass(ParentClass): # 자식 클래스 CalcClass, 부모 클래스 ParentClass // ParentClass것을 상속 받겠음.
    def __init__(self, prm_grade): # CalcClass(): #이게 기본으로 탑재되어 있고 아래와 같이 각각 변수를 만들어주고 싶을 때 사용하는 건가? #파이썬은 주소를 self에 담아줌. #초기화의 목적 : 메모리에 새롭게 올리기 위함.
        # super(CalcClass, self).__init__()
        ParentClass.__init__(self) # 메모리 주소 만들어서 그 주소 올려놔.
        self.grade = prm_grade #각 인스턴스에 다른 prm_grade 생성, 모든 변수들을 Key:Value로 관리함.
        print("CalcClass 생성자 메서드 호출", self) #생성자를 만드는 이유는 초기화 하기 위함.
    default_value = 0
    # 오버라이딩(over riding) : 상속 개념에서만 존재함.
    # 메서드의 선언부가 같고 내용을 달리할 수 있는 메서드
    def instanceMethod(self): # self 자리에는 주소가 들어감.
        print("--------------overriding-----------------")
        print("ChildClass ---ParentClass instanceMethod())")
    def add2(self, a, b): #인스턴스 메서드 : self를 파라미터로 갖는 메서드
        list = []
        list.append(a)
        print(list)
        return a+b
    def add2(self, a, b, c): # 파이썬은 같은 이름의 함수가 두 개 있어도 실행한다. 이유는 아래와 같다. 대체로 다른 언어는 X
        # 메서드의 이름이 키이름이 된다. 그래서 같은 이름의 메서드를 여러 개쓰면 가장 아래에 적은 메서드가 다 덮어버린다.
        # 오버로딩 : 이름은 같고 파라미터는 다른 것. 개념 상의 오버로딩은 있지만 실제로는 일어나지 않는다.
        # 파이썬에서는 모든 객체를 name space로 관리하는데 또한 dict타입으로 관리하고 메서드 이름이 곧 키 이름이 된다.
        list = []
        list.append([a, b, c])
        print(list)
        return a+b
    def add(a, b):
        return a+b
    def div(a, b):
        return a/b
    def mul(a, b):
        return a*b

if __name__ =="__main__":   #
    print(CalcClass.__dict__)
    print(dir())  #현재 파일에서 정의된 모듈명을 출력하라.
#-----------------------------------------
# res = CalcClass.add(1, 2)
# print(res)

# class UserClass:              #하나의 py파일에는 class가 여러 개 올 수 있으나, 하나 넣는 걸 추천.
#     def login(id, pw):
#         return "홍길동"

# 상속은 내 것인양 갖고 와 내 마음대로 뜯어 고치고 수정하는 것을 말함.
# import 개념은 rental
# call이란 다른 파일에서 데리고 오는 것!