#4 1이 될 때까지
## 내가 푼 방법
result = 0
N, K = map(int, input().split())

## N이 K보다 클 때(나머지에 따라서 계산이 달라짐) 1보다 클 때 두 가지로 나누어서 계산한다.
while N > K :
    if N % K != 0 :
        N = N - 1
        result += 1
    else :
        N = N / K
        result += 1

while N > 1 :
    N -= N
    result += 1

print(result)

## 답안 예시 (잘 모르겟음........)
result = 0
N, K = map(int, input().split())

while True:
    # 만약 N이 K로 나누어 떨어지지 않을 때,, K로 나누어 떨어지는 수 중 가장 가까운 수 찾기
    target = (N // K) * K
    # 1을 몇 번 뺄지 한 번에 계산
    result += (N - target)
    N = target
    if N < K:
        break
    result += 1
    N //= K

result += ( N - 1 )
print(result)