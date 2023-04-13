'''
readlines() : 한줄 내용을 담은 리스트를 반환한다.
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    print(line_list)
    # for line in line_list:
    #     print(line, end='')
    for no, line in enumerate(line_list):
        print('{} {}'.format(no+1, line), end='')