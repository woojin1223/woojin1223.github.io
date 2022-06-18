---
title: "[백준] 1915번: 가장 큰 정사각형"
categories: 코딩테스트
tags: [백준, 다이나믹프로그래밍]
---

## 문제 링크

<https://www.acmicpc.net/problem/1915>

## 문제

n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.

|||||
|-|-|-|-|
|0	|1	|0	|0|
|0	|1	|1	|1|
|1	|1	|1	|0|
|0	|0	|1	|0|

위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.

## 입력

첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

## 출력

첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.

## 예제 입력 1

```
4 4
0100
0111
1110
0010
```

## 예제 출력 1

```
4
```

## 풀이

```python
n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
answer = max(array[0])

for i in range(1, n):
    for j in range(1, m):
        if array[i][j] == 1:
            array[i][j] = min(array[i - 1][j - 1], array[i - 1][j], array[i][j - 1]) + 1
        
    answer = max(answer, max(array[i]))
        
print(answer ** 2)
```