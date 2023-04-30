# 7-9

# dictionalries

student = {
    "student_no": "20230401", 
    "major": "English",
    "grade": 1
}

print(student["student_no"])
print('___________________________________________')


# 딕셔너리 내 데이터 수정
student["student_no"] = "20230101"

print(student)
print(student["student_no"])
print('___________________________________________')


# 7-10

#추가
student["gpa"] = 4.5
print(student)
print('___________________________________________')

#수정
student["gpa"] = 4.3
print(student)
print('___________________________________________')

#삭제
del student["gpa"]
print(student)
print('___________________________________________')



# 7-11

#데이터에 접근
print(student.get("grade"))
print('!!!!')

# 만약 없는 데이터에 접근한다면
print(student.get("gpa"))       # None 출력
print('___________________________________________')


print(student.get("gpa", "해당 키-값이 없습니다~"))    # 없다면 출력할 문구
print('___________________________________________')

# 딕셔너리의 키를 반환
print(student.keys()) 
print('___________________________________________')

# 딕셔너리의 키를 리스트로 반환
print(list(student.keys()))
print('___________________________________________')

# 딕서녀리의 값을 반환
print(student.values()) 
print('___________________________________________')




# 7-12

tech = {
    "HTML" : "Advanced",
    "JavaScript": "Intermediate",
    "Python": "Expert",
    "Go": "Novice"
}

for key, value in tech.items():
    print(f'{key} - {value}')
    
print('____________!!!!!!_______________________________')

for i in tech:
    print(i)

print('___________________________________________')

for value in tech.values():
    print(value)
print('___________________________________________')




# 7-13

# 중첩 Nesting

student_1 ={
    "student_no": "1",
    "gpa": "4.3"
}

student_2 ={
    "student_no": "2",
    "gpa": "3.8"
}

students = [student_1, student_2]

for student_ in students:
    print(student_['student_no'])
    
print('___________#######__________________')

for student_ in students:
    student['graduated'] = False
    print(student_)
    
print('____________________________________')


student_a = {
    "subjects": ["회계원리", "중국어회화"]
}

print(student_a["subjects"]) # 리스트 불러오기
subjects_list = student_a["subjects"]

for subject in subjects_list:
    print(subject)
    
print('___________________0000000___________________')

studnet_b = {
    "scholarship": {
        "name": "국가장학금",
        "amount": "1000000"
    }
}

print(studnet_b)

for key in studnet_b.keys():
    print(key)
    
for value in studnet_b.values():
    for value_2 in value.values():
        print(value_2)