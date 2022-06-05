---
title: "[프로그래머스][파이썬] 최댓값과 최솟값"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 파이썬
    - 문자열
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 링크

<https://programmers.co.kr/learn/courses/30/lessons/12939>

## 문제 설명

문자열 `s`에는 공백으로 구분된 숫자들이 저장되어 있습니다.  
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)" 형태의 문자열을 반환하는 함수, `solution`을 완성하세요.  
예를 들어 `s`가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

## 제한사항

- `s`에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

## 입출력 예

|s|return|
|-|------|
|"1 2 3 4"|"1 4"|
|"-1 -2 -3 -4"|"-4 -1"|
|"-1 -1"|"-1 -1"|

## 풀이

1. `s.split()`: 문자열의 메서드 `split()`을 이용하여 문자열 s를 **공백을 기준으로 분리**하여 만든 리스트
2. `list(map(int, s.split()))`: `s.split()`으로 만든 리스트의 각 원소를 정수형으로 변환
3. `min(s_splited)`, `max(s_splited)`: `min()`과 `max()`를 이용하여 `s_splited`의 최솟값과 최댓값을 구함
4. `f"{min(s_splited)} {max(s_splited)}"`: **f-string**을 이용하여 "(최소값) (최대값)" 형태의 문자열을 구함

```python
def solution(s):
    s_splited = list(map(int, s.split()))
    
    return f"{min(s_splited)} {max(s_splited)}"
```