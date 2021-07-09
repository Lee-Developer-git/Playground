#3 큰 수의 법칙

## 내가 푼 방법
N, M, K  = map(int, input().split())
array = list(map(int, input().split()))
result = 0
i = 0 # K번 더한 수를 센다(가장 큰 수를 더할 때)
count = 0 # 전체를 더한 수를 센다

m1 = max(array)
del array[array.index(m1)]
m2 = max(array)

while M > count:
    while K > i:
        if M <= count: # while문이 바깥에 있어서 적용이 안되는 부분이있음..
            break
        result += m1
        i += 1
        count += 1
    if M <= count:
        break
    result += m2
    count += 1
    i = 0

print(result)

## 답안 예시
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #정렬
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수
## 정렬 함수를 사용해서 배열을 변경하지 않아도 큰 수를 뽑아냄

result = 0

while True:
    for i in range(k): # 가장 큰 수 k번 더하기,, 새로운 변수를 사용하지 않아도 k번 반복 가능하게 하도록 하였음
        if m == 0 :
            break
        result += first
        m -= 1 # 전체 경우의 수를 셀 때 m에서 -1하는 방법 사용
    if m == 0 :
        break
    result += second
    m -= 1

print(result)