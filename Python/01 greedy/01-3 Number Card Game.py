# 3 숫자 카드 게임
## 내가 푼 방법
N, M = map(int, input().split())
List = []

for i in range(N):
    row = list(map(int, input().split()))
    row.sort()
    min_num = row[0]
    List.append(min_num)

List.sort()
result = List[N-1]
print(result)


## 답안 예시 (2중 반복문 구조 이용)
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001 ##현재 줄에서 가장 작은 수 찾기..... #사실 이 부분 이해가 안 감
    for a in data:
        min_value = min(min_value,a)
    result= max(result, min_value)

print(result)