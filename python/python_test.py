
"""
덕성 아기사자 김지민 과제 입니다!~ 

파이썬 문제풀이 과제 파일입니다. (마감기한: ~ 5/8 17:00)


                                        ##### 문제 1 #####

딕셔너리에 국어: 87, 수학: 88, 영어: 92, 과학: 67, 사회: 72 를 저장하고 평균을 구하시오.
"""
### 문제1 답안 (이 아래에 적어주세요!)
print("[문제 1]")

subjects = {
    "국어": 87, 
    "수학": 88,
    "영어": 92,
    "과학": 67,
    "사회": 72   
}
print("점수의 총 합은 " + str(sum(subjects.values())) + " 이고,")

print("총 과목의 수는 " + str(len(subjects.keys())) + " 이므로,")

print("평균은 "+ str(sum(subjects.values())/len(subjects.keys())) + " 입니다.")










"""
                                        ##### 문제 2 #####

food = ["김밥", "라면", "튀김", "떡볶이", "순대"]

위 리스트의 요소를 아래와 같은 형식으로 순서대로 출력하시오. 

오늘의 메뉴: 김밥
오늘의 메뉴: 라면
오늘의 메뉴: 튀김
오늘의 메뉴: 떡볶이
오늘의 메뉴: 순대

"""
### 문제2 답안 (이 아래에 적어주세요!)
print("[문제 2]")

food = ["김밥", "라면", "튀김", "떡볶이", "순대"]

i = 0
for i in food :
    print( "오늘의 메뉴: " + i)	










""" 
                                        ##### 문제 3 #####

통장에 10,000원이 들어있다.
사용자로부터 '출금'과 '입금' 중 하나를 입력받고, 입출금시 금액 부분을 입력 받도록 하시오.

입금을 하면 "ㅇㅇㅇ원이 입금되었습니다. 현재 잔고는 ㅇㅇㅇ입니다." 출력
출금을 하면 "ㅇㅇㅇ원이 출금되었습니다. 현재 잔고는 ㅇㅇㅇ입니다." 출력

출금시에 잔고가 부족하면 "현재 잔고 부족입니다. ㅇㅇㅇ원이 부족합니다." 라고 출력
통장잔고가 0원이 되면 "통장을 파기합니다" 출력

사용자로부터 종료 받기 전까지 무한 반복하는 코드 작성



(((( 출력 결과 예시 참고 )))

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 1
금액: -2
금액을 0보다 크게 적으세요.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 1
금액: 5000 
5000원이 입금되었습니다. 현재 잔고는 15000원 입니다.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 2
금액: 3000
3000원이 출금되었습니다. 현재 잔고는 12000원 입니다.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 2
금액: 15000
현재 잔고 부족입니다. 3000원이 부족합니다.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 2
금액: 12000
통장을 파기합니다.

"""
### 문제3 답안 (이 아래에 적어주세요!)
print("[문제 3]")

print("현재 잔금은  10,000원입니다. ")
money = 10000

while True:

    bank = input("입금이라면 '입금'을, 출금이라면 '출금'을 입력해주세요 :   ")
    myMoney=money
    
    if bank == '입금':
        print ("'입금'을 입력하셨습니다.")
        money_in = input("금액을 입력해주세요 :    ")
        print (money_in + " 이 입금되었습니다.")
        money_sum = int(money_in) + myMoney
        print ("현재 잔금은" + str(money_sum) + " 원입니다.")
        money=money_sum

    elif bank == '출금':
        print("'출금'을 입력하셨습니다.")
        money_out = input("금액을 입력해주세요 :    ")
        if int(money_out) > myMoney:
            lack = int(money_out) - money
            print("현재 잔고 부족입니다." + str(lack) + " 원이 부족합니다.")
        elif int(money_out) == myMoney:
            print ("통장을 파기합니다")
        else:
            left = myMoney - int(money_out)
            print (str(money_out) + " 원이 출금되었습니다.")
            print ("현재 잔금은" + str(left) + " 원입니다.")
            money=left
            
    elif bank == "exit":
        break
    
    else:
        print("다시 입력해주세요. 입금이라면 '입금'을, 출금이라면 '출금'을 입력해주세요 :  ")










"""
                                        ##### 문제 4 #####

메뉴판에 메뉴를 추가하세요. 
추가를 완료하면 각 테이블에서 어떤 주문을 했는지 랜덤으로 출력되게 하세요. 
(테이블은 총 6개가 있습니다. 단, 몇 개의 테이블에서 주문하는지도 랜덤입니다.)

6개의 테이블 중 몇 개의 테이블에서 주문할지, 주문 내역이 랜덤값입니다.

힌트: import random, randomrange


(((( 출력 결과 예시 참고 )))

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 순대
메뉴판:  ['순대']

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 튀김
메뉴판:  ['순대', '튀김']

"""
### 문제4 답안 (이 아래에 적어주세요!)
print("[문제 4]")

menu =[]

while True:
    new_menu = input("추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): ")
    if new_menu == '완료':
        break
    else:
        menu.append(new_menu)
        menu.sort()
        print( "메뉴판 : " )	
        print(menu)	










"""
                                    ##### 문제 5-1 #####

mbti의 검사결과는 아래와 같이 16가지 유형이 있다.
'ISTJ'
'ISFJ'
'INFJ'
'INTJ'
'ISTP'
'ISFP'
'INFP'
'INTP'
'ESTP'
'ESFP'
'ENFP'
'ENTP'
'ESTJ'
'ESFJ'
'ENTJ'

이때, 200명의 mbti 검사결과를 random 하게 만드는 함수를 작성해보세요

출력 조건) 200명의 검사 결과는 list로 담는다
힌트) 문자열을 랜덤하게 출력하는 코드는 아래와 같습니다.
import random

hint = "ABCDEFGH"
random.choice(hint)

"""
### 문제 5-1 답안 (이 아래에 적어주세요!)
print("[문제 5-1]")
import random

mbti =  'ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENTJ'
result = []

for i in range (0, 200):
    k = random.choice(mbti)
    result.append(k)
    i += 1
    
print(result)










"""
##### 문제 5-2 #####

200명의 검사 결과가 각 16가지의 유형별 몇 명이 있는지 구하기

출력 조건) 딕셔너리 형식( {'mbti유형': 총 명수})
출력 예시) {'ESFP':17, 'INFJ': 13...}
힌트) 각각의 mbti 유형을 세는 법(counting)을 생각해보자.

"""
### 문제 5-2 답안 (이 아래에 적어주세요!)
print("[문제 5-2]")

mbti_dic = {}

for m in result:
    try: mbti_dic[m] += 1
    except: mbti_dic[m] =1
print (mbti_dic)    










"""
##### 문제 5-3 #####

mbti 유형을 딕셔너리의 key로 입력했을 경우, 
value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
출력 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것

"""
### 문제 5-3 답안 (이 아래에 적어주세요!)
print("[문제 5-3]")

mymbti = (input("mbti 유형을 입력해보세요: ")).upper()

print(str(mymbti) + " 에 해당하는 사람은 총 " + str(mbti_dic.get(mymbti)) + " 명 입니다.")