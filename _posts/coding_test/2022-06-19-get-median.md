---
title: "[백준] 2696번: 중앙값 구하기"
categories: 코딩테스트
tags: [백준, 힙]
---

## 문제 링크

<https://www.acmicpc.net/problem/2696>

## 문제

어떤 수열을 읽고, 홀수번째 수를 읽을 때 마다, 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.

예를 들어, 수열이 1, 5, 4, 3, 2 이면, 홀수번째 수는 1번째 수, 3번째 수, 5번째 수이고, 1번째 수를 읽었을 때 중앙값은 1, 3번째 수를 읽었을 때는 4, 5번째 수를 읽었을 때는 3이다.

## 입력

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스의 첫째 줄에는 수열의 크기 M(1 ≤ M ≤ 9999, M은 홀수)이 주어지고, 그 다음 줄부터 이 수열의 원소가 차례대로 주어진다. 원소는 한 줄에 10개씩 나누어져있고, 32비트 부호있는 정수이다.

## 출력

각 테스트 케이스에 대해 첫째 줄에 출력하는 중앙값의 개수를 출력하고, 둘째 줄에는 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 구분하여 출력한다. 이때, 한 줄에 10개씩 출력해야 한다.

## 예제 입력 1

```
3
9
1 2 3 4 5 6 7 8 9
9
9 8 7 6 5 4 3 2 1
23
23 41 13 22 -3 24 -31 -11 -8 -7
3 5 103 211 -311 -45 -67 -73 -81 -99
-33 24 56
```

## 예제 출력 1

```
5
1 2 3 4 5
5
9 8 7 6 5
12
23 23 22 22 13 3 5 5 3 -3
-7 -3
```

## 풀이

```python
from heapq import heappop, heappush

tc = int(input())
answers = []

for _ in range(tc):
    answer = []
    max_hq, min_hq = [], []
    n = int(input())
    seq = []
    
    for _ in range(n//10 + 1):
        seq.extend(list(map(int, input().split())))
        
    heappush(min_hq, seq[0])
    answer.append(min_hq[0])
    
    for i, x in enumerate(seq[1:], 2):
        if x < min_hq[0]:
            heappush(max_hq, -x)
        else:
            heappush(min_hq, x)
        
        if len(max_hq) > len(min_hq):
            heappush(min_hq, -heappop(max_hq))
        elif len(max_hq) < len(min_hq):
            heappush(max_hq, -heappop(min_hq))
        
        if i % 2 == 1:
            if len(max_hq) > len(min_hq):
                answer.append(-max_hq[0])
            else:
                answer.append(min_hq[0])
    
    answers.append(answer)

for answer in answers:
    print(len(answer))

    for i, ans in enumerate(answer):
        if i != 0 and i % 10 == 0:
            print()
            
        print(ans, end=" ")
    
    print()
```