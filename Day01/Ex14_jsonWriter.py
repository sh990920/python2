'''
json (JavaScript Object Notation)
    키-값(Value) 쌍으로 중괄호로 묶인 객체형태 데이터
    파이썬의 딕셔너리와 비슷한 생김새
    구조 -> { K : V }

'''
import json

dictList = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]
    },
    {
        'name' : 'alice',
        'age' : 21,
        'spec' : [
            168.5,
            60.5
        ]
    }
]
jsonString = json.dumps(dictList, indent=4)

# indent 들여쓰기, ensure_ascil=false 한글 아스키코드로 변환하지 않음
with open('dictList.json', 'w') as file:
    file.write(jsonString)
print('dictList.json 파일이 생성되었습니다.')