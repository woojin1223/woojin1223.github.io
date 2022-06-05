---
title: "[프로그래머스] 숫자의 표현"
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

Finn은 요즘 수학공부에 빠져 있습니다.  
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.  
예를 들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

- 1 + 2 + 3 + 4 + 5 = 15
- 4 + 5 + 6 = 15
- 7 + 8 = 15
- 15 = 15

자연수 `n`이 매개변수로 주어질 때, 연속된 자연수들로 `n`을 표현하는 방법의 수를 return하는 `solution`를 완성해주세요.

## 제한 사항

- `n`은 10,000 이하의 자연수 입니다.

## 입출력 예

|n|return|
|-|------|
|15|4|

## 입출력 예에 대한 설명

- 입출력 예 #1

문제의 예시와 같습니다.

## 풀이

```python
def solution(n):
    number_list = list(range(1, n + 1))
    count = 0
    
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            if sum(number_list[i:j]) == n:
                count += 1
                break
            elif sum(number_list[i:j]) > n:
                break
            
    return count
```