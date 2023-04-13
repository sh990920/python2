'''
파일복사 : 원본 -> 버퍼 변수(Memory) -> 복사본
open 함수모드
    b(binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력을 진행한다.
'''
buffer_size = 1024 # 1024Byte -> 1KB
with open('hello.txt', 'rb') as sourse:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = sourse.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사 되었습니다.')
