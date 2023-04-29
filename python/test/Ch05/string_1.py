# 5장 실습

# 5-3

#  문자열 string = 문자의 나열

city = "seoul"      # Seoul, SEOUL, SEouL 
print(city)

city.upper()
print(city.upper())

city = city.upper()
print(city)         # 대문자로 변형된 데이터가 대입되어 출력

city.lower()
print(city.lower())

city = city.lower()
print(city)         # 소문자로 변경된 데이터가 데입되어 출력



occupation = "      developer       " # 공백 하나하나 문자다
print(occupation)

occupation.rstrip()
print(occupation.rstrip()) # 우측 공백 제거

occupation.lstrip()
print(occupation.lstrip()) # 좌측 공백 제거 



print("INFP ENFP INTP ESTJ")
# print("INFP    
#       ENFP 
#       INTP 
#       ESTJ")
print("INFP\nENFP\nNTP\nESTJ")  #개행
print("INFP\tENFP\tNTP\tESTJ")  # tab



# 5-4

score = "점수:90"
print(score.removeprefix("점수:"))

score_2 = "75점"
print(score_2.removesuffix("점")) 

city ="서울 중구"
print(city.replace("서울", "서울시"))



# 5-5

si_1 = "용인"
gu_1 = "기흥"
address_1 = f"{si_1}시  {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"

#서울시 종로구
#용인시 기흥구
#(시의이름)시 (구의이름)구

print(f"{si_1}시  {gu_1}구")
print("용인시  기흥구")
print(f"{si_2}시  {gu_2}구")
