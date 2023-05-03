"""
##### 문제 1 #####
 
딕셔너리에 국어: 87, 수학: 88, 영어: 92, 과학: 67, 사회: 72 를 저장하고 평균을 구하시오.

"""
### 문제1 답안 (이 아래에 적어주세요!)
print("[문제 1]")
scores={'국어':87, '수학':86, '영어':92, '과학':67,'사회':72}
hap=0
for score in scores.values():
    hap+=score
ave=hap/len(scores)
print("평균 : ",ave)




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
foods = ["김밥", "라면", "튀김", "떡볶이", "순대"]
for food in foods:
    print("오늘의 메뉴: ",food)







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
money=10_000

while True:
    choice=input("출금 or 입금 or 종료 입력 : ")
    if choice=="출금":
        wd=int(input("금액? : "))
        if money>=wd:
            money-=wd
            print(wd,"원이 출금되었습니다. 현재 잔고는 %d입니다"%money)
        else:
            lack=wd-money
            print("현재 잔고 부족입니다. %d원이 부족합니다"%lack)
        if money==0:
            print("통장을 파기합니다.")
            break
    elif choice=="입금":
        dp=int(input("금액? : "))
        money+=dp
        print(dp,"원이 입금되었습니다. 현재 잔고는 %d입니다"%money)
    elif choice=="종료":
        break
    else:
        print("잘못 입력")




"""
##### 문제 4 #####

메뉴판에 메뉴를 추가하세요. 
추가를 완료하면 각 테이블에서 어떤 주문을 했는지 랜덤으로 출력되게 하세요. (테이블은 총 6개가 있습니다. 단, 몇 개의 테이블에서 주문하는지도 랜덤입니다.)

6개의 테이블 중 몇 개의 테이블에서 주문할지, 주문 내역이 랜덤값입니다.

힌트: import random, randomrange


(((( 출력 결과 예시 참고 )))

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 순대
메뉴판:  ['순대']

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 튀김
메뉴판:  ['순대', '튀김']
... (86줄 남음)
"""
import random
total_menus={}  #마지막에 한번에 테이블 번호:메뉴 리스트를 출력하기 위해 딕셔너리 생성
table_num=[]  #중복되지 않는 테이블 리스트

tables=random.randrange(1,7)  #몇개의 테이블에서 주문을 받을 것인지 렌덤으로.
print("총 %d개의 테이블에서 주문을 받겠습니다."%tables)
for num in range(tables):
    menus=[]
    menus_not_d=[]
    
    while True:
        
        random_table_num=random.randrange(1,7)  #몇번 테이블에서 주문을 받을 것인
        if random_table_num not in table_num:
            table_num.append(random_table_num)
            break
        
    while True:
        
        print(table_num[num],"번 테이블")
        menu=input("추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): ")

        if menu=="완료":
            for i in range(len(menus)):
            
                m=menus[random.randrange(len(menus))]
                while m in menus_not_d:
                    m=menus[random.randrange(len(menus))]
                menus_not_d.append(m)
            print(menus_not_d)
            break

        menus.append(menu)
        print("메뉴판: ",menus)

    total_menus["%s번 테이블"%table_num[num]]=menus_not_d
        
print(total_menus)
