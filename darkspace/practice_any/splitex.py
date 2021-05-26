a, b = map(int, input('').split())

print(a, b)

if a > b:
    print('>')
elif a == b:
    print('==')
elif a < b:
    print('<')

# a, b = map(int, input('').split())
# split() -> 공백을 기준으로 나눔
# map() -> map(함수, 자료형)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
# map()은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
# a, b = map(입력받은 값 (ex) '3 4' 를 공백을 기준으로 나누고, 그 각각의 원소를 정수형으로 변환
