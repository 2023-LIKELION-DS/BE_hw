# 7 -7 튜플

tup = (1, 20, 40)
    # 각각의 요소를 변경할 수 없다는 리스트와의 차이점을 가진다., 
print(tup[0])

# tup[0] =100 # 요소를 재할당하면 오류난다.

tup = (100, 20, 200)        # 전체를 새로 정의해 바꾸면 괜찮다.
print(tup)

print('---------------------------------------------------')

# # 7-8
tup = (1, 20, 40)

for x in tup:
    print(x)        # 순서대로 출려된다. 
    

print('---------------------------------------------------')

# 리스트로 변환하기 
list_1 = list(tup)
print(list_1)

#리스트로 변환 2
list_2 = [x for x in tup]
print(list_2)

#리스트 변환 3
list_3=[]

for x in tup:
    list_3.append(x)
    
print(list_3)