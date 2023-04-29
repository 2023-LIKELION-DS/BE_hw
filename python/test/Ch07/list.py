# 7장
# 7-1 리스트- 리스트의 정의 및 선언

mbti = ['INFP', 'ENFP', 'ESTJ', 'INTP']

print(mbti)
print(mbti[0])

mbti[0] = 'infj'        # 새로운 값을 넣어서 만들기 

print(mbti)
print(mbti[0])


my_list = [123, 'apple']

print(my_list)



# 7-2 리트스 데이터 접근 및 조작


colors = ['red', 'blue', 'green']

# #수정
# colors[2] = 'black'
# print(colors)

# # 가장 마지막 순서에 추가
# colors.append('purple')
# print(colors)

# # 원하는 위치에 추가
# colors.insert(1, 'yellow')
# print(colors)

# # 제거 - 지워도 다시 사용할 수 없음
# del colors[0]
# print(colors)

# 제거 - 다시 반환한다. 
colors.pop(0)
print(colors)
print("@@@#########################@@@@@@@")

# color = colors.pop(0)
# print(colors)
# print(color)

# # 특정 데이터 자체를 입력해  제거 
# colors.remove('black')
# print(colors)



# 7-3  리스트 정렬

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# 정렬 - 원본데이터 변경
colors.sort()
print(colors) 
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# 역순정렬
colors.sort(reverse=True)
print(colors) 
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# 정렬 2
sorted(colors) # 최초의 초기화 데이터 를 변형시키지 않음. 
print(colors)

print(sorted(colors))
print("@@@@@@@@@@@@@@@@@@@@@@@@@------@@@@@@")


# 길이 - 요소의 갯수
print(len(colors))

print(colors[5])
print(colors[-1]) # 마지막 원소를 출력하고 싶다면
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



# 7-4 리스트 슬라이싱 및 복사

print(colors[1:5])
print(colors[:5])
print(colors[0:])
print(colors[:]) # 전체를 의미한다. 
print(colors[-1:])  

colors_2 = colors[:] # 리스트 전체를 새로운 변수에 넣는다
# colors-2 = color 와 다른 것은, 최초의 할당 메모리가 동일함. 최초와 분리되어서 출력되지 않는다. 
print("@@@@@@@@!!!!@@!!!@@@")

print(colors_2)

print("...........................................")


# 7-5 리스트와 흐름제어

scores = [88, 100, 96, 43, 65, 78]

scores.sort(reverse=True)
print(scores)

for score in scores:
    if score >= 80:
        print(scores)
    else:
        print("fail")
print("...........................................")
        
        
        
        
# 7-6 리스트 최댓값 최솟값 총합

# max_val = max(scores)
# min_val = min(scores)
sum_val = sum(scores)

sum_values = 0

for score in scores:
    sum_values = 0
    for score in scores:
        sum_values = sum_values + score
print(sum_values)       # 합을 구하기 
print("...........................................")


#평균구하기 
avg_val = sum(scores) / len(scores)
print(avg_val)