'''
open 함수모드
    r(read mode) : 읽기 전용 모드 / 파일 없으면 에러
'''
'''
file = open('hello.txt', 'rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end="")