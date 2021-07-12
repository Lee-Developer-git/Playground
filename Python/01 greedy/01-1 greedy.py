#1 거스름돈 문제
count = 0
n = 1260

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin #몫 => count에 넣음
    n %= coin

print(count)