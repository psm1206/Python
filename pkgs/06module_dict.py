#06module_dict.py
lists = []
# lists = list() 위와 같음.
lists.append("1")
print(lists, type(lists))

books = {}
# books = dict() 위와 같음.
books["price"] = 1000
print(books, type(books))

tpl = ("1", 2, 3)
# tpl = tuple()
print(tpl, type(tpl))

str = "{'price': 1000}"
print(str, type(str))

# *args(argument) : *(tuple) (인자/파라미터/매개변수)
# **kwargs(keyword argument) : **(dictionary)

# 함수 : 입력에 의해 동일한 결과를 내는 기능
# 이름(파라미터1, 파라미터2, ...) : print()
# 호출 : 기존의 함수를 사용하는 것

# 대입 : 호출할 때 값을 함수의 파라미터로 넣는 것
# def add(n1, n2, n3):
#   return n1 + n2 + n3
# add(1, 2, 3)

def add(n1, n2):    #파이썬은 따로 자료형을 정해주지 않아도 됨.
    return n1 + n2

res = add(1, 2)
print(res)

def add(n1, n2):
    res1 = n1 + n2
    res2 = n1 * n2
    res3 = "ABC"
    return res1, res2, res3
(r1, r2, r3) = add(1, 2)
print(r1, r2, r3)

def listPrint(num, *book_list):     # 일반 변수, *, ** 순서대로 써야 함.
    print(book_list)                # *, **는 타입, 개수 제한을 받지 않고 값을 받음. 0개부터 n개!
bb = ["11", "bb", "cc"]
listPrint(1, 2, 3, 4, 5)

def dicPrint(**dic):
    print(dic)
aa = {"uid":"kim", "upw":"111"} #양따옴표로 만들었는데 홑따옴표로 출력된다? dictionary!
# dicPrint(aa)    error
dicPrint(uid="kim", upw="111") # key=value로 줘야하고 키값에 따옴표 붙이면 안 됨.

def tpldicPrint(str, num, *t, **d):

    print(num, t, d)
tpldicPrint(1, 2, (3, 4), uid="kim", upw="111") # 2 (3,) {'uid': 'kim', 'upw': '111'}
tpldicPrint([1, 2, 3], 2, uid="kim", upw="111") # 2 () {'uid': 'kim', 'upw': '111'}

# naming rule : PEP8(Python Enhancement Proposal)
# 메서드 이름 : listPrint
# 클래스 이름 첫글자는 대문자 : ShopCart
# 소문자 : 메서드 이름 규칙을 따름.
# 패키지 : 소문자 _ - 사용
# 상수 : 대문자 DEFAULT

tuple1 = (1, 2, 3)
tuple[0]
dict1= {"asdf":"sdf",  }
dict1["asdf"]

