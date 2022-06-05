---
title: "[프로그래머스] 행렬의 곱셈"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

2차원 행렬 `arr1`과 `arr2`를 입력받아, `arr1`에 `arr2`를 곱한 결과를 반환하는 함수, `solution`을 완성해주세요.

## 제한사항

- 행렬 `arr1`, `arr2`의 행과 열의 길이는 2 이상 100 이하입니다.
- 행렬 `arr1`, `arr2`의 원소는 -10 이상 20 이하인 자연수입니다.
- 곱할 수 있는 배열만 주어집니다.

## 입출력 예

|arr1|arr2|return|
|----|----|------|
|`[[1, 4], [3, 2], [4, 1]]`|`[[3, 3], [3, 3]]`|`[[15, 15], [15, 15], [15, 15]]`|
|`[[2, 3, 2], [4, 2, 4], [3, 1, 4]]`|`[[5, 4, 3], [2, 4, 1], [3, 1, 1]]`|`[[22, 22, 11], [36, 28, 18], [29, 20, 14]]`|


## 풀이

```python
def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr2[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):     
            result[i][j] = sum(x * y for x, y in zip(arr1[i], list(zip(*arr2))[j]))
            
    return result
```