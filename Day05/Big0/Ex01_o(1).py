'''
빅오 표기법(Bih o notation)
    알고리즘의 시간 복잡도와 공간 복잡도를 분석할 때 사용되는 표기법
    입력 크기 n에 대한 함수 f(n)의 실행 시간이나 메모리 사용량을 나타냄
    ! 빅오 표기법은 최악의 경우 성능 표현
    빅오 표기법의 규칙
    상수는 무시 : 9(2n) -> o(n), o(3n^2) -> o(n^2)
    낮은 차수의 항은 무시 : o(n^2 + n) -> o(n^2), o(n^3 + 100n^2) -> o(n^3)
'''
# o(1): 상수 시간 복잡도, 입력 크기와 상관없이 일정한 시간이 걸림
def return_first_value(arr):
    return arr[0]

# 실행코드
arr = [1, 3, 5, 7, 8]
print(return_first_value(arr))