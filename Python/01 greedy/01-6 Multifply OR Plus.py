# CH11 - 02 곱하기 혹은 더하기

## 내가 푼 방법
num = input()
result = 0
m_plus = 0
m_mul = 0

for i in range(len(num)):
    value = int(num[i])
    if i == 0:
        result = value
        m_plus = value
        m_mul = value
    elif i < len(num):
        m_plus += value
        m_mul *= value
        print(m_plus , m_mul)
        if m_plus > m_mul:
            result += value
        else:
            result *= value
    else:
        break
    m_plus= result
    m_mul = result

print(result)

## 답안 예시
data = input()

result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1: ## 두 수 중에서 하나라도 0 혹은 1인 경우 곱하기보다 더하기 시행
        result +=  num
    else :
        result *= num

print(result)