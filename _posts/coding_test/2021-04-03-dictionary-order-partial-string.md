---
title: "[프로그래머스] 사전순 부분 문자열"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 해시
    - 스택
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

어떤 문자열 `s`가 주어졌을 때, `s`로부터 만들 수 있는 부분 문자열 중 사전 순으로 가장 뒤에 나오는 문자열을 찾으려 합니다.  
부분 문자열을 만드는 방법은 다음과 같습니다.  

1. `s`에서 일부 문자를 선택해 새로운 문자열을 만듭니다.
2. 단, 이때 문자의 순서는 뒤바꾸지 않습니다.

예를 들어 문자열 "xyb"로 만들 수 있는 부분 문자열은 다음과 같습니다.  

x  
y  
b  
xy  
xb  
yb  
xyb  

이 중 사전 순으로 가장 뒤에 있는 문자열은 "yb"입니다.  

문자열 `s`가 주어졌을 때 `s`로부터 만들 수 있는 부분 문자열 중 사전 순으로 가장 뒤에 나오는 문자열을 리턴하는 `solution` 함수를 완성해주세요.

## 제한사항

- `s`는 길이가 1 이상 1,000,000 이하인 문자열입니다.
- `s`는 알파벳 소문자로만 이루어져 있습니다.

## 입출력 예

|s|return|
|-|------|
|`"xyb"`|`"yb"`|
|`"yxyc"`|`"yyc"`|

## 입출력 예 설명

- 입출력 예 #1

문제의 예시와 같습니다.

- 입출력 예 #2

"yxyc"로 만들 수 있는 부분 문자열은 다음과 같습니다.

y  
x  
c  
yx  
yy  
yc  
xy  
xc  
yxy  
yxc  
yyc  
xyc  
yxyc  

이 중 사전 순으로 가장 뒤에 나오는 문자열은 "yyc"입니다.

## 풀이 1

```python
from collections import defaultdict

def solution(s):
    char_index_dict = defaultdict(list)
    answer = ""
    
    for i, char in enumerate(s):
        char_index_dict[char].append(i)
    
    max_index = -1

    while max_index < len(s) - 1:
        max_char = max(char_index_dict.keys())
        max_char_index = [x for x in char_index_dict[max_char] if x > max_index]
        answer += len(max_char_index) * max_char
        max_index = max_char_index[-1]

        for key in list(char_index_dict.keys()):
            if char_index_dict[key][-1] <= max_index:
                char_index_dict.pop(key)
    
    return answer
```

## 풀이 2

```python
def solution(s):
    stack = []
    
    for char in s:
        while stack and stack[-1] < char:
            stack.pop()
            
        stack.append(char)
        
    return "".join(stack)
```