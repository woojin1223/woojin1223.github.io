---
title: "[프로그래머스] 소수 찾기"
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

한자리 숫자가 적힌 종이 조각이 흩어져있습니다.  
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.  

각 종이 조각에 적힌 숫자가 적힌 문자열 `numbers`가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 `solution` 함수를 완성해주세요.

## 제한사항

- `numbers`는 길이 1 이상 7 이하인 문자열입니다.
- `numbers`는 0~9까지 숫자만으로 이루어져 있습니다.
- "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

## 입출력 예

|numbers|return|
|-------|------|
|`"17"`|`3`|
|`"011"`|`2`|

## 입출력 예 설명

- 입출력 예 #1

`[1, 7]`으로는 소수 `[7, 17, 71]`를 만들 수 있습니다.

- 입출력 예 #2

`[0, 1, 1]`으로는 소수 `[11, 101]`를 만들 수 있습니다.  
_11과 011은 같은 숫자로 취급합니다._

## 풀이

```python
from itertools import permutations

def get_prime(n):
    result = [False, False] + [True] * (n - 1)
    
    for i in range(2, int(n ** 0.5) + 1):
        if result[i]:
            for j in range(2 * i, n + 1, i):
                result[j] = False
    
    result = [i for i, r in enumerate(result) if r]
    
    return result
    
def solution(numbers):
    candidate_numbers = set()
    
    for i in range(1, len(numbers) + 1):
        for number in set(permutations(numbers, i)):
            candidate_numbers.add(int("".join(number)))  

    primes = get_prime(max(candidate_numbers))
    
    return sum(n in primes for n in candidate_numbers)

```