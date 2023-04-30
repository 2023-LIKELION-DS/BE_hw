# 6장 

# 6-3

#반복문 loops

i = 0
sum = 0

for i in range(1, 101):   #1   부터 100 번까지 반복
    print(i)

for i in  range(1, 101):
    sum = sum + i

print(sum)  # 1 부터 100 까지 더한 값


# 6-4

# 무한반복
# while True:
#     print("while loop")

progress = 0

while progress < 100:
    progress = progress + 1
    print(f"{progress}% completed")
    
    