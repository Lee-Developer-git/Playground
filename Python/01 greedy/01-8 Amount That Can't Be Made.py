# CH11 - 04 만들 수 없는 금액

## 내가 푼 방법
# 실패....ㅠㅠㅠㅠㅠ

# N = int(input())
# coin = list(map(int, input().split()))
# result = 0
# count = 0

# coin.sort(reverse=True)
# for i in coin:
#     count += i

# for i in range(1, count):
#     for j in range(1, N-1):
#         if i == coin[j]:
#             break
#         elif i > coin[j]:
#             i = i - coin[j]
#             if i == 0:
#                 break
#             elif i > 0 :
#                 continue
#         elif i < coin[N-1]:
#             result = i
#             break
#     if result != 0:
#         break

# print(result)

## 답안 예시
# target을 점차적으로 늘리면서 target 금액을 만들 수 있는지에 대해 알아보면 된다!
# 거스름돈 문제와 비슷한줄 알았는데 아니었음 #
# 거스름돈 문제 => 동전이 무한 개 / 만들 수 없는 금액 문제 => 동전이 한정적
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x: #만들 수 없는 금액을 찾았을 때 반복 종료
        break
    target += x #띠용........ㅠㅠㅠㅠㅠㅠㅠㅠ

print(target)