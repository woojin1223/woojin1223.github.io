---
title: "[프로그래머스][파이썬] 소수 만들기"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 파이썬
    - 소수
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 링크

<https://programmers.co.kr/learn/courses/30/lessons/12977>

## 문제 설명

주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.  
숫자들이 들어있는 배열 `nums`가 매개변수로 주어질 때, `nums`에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 `solution` 함수를 완성해주세요.

## 제한사항

- `nums`에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
- `nums`의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

## 입출력 예

|nums|return|
|----|------|
|[1, 2, 3, 4]|1|
|[1, 2, 7, 6, 4]|4|

## 입출력 예 설명

### 입출력 예 #1

[1, 2, 4]를 이용해서 7을 만들 수 있습니다.

### 입출력 예 #2

[1, 2, 4]를 이용해서 7을 만들 수 있습니다.  
[1, 4, 6]을 이용해서 11을 만들 수 있습니다.  
[2, 4, 7]을 이용해서 13을 만들 수 있습니다.  
[4, 6, 7]을 이용해서 17을 만들 수 있습니다.

## 풀이

[에라토스테네스의 체](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)를 이용하여 `n` 이하의 소수를 전부 구하는 함수 `get_primes(n)`를 정의합니다.  
`nums`를 정렬(`nums.sort()`)한 후 `nums`에서 서로 다른 3개의 수를 골랐을 때 가장 큰 수(`sum(nums[-3:])`)를 구합니다.  
`max_num = sum(nums[-3:])`을 함수 `get_primes()`의 입력값으로 하여 `max_num` 이하의 소수를 전부 구해서 `primes`라는 변수에 할당합니다.  
`itertools` 모듈의 `combinations` 함수를 사용하여 `nums`에서 고른 서로 다른 3개의 수의 합이 `primes`에 몇 개가 있는지를 반환합니다.

```python
from itertools import combinations

def get_primes(n):
    primes = [False, False] + [True] * (n-1)
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    return [i for i, r in enumerate(primes) if r]

def solution(nums):
    nums.sort()
    max_num = sum(nums[-3:])
    primes = get_primes(max_num)
    
    return len([c for c in combinations(nums, 3) if sum(c) in primes])
```