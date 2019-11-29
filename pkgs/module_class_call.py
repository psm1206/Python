#08module_class_call.py
# 폴더.폴더.모듈명     import 클래스명
from pkgs.module_class import CalcClass #as cc -> 지양, 클래스임을 확인하기 위해 혼선을 일어남.
#클래스메서드 : 클래스내에 정의된 메서드
#클래스.메서드명()로 호출
res = CalcClass.add(1, 2)
print(res)

import pkgs.module_def # class가 없으면 그냥 파일 자체가 class라고 생각하고 import해줌.
import pkgs.module_def as md # alias를 활용해 모듈명 줄이기.
# 폴더.폴더.모듈명   import 함수명
from pkgs.module_def import add, div# 원하는 함수들만 import해주고 싶을 때

res1 = pkgs.module_def.add(1, 4) #이렇게 한 번에 폴더.모듈명.함수명 해줘도 됨.
print(res1)

from pkgs.module_def import add
res2 = pkgs.module_def.div(4, 3) #[error] add만 사용하기로 import해줬는데 div를 사용하라고 하면 error
res3 = add(1, 4)

print(res2)
print(res3)
print(CalcClass.__dict__)
#생성자(constructor)함수 ex. CalcClass()
ox100 = CalcClass("Silver") #ox100에 클래스 CalcClass를 복제 떠서 그 곳의 주소를 넣어줌.
CalcClass.instanceMethod(ox100) #self가 들어간 메서드만 복제 뜸. self가 들어간 메서드를 사용하고 싶으면 무조건 복제 뜬 메서드의 주소를 알려줘야 함. 그래야 찾아감.
ox100.add2(1, 1, 3) # 이렇게 ox100라는 주소에 가서 add2 메서드를 실행해라!
# ox100.default_value11 = 1000 #인스턴스 ox100 에 default_value11 = 1000 이라는 것 추가.
# print(ox100.__dict__)
# ox200 = CalcClass()
# ox200.add2(2, 2) #[error] self 개념 등장!
# print(ox200.default_value) # 0
# print(ox200.__dict__)
# result = ox200.add2(1, 2)
# print(result)

#인스턴스 메서드 : self를 파라미터로 갖는 메서드
#반드시 생성자를 통해 주소를 만들어서 주소.메서드()로 호출함.
#주소는 4바이트(=32비트)로 표현함.

#__dict__ 인스턴스에 없으면 클래스에 가서 찾아본다. 인스턴스 우선!
# 클래스에도 없으면 부모(상속해준 곳)한테 찾아감.

