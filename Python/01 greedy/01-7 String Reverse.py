# CH11 - 03 문자열 뒤집기

## 내가 푼 방법
string = input()
List = []

for i in range(len(string)-1):
    if string[i] == string[i+1]:
        continue
    elif string[i] > string[i+1]: # 1에서 0으로 바뀌는 경우
        List.append(0)
    else: # 0에서 1로 바뀌는 경우
        List.append(1)

print(min(List.count(0), List.count(1)))