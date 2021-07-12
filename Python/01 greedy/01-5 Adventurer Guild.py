# 5 모험가 길드

## 내가 푼 방법
# 공포도별로 분류함
N = int(input('모험가 수를 입력하세요 :'))
List = list(map(int, input().split()))
result = 0 # 그룹 수
count_num = [0 for i in range(N)] # 모험가의 max공포도를 N으로 설정(N보다 크면 여행을 떠나지 못하므로)

for i in range(N):
    x = List[i]
    if x == 1:
        result += 1
    else:
        count_num[x] += 1 # 공포도에 대한 사람 수를 더함

# 공포도가 x인 사람 수가 x명 이상일 때 그룹 수 추가
if count_num[x] > x:
    result += 1

print(result)

## 답안 예시
n = int(input())
data = list(map(int, input().split()))
data.sort() # 그리디 알고리즘에서는 정렬이 진짜 유용하게 쓰이는 듯,,
result = 0
count = 0

for i in data: #공포도 '낮은 것'부터 확인
    count += 1
    if count >= i: #현재 그룹에 포함된 모험가 수가 현재 공포도 이상이면 그룹 결성
        result += 1
        count = 0

print(result)