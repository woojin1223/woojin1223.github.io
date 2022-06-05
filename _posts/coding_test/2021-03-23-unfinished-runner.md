---
title: "[프로그래머스][파이썬] 완주하지 못한 선수"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 파이썬
    - 해시
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 링크

<https://programmers.co.kr/learn/courses/30/lessons/42576>

## 문제 설명

수많은 마라톤 선수들이 마라톤에 참여하였습니다.  
단 **한 명의 선수**를 제외하고는 모든 선수가 마라톤을 완주하였습니다.  
마라톤에 참여한 선수들의 이름이 담긴 배열 `participant`와 완주한 선수들의 이름이 담긴 배열 `completion`이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 `solution` 함수를 작성해주세요.

## 제한 사항

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- `completion`의 길이는 `participant`의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

## 입출력 예

|participant|compeletion|return|
|-----------|-----------|------|
|["leo", "kiki", "eden"]|["eden", "kiki"]|"leo"|
|["marina", "josipa", "nikola", "vinko", "filipa"]|["josipa", "filipa", "marina", "nikola"]|"vinko"|
|["mislav", "stanko", "mislav", "ana"]|["stanko", "ana", "mislav"]|"mislav"|

## 입출력 예 설명

### 입출력 예 #1

"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

### 입출력 예 #2

"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

### 입출력 예 #3

"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

## 풀이 1

`collections` 모듈의 `Counter` 클래스를 사용합니다.  
`Counter`는 iterable 객체 안의 각 원소의 개수를 나타내는 클래스입니다.  
`Counter` 클래스는 덧셈과 뺄셈 연산이 가능하며, 이 문제의 경우에는 뺄셈을 사용합니다.  
뺄셈을 통해, 완주하지 못한 선수의 이름을 구할 수 있습니다.  
아래의 코드에서 `result_dict`는 `{선수이름: 1}`과 같이 사전 형식의 객체이기 때문에 `result_dict`의 `key`를 반환해야 합니다.

```python
from collections import Counter

def solution(participant, completion):
    result_dict = Counter(participant) - Counter(completion) # Counter 클래스 간의 뺄셈
    
    return list(result_dict.keys())[0]
```

## 풀이 2

`participant`과 `completion`을 정렬한 후, `zip` 함수로 두 리스트에서 같은 위치의 원소들을 비교합니다.  
두 원소가 서로 다르다면, 참여자 명단에 있지만 완주자 명단에는 없는 사람이므로 그 값을 반환합니다.  
만약 두 원소가 전부 같다면, 참여자 명단의 제일 끝에 있는 사람이 완주자 명단에 없는 유일한 사람입니다.  
따라서, 참여자 명단의 제일 끝에 있는 값을 반환합니다.  
(참고: `completion`의 길이는 `participant`의 길이보다 1 작습니다.)

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
        
    return participant[-1]
```