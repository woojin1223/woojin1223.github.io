---
title: "[프로그래머스] 주식가격"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

초 단위로 기록된 주식가격이 담긴 배열 `prices`가 매개변수로 주어질 때, **가격이 떨어지지 않은 기간**은 몇 초인지를 return 하도록 `solution` 함수를 완성하세요.

## 제한사항

- `prices`의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- `prices`의 길이는 2 이상 100,000 이하입니다.

## 입출력 예

|prices|return|
|------|------|
|`[1, 2, 3, 2, 3]`|`[4, 3, 1, 1, 0]`|

## 입출력 예 설명

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

## 풀이

```python
def solution(prices):
    n = len(prices)
    answer = []
    
    for i in range(n):
        count = 0
        
        for j in range(i + 1, n):
            count += 1
            if prices[j] < prices[i]:
                break
            
        answer.append(count)
    
    return answer
```