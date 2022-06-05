---
title: "[프로그래머스][파이썬] 문자열 압축"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 파이썬
    - 카카오
    - 완전탐색
    - 구현
    - 문자열
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 링크

<https://programmers.co.kr/learn/courses/30/lessons/60057>

## 문제 설명

데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.  
최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.  
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.  
예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다.  
"어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.  
예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다.  
다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.  
다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다.  
이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.  
압축할 문자열 `s`가 매개변수로 주어질 때, 위에 설명한 방법으로 **1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이**를 return 하도록 `solution` 함수를 완성해주세요.

## 제한사항

- `s`의 길이는 1 이상 1,000 이하입니다.
- `s`는 알파벳 소문자로만 이루어져 있습니다.

## 입출력 예

|s|return|
|-|------|
|"aabbaccc"|7|
|"ababcdcdababcdcd"|9|
|"abcabcdede"|8|
|"abcabcabcabcdededededede"|14|
|"xababcdcdababcdcd"|17|

## 입출력 예 설명

### 입출력 예 #1

문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.

### 입출력 예 #2

문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.

### 입출력 예 #3

문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.

### 입출력 예 #4

문자열을 2개 단위로 자르면 `"abcabcabcabc6de"` 가 됩니다.  
문자열을 3개 단위로 자르면 `"4abcdededededede"` 가 됩니다.  
문자열을 4개 단위로 자르면 `"abcabcabcabc3dede"` 가 됩니다.  
문자열을 6개 단위로 자를 경우 `"2abcabc2dedede"`가 되며, 이때의 길이가 14로 가장 짧습니다.

### 입출력 예 #5

문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.  
따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.  
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

## 풀이

```
1. 압축할 문자열을 주어진 단위만큼 잘라서 배열 splited_str_list에 할당한다.
2. 함수 groupby를 이용해 splited_str_list에서 연속된 문자열의 개수를 구한다.
3. 압축한 문자열을 comp_str_list에 할당한다.
4. comp_str_list를 하나의 문자열로 변환하여 그 문자열의 길이를 구한다.
5. 주어진 단위를 1부터 len(s) // 2까지 바꿔가며 1~4를 반복한다.
6. 5에서 나온 값들의 최솟값을 구한다.
------------------------------------------------------
압축할 문자열: "aabbaccc"

(1개 단위) 
splited_str_list = ["a", "a", "b", "b", "a", "c", "c", "c"]
--groupby-->
key: "a", group: ("a", "a")
key: "b", group: ("b", "b")
key: "a", group: ("a")
key: "c", group: ("c", "c", "c")
->
comp_str_list = ["2a", "2b", "a", "3c"]
->
압축된 문자열의 길이 =  7

(2개 단위)
splited_str_list = ["aa", "bb", "a", "cc", "c"]
--groupby-->
key: "aa", group: ("aa")
key: "bb", group: ("bb")
key: "a", group: ("a")
key: "cc", group: ("cc")
key: "c", group: ("c")
->
comp_str_list = ["aa", "bb", "a", "cc", "c"]
->
압축된 문자열의 길이 =  8

(3개 단위)
splited_str_list = ["aab", "bac", "cc"]
--groupby-->
key: "aab", group: ("aab")
key: "bac", group: ("bac")
key: "cc", group: ("cc")
->
comp_str_list = ["aab", "bac", "cc"]
->
압축된 문자열의 길이 =  8

(4개 단위)
splited_str_list = ["aabb", "accc"]
--groupby-->
key: "aabb", group: ("aabb")
key: "accc", group: ("accc")
->
comp_str_list = ["aabb", "accc"]
->
압축된 문자열의 길이 =  8

따라서, 압축된 문자열 중 가장 짧은 것의 길이는 7
```

```python
from itertools import groupby

# 압축 단위가 n일 때, 압축된 문자열의 길이(compressed string length)를 반환하는 함수
def get_comp_str_len(s, n):
    splited_str_list = [s[i:i + n] for i in range(0, len(s), n)] # 문자열 s를 n개 단위로 자른 문자열들을 저장한 배열
    comp_str_list = []                                           # 압축된 문자열을 저장한 배열
    
    for key, group in groupby(splited_str_list):
        group_len = len(list(group))
        
        if group_len == 1:
            comp_str_list.append(key)
        else:
            comp_str_list.append(f"{group_len}{key}")
    
    return len("".join(comp_str_list))

def solution(s):
    # 예외 처리 (s의 길이가 1일 때)
    if len(s) == 1:
        return 1
    
    # 압축 단위는 1부터 (len(s) // 2)까지
    result_list = []
    
    for i in range(1, (len(s)//2) + 1):
        result_list.append(get_comp_str_len(s, i))
        
    return min(result_list)
```