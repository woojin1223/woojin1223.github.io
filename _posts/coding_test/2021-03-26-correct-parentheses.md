---
title: "[프로그래머스][파이썬] 올바른 괄호"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 파이썬
    - 스택
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

괄호가 바르게 짝지어졌다는 것은 **"(" 문자로 열렸으면 반드시 짝지어서 ")" 문자로 닫혀야 한다**는 뜻입니다.  
예를 들어

- "()()" 또는 "(())()" 는 올바른 괄호입니다.
- ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

"(" 또는 ")" 로만 이루어진 문자열 `s`가 주어졌을 때, 문자열 `s`가 올바른 괄호이면 `true`를 return 하고, 올바르지 않은 괄호이면 `false`를 return 하는 `solution` 함수를 완성해 주세요.

## 제한사항

- 문자열 `s`의 길이 : 100,000 이하의 자연수
- 문자열 `s`는 "(" 또는 ")" 로만 이루어져 있습니다.

## 입출력 예

|s|return|
|-|------|
|"()()"|true|
|"(())()"|true|
|")()("|false|
|"(()("|false|

## 입출력 예 설명

### 입출력 예 #1,2,3,4

문제의 예시와 같습니다.

## 풀이 1

```python
def solution(s):
    # 문자열 s의 맨 처음 문자는 "("이고 맨 마지막 문자는 무조건 ")" 이어야 함
    if s[0] == ")" or s[-1] == "(":
        return False

    stack = []

    for x in s:
        if stack:
            if stack[-1] == "(" and x == ")":
                stack.pop()
            else:
                stack.append(x)
        elif x == ")":
            return False
        else:
            stack.append(x)
    
    return False if stack else True
```

## 풀이 2

```python
def solution(s):
    # 문자열 s의 맨 처음 문자는 "("이고 맨 마지막 문자는 무조건 ")" 이어야 함
    if s[0] == ")" or s[-1] == "(":
        return False

    cnt = 0

    for x in s:
        if x == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return cnt == 0
```

