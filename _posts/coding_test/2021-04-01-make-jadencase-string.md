---
title: "[프로그래머스] JadenCase 문자열 만들기"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 문자열
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

**JadenCase**란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.  
문자열 `s`가 주어졌을 때, `s`를 JadenCase로 바꾼 문자열을 리턴하는 함수, `solution`을 완성해주세요.

## 제한사항

- `s`는 길이 1 이상인 문자열입니다.
- `s`는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. (첫번째 입출력 예 참고)

## 입출력 예

|s|return|
|-|------|
|`"3people unFollowed me"`|`"3people Unfollowed Me"`|
|`"for the last week"`|`"For The Last Week"`|

## 풀이

```python
def solution(s):
    s_splited = s.split(" ")

    for i, string in enumerate(s_splited):
        string = string.lower()
        string = string.capitalize()
        s_splited[i] = string
        
    return " ".join(s_splited)
```