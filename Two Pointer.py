n = 5 # 데이터 갯수
m = 5 # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0 # 카운트 횟수
interval_sum = 0 # 부분합
end = 0 # 끝점

for start in range(n): # 시작점을 차례대로 증가시키며 반복
    while interval_sum < m and end < n: # end를 최대한 이동
        interval_sum += data[end]
        end += 1

    if interval_sum == m: # 부분합이 m 일때
        count += 1 # 카운트 증가
    interval_sum -= data[start]

print(count)