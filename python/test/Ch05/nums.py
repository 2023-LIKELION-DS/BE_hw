# 5장실습

# 5-6

a = 2
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)        # 몫 아님

print(a ** b)       # 제곱승

print((a+b) * b)

print(a // b)       # 몫
print(a % b)        # 나머지

#실수(float)

x = 0.6
y = 0.3
z = 1

print("실수와 실수의 연산 -> 실수로 나타난다@@@@")
print(x + y)
print(x - y)
print(x * y)
print(x / y)

print("실수와 정수의 연산 -> 실수로 나타난다")
print(x + z)
print(x - z)
print(x * z)
print(x / z)

#실수와 연산하는 수는 그 결과가 모두 실수이다. 




# 5-7

price = 123_900_000_000  # 숫자 3 자리마다 언더스코어를 넣어 표기 가능
print(price)            # 출력값에서 _ 는 생략된다.


# 상수 contants

PI = 3.141592       # 다른 데이터 덮어쓰기 하면 X

PI = 1.23           # 이런식으로 작성 X

print(PI) 


# 5-8

#문자열-숫자간 변환

a = 100
b = "100"
# 위의 두 값을 컴퓨터는 동일한 100으로 인식하지 않는다. 
c = "0.456"

a = str(a)  # 숫자를 문자열로
b = int(b)  # 문자열을 숫자로 
c = float(c) # 숫자로 . 데이터가 동일한지 비교할 때 유용하다.




# 5-9

# 논리형 데이터 bool, boolean
# 대문자로 시작하는 키워드 

# True
# False 

print(3>2)
print(3==3)
print(3==3.0)
print(3 is 3.0)    # 데이터형 구분. 정수와 실수라서 False 결과 나옴
