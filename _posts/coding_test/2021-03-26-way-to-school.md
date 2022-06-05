---
title: "[프로그래머스] 등굣길"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 완전탐색
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

계속되는 폭우로 일부 지역이 물에 잠겼습니다.  
물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.  
집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.  
아래 그림은 m = 4, n = 3 인 경우입니다.
![그림1](https://grepp-programmers.s3.amazonaws.com/files/ybm/056f54e618/f167a3bc-e140-4fa8-a8f8-326a99e0f567.png)  
가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.  
격자의 크기 `m`, `n`과 물이 잠긴 지역의 좌표를 담은 2차원 배열 `puddles`이 매개변수로 주어집니다.  
**오른쪽과 아래쪽으로만 움직여** 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 `solution` 함수를 작성해주세요.

## 제한사항

- 격자의 크기 `m`, `n`은 1 이상 100 이하인 자연수입니다.
    + `m`과 `n`이 모두 1인 경우는 입력으로 주어지지 않습니다.
- 물에 잠긴 지역은 0개 이상 10개 이하입니다.
- 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

## 입출력 예

|m|n|puddles|return|
|-|-|-------|------|
|`4`|`3`|`[[2, 2]]`|`4`|

## 입출력 예 설명

![그림2](https://grepp-programmers.s3.amazonaws.com/files/ybm/32c67958d5/729216f3-f305-4ad1-b3b0-04c2ba0b379a.png)

## 풀이 1

```python
def get_value(matrix, x, y):
    try:
        return matrix[x][y]
    except:
        return 0

def solution(m, n, puddles):
    matrix = [[0] * m for _ in range(n)]
    matrix[0][0] = 1
    
    for y in range(n):
        for x in range(m):
            if [x + 1, y + 1] in puddles:
                continue
            else:
                matrix[y][x] += get_value(matrix, y, x - 1) + get_value(matrix, y - 1, x)
    
    return matrix[n - 1][m - 1] % 1000000007
```

## 풀이 2

```python
# --- (n + 1) x (m + 1) 행렬로 푸는 풀이 ---
def solution(m, n, puddles):
    area = [[0] * (m + 1) for _ in range(n + 1)]
    area[1][1] = 1 # (1, 1) 좌표의 경우의 수는 1입니다

    for x, y in puddles:
        area[y][x] = -1 # 웅덩이 좌표 값을 -1로 바꿉니다.

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if area[y][x] == -1: # 웅덩이는 생략합니다.
                area[y][x] = 0 # 이후 합에 영향이 안가도록 0으로 바꿉니다
                continue

            # 왼쪽과 위의 경우의 수를 합칩니다.
            area[y][x] += area[y][x - 1] + area[y - 1][x]

    return area[n][m] % 1000000007 # n, m 좌표의 경우의 수를 리턴합니다.
```