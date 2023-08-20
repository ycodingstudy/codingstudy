# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이
    m = len(a[0])  # 열 길이
    result = [[0] * n for _ in range(m)]  # 90도 회전한 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock)
    for i in range(lock_length)
