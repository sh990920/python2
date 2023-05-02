'''
4. 퀵 정렬(Quick Sort)
    분할 정복 알고리즘의 일종, 기준점(pivot)을 설정하고
    pivot 보다 작은 값을 왼쪽, 큰 값을 오른쪽에 분할한 후
    각 부분 리스트에 대해 재귀적으로 퀵 정렬을 수행하는 알고리즘
    최악의 경우 시간 복잡도 : o(n^2)
    최선의 경우 시간 복잡도 : o(n*log n)
    평균 시간 복잡도 : o(n*log n)
'''
# 퀵 정렬 알고리즘을 구현하는 함수
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # pivot 값 설정
    pivot = arr[0]

    left, right, equal = [], [], []
    for a in arr:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)

    return quick_sort(left) + equal + quick_sort(right)

# 실행 코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(arr))
