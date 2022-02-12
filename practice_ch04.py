# ch04.
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)
# 여기까지 "문자열"
# ------------------------------------------------
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
# print("월 : " + jumin[2,4]) # 2 부터 4 직전까지 (2, 3)
# print("일 : " + jumin[4,6]) # 4 부터 6 직전까지 (4, 5)

# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지
# 여기까지 "슬라이싱"
# ------------------------------------------------
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java")) # find 사용시 해당 값이 없으면 -1 출력하고 프로그램 진행함.
# # print(python.index("Java")) # 인덱스 사용시 해당 값이 없으면 오류 냄..
# print("hi")

# print(python.count("n"))
# 여기까지 '문자열 처리 함수'
# ------------------------------------------------
# print("a" + "b")
# print("a","b")

# # 방법 1
# print("나는 %d살입니다." % 20) # %d는 정수
# print("나는 %s을 좋아해요." % "파이썬") # %s는 문자열
# print("Apple 은 %c로 시작해요." % "A") # %c는 한 글자
# # %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

# # 방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
# 여기까지 '문자열 포맷'
# ------------------------------------------------
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
print("C:\\workspace\\python")

# \r : 커서를 맨 앞으로 이동
print("Rea Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")
# 여기까지 "탈출문자"
# ------------------------------------------------