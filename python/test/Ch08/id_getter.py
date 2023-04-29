# 8-4 모듈 id_getter.py

def get_id(email):
    
    if email.endswith('@test.com'):
        email_id = email.removesuffix('@test.com')
        print(email_id)
        return email_id         # 반한하고자 하는 데이터를 정해주어야 함
    else:
        print('처리할 수 없는 이메일 주소입니다.')

# # user_id = get_id('user@duksung.com')
# # print(user_id)
# user_id = get_id('user@test.com')
# print(user_id)

