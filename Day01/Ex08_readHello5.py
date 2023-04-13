'''

'''
import sys # OS를 사용하기 위해서 import
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list)