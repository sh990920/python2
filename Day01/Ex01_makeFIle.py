# 예외처리 진행해야댐
# 파일 입출력
# 파일 입출력(I/O - Input/Output)
#   입력(Input) : 기존 파일을 읽어들이는 것을 말한다.
#   출력(Output) : 파일 생성, 내용 추가를 말한다.
'''
file = open("myFIle.txt", "wt")
print("myFile.txt 파일이 생성되었습니다.")
file.close()
'''

# with 문
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')
