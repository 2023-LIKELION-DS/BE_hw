# 6장
# 6-1

#조건문

if True:        # 콜론이 기준이 된다.
    print("True")       # 들여쓰기를 해야한다
else:
    print("False")
    
    
if 4>3:
    print("a")
else:
    print("b")
    

#입력값을 int로 처리 
value = input("값을 입력해주세요: ")

# if int(value) > 10:      # 문자열로 출력되기에 숫자로 변환해야함
#     print("a")
# else:
#     print("b")
    
value = value.upper()

if value == "INFP":
    print("INFP")    
else:
    print("nothing")
    
    

# 6-2

day = input("요일을 입력해주세요(0~6): ")
if day == "0":
    print("휴무")
elif day == "6":
    print("단축영업")
elif day == "1":
    print("연장영업")
elif day == "3":
    print("암튼 휴일로 해")
else:
    print("정상영업")
    
