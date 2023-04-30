# 8장
# 8-1 함수 functions

# 매개변수(파라미터) ; 함수 정의에 쓰인 것
# 인자 (인수) ; 함수 실행시 들어간 값

# 여러 프로그램에 걸쳐서 사용할 수 있는 효율이 있다. 
def print_name(name):      #함수 선언, name은 파라미터
    print(f'이름은 {name}입니다')     


# "김멋사", "이멋사" 는 인자(인수)이다.
print_name("김지민") 
print_name("김멋사") 



def print_ex_string():
    print('예시 문자열 입니다. ')

print_ex_string()       # 만든 함수 콜   



# 여러개의 인자
def print_name_age(name, age):      #함수 선언, name은 파라미터
    print(f'이름은 {name}이고, 나이는 {age}살 입니다')
    
print_name_age("김지민", "23")
# print_name_age() # 인자가 없으면 오류난다. 

    
    
    
    
    
    
# 8-2 함수(2)

def order_coffee(qty, option='hot'):
    print(f'{qty}잔 / {option}')
    
order_coffee(3, 'iced')     # 다른 겂
order_coffee(3)             # 기본 값 출력
order_coffee(option='iced', qty=5)      # 각각 선언을 한다면 순서 바꿔도 괜찮다.









# 8-3 함수(3)

def get_id(email):
    
    if email.endswith('@test.com'):
        email_id = email.removesuffix('@test.com')
        print(email_id)
        return email_id         # 반한하고자 하는 데이터를 정해주어야 함
    else:
        print('처리할 수 없는 이메일 주소입니다.')

user_id = get_id('user@duksung.com')
print(user_id)
user_id = get_id('user@test.com')
print(user_id)

