import json

with open('dictList.json', 'r', encoding='UTF-8')as file:
    jsonReader = file.read()
    dictList = json.loads(jsonReader)
for dic in dictList:
    print("이름 : {}".format(dic['name']))
    print("나이 : {}".format(dic['age']))
    print("키 : {}".format(dic['spec'][0]))
    print("몸무게 : {}".format(dic['spec'][1]))
    print()