#o(log n): 로그 시간 복잡도, 이진 탐색처럼 문제를 절반으로 나누어 해결하는 알고리즘
def binary_search(arr, x):
    # 검색 범위의 시작점 설정
    low = 0

    # 검색 범위의 끝점을 설정
    high = len(arr) - 1

    # 시작점이 끝점보다 같거나 작을 때 까지 반복
    while low <= high:
        mid = (low + high) // 2

        # 중간점의 값이 찾고자 하는 값보다 작은경우
        # 검색 범위의 시작점을 중간점 다음 인덱스로 설정
        if arr[mid] < x:
            low = mid + 1

        # 중간점의 값이 찾고자 하는 값보다 큰 경우,
        # 검색 범위의 끝점을 중간점 이전 인덱스로 설정
        elif arr[mid] > x:
            high = mid - 1
        # 중간점의 값이 찾고자 하는 값과 같은 경우,
        # 중간점의 인덱스를 반환
        else:
            return mid
        
    # 찾고자 하는 값이 없는 경우 -1 반환
    return -1

# 실행코드
arr = [1, 10, 5, 7, 8, 9, 3, 11, 21]
arr = sorted(arr)
print(arr)
print(binary_search(arr, 5))