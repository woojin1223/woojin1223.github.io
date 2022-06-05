---
title: "[프로그래머스] 약수의 개수와 덧셈"
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

두 정수 `left`와 `right`가 매개변수로 주어집니다.  
`left`부터 `right`까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 `solution` 함수를 완성해주세요.

## 제한 사항

- 1 ≤ `left` ≤ `right` ≤ 1,000

## 입출력 예

|left|right|return|
|----|-----|------|
|13|17|43|
|24|27|52|

## 입출력 예에 대한 설명

### 입출력 예 #1

- 다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.

|수|약수|약수의 개수|
|--|----|-----------|
|13|1, 13|2|
|14|1, 2, 7, 14|4|
|15|1, 3, 5, 15|4|
|16|1, 2, 4, 8, 16|5|
|17|1, 17|2|

- 따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.

### 입출력 예 #2

- 다음 표는 24부터 27까지의 수들의 약수를 모두 나타낸 것입니다.

|수|약수|약수의 개수|
|--|----|-----------|
|24|1, 2, 3, 4, 6, 8, 12, 24|8|
|25|1, 5, 25|3|
|26|1, 2, 13, 26|4|
|27|1, 3, 9, 27|4|

- 따라서, 24 - 25 + 26 + 27 = 52를 return 해야 합니다.

## 풀이

```python
# --- 완전 탐색 풀이 ---
# 시간 복잡도: O((right - left)right)

def get_n_aliquot(x):
    count = 0
    
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    
    return count

def solution(left, right):
    result = 0
    
    for x in range(left, right + 1):
        if get_n_aliquot(x) % 2 == 0:
            result += x
        else:
            result -= x
    
    return result

# --- 효율적인 풀이 ---

from math import ceil, floor, sqrt

def solution(left, right):
    result = int((right-left+1) * (left+right)/2)

    for x in range(ceil(sqrt(left)), floor(sqrt(right)) + 1):
        result -= 2 * (x**2)
    
    return result

# --- 더 효율적인 풀이 ---

from math import ceil, floor, sqrt

def get_quad_sum(x):
    
    return x * (x+1) * (2*x+1)/6
    
def solution(left, right):
    result = int((right-left+1) * (left+right)/2)
    result -= 2 * (get_quad_sum(floor(sqrt(right))) - get_quad_sum(ceil(sqrt(left)) - 1))
        
    return result
```