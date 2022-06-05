---
title: "[프로그래머스] FloodFill"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - BFS
    - 큐
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

n x m 크기 도화지에 그려진 그림의 색깔이 2차원 리스트로 주어집니다.  
같은 색깔은 같은 숫자로 나타난다고 할 때, 그림에 있는 영역은 총 몇 개인지 알아내려 합니다.  
영역이란 상하좌우로 연결된 같은 색상의 공간을 말합니다.  

예를 들어, `[[1, 2, 3],  [3, 2, 1]]` 같은 리스트는 다음과 같이 표현할 수 있습니다.  

![그림1](https://grepp-programmers.s3.amazonaws.com/files/production/516f9d3375/3b7691f5-bc15-4dbb-b99a-a66240b41406.png)  

이때, 이 그림에는 총 5개 영역이 있습니다.  

도화지의 크기 `n`과 `m`, 도화지에 칠한 색깔 `image`가 주어질 때, **그림에서 영역이 몇 개 있는지** 리턴하는 `solution` 함수를 작성해주세요.

제한 사항

## 제한사항

- `n`과 `m`은 1 이상 250 이하인 정수입니다.
- 그림의 색깔은 1 이상 30000 미만인 정수로만 주어집니다.

## 입출력 예

|n|m|images|return|
|-|-|------|----|
|`2`|`3`|`[[1, 2, 3], [3, 2, 1]]`|`5`|
|`3`|`2`|`[[1, 2], [1, 2], [4, 5]]`|`4`|

## 입출력 예에 대한 설명

- 입출력 예 #1

앞서 설명한 예와 같습니다.

- 입출력 예 #2

주어진 이미지는 다음과 같이 표현할 수 있습니다.  

![그림2](https://grepp-programmers.s3.amazonaws.com/files/production/516f9d3375/3b7691f5-bc15-4dbb-b99a-a66240b41406.png)  

따라서 이 이미지에는 4개 영역이 있습니다.

## 풀이

```python
from collections import deque

def bfs(image, visited, start):
    queue = deque([start])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= len(image) or ny < 0 or ny >= len(image[0]):
                continue
            
            if visited[nx][ny] or image[nx][ny] != image[x][y]:
                continue
                
            visited[nx][ny] = 1
            queue.append((nx, ny))
                
    return 1

def solution(n, m, image):
    visited = [[0] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                count += bfs(image, visited, (i, j))
    
    return count
```