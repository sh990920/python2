'''
파일명 : Ex07-O(n!).py

- O(n!): 팩토리얼 시간 복잡도, 순열을 구하는 알고리즘

'''
def permute(data, i, lenght):
    if i == lenght:
        print(''.join(data))
    else:
        for j in range(i, lenght):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, lenght)
            data[i], data[j] = data[j], data[i]

data = list('abcd')
permute(data, 0, len(data))