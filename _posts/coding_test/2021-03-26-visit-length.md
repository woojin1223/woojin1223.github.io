---
title: "[프로그래머스] 방문 길이"
categories: 
    - 코딩테스트
tags: 
    - 프로그래머스
    - 그래프
    - 해시
toc: true
toc_sticky: true
toc_label: "목차"
---

## 문제 설명

게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다.  
명령어는 다음과 같습니다.

- U: 위쪽으로 한 칸 가기
- D: 아래쪽으로 한 칸 가기
- R: 오른쪽으로 한 칸 가기
- L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.  
좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.  

![그림1](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ace0e7bc-9092-4b95-9bfb-3a55a2aa780e/%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%80%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%B51_qpp9l3.png)  

예를 들어, "ULURRDLLU"로 명령했다면  

![그림2](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/668c7458-e184-472d-9d32-f5d2acca759a/%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%80%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%B52_lezmdo.png)  

- 1번 명령어부터 7번 명령어까지 다음과 같이 움직입니다.

![그림3](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/08558e36-d667-4160-bfec-b754c78a7d85/%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%80%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%B53_sootjd.png)  

- 8번 명령어부터 9번 명령어까지 다음과 같이 움직입니다.

![그림4](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/a52af28e-5835-438b-9f40-5467ebf9bf03/%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%80%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%B54_hlpiej.png)  

이때, 우리는 게임 캐릭터가 지나간 길 중 **캐릭터가 처음 걸어본 길의 길이**를 구하려고 합니다.  
예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.  
(8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다.)  
단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.  
예를 들어, "LULLLLLLU"로 명령했다면  

![그림5](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/f631f005-f8de-4392-a76c-a9ef64b6de08/%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%80%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%B55_nitjwj.png)  

- 1번 명령어부터 6번 명령어대로 움직인 후, 7, 8번 명령어는 무시합니다. 다시 9번 명령어대로 움직입니다.

![그림6](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/35e62f0a-43c6-4142-bec6-6d28fbc57216/%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%80%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%B56_nzhumd.png)  

이때 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.  
명령어가 매개변수 `dirs`로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 `solution` 함수를 완성해 주세요.

## 제한사항

- `dirs`는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
- `dirs`의 길이는 500 이하의 자연수입니다

## 입출력 예

|dirs|return|
|----|------|
|"ULURRDLLU"|7|
|"LULLLLLLU"|7|

## 입출력 예 설명

- 입출력 예 #1

문제의 예시와 같습니다.

- 입출력 예 #2

문제의 예시와 같습니다.

## 풀이 1

```python
# --- 직관적인 풀이 ---
def solution(dirs):
    x, y = 0, 0 # 시작 좌표를 0, 0으로 지정
    check = dict() # 좌표를 키로 사용하는 해시 생성
    
    for command in dirs:
        if command == 'U' and y < 5: # 위로
            check[(x, y, x, y + 1)] = True # 현재 좌표, 이동할 좌표
            y += 1
        elif command == 'D' and y > -5: # 아래로
            check[(x, y - 1, x, y)] = True # 이동할 좌표, 현재 좌표
            y -= 1
        elif command == 'R' and x < 5: # 오른쪽으로
            check[(x, y, x + 1, y)] = True # 현재 좌표, 이동할 좌표
            x += 1
        elif command == 'L' and x > -5: # 왼쪽으로
            check[(x - 1, y, x, y)] = True # 이동할 좌표, 현재 좌표.
            x -= 1

    return len(check) # 추가된 값들이 곧 방문 길이
```

## 풀이 2

```python
# --- 무방향 그래프 풀이 ---
def solution(dirs):
    dir_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    result_set = set()
    x, y = 0, 0

    for d in dirs:
        dx, dy = dir_dict[d]
        nx, ny = x + dx, y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            result_set.add(tuple(sorted([(x, y), (nx, ny)])))
            x, y = nx, ny
        
    return len(result_set)
```

## 풀이 3

```python
from collections import defaultdict

def solution(dirs):
    dir_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    result_dict = defaultdict(set)
    x, y = 0, 0
    
    """
    [result_dict 설명]
    1. 캐릭터의 시작점과 끝점을 기록한 사전
    2. 캐릭터가 처음 걸어본 길의 길이를 구해야 하므로 시작점(key)과 끝점(value), 끝점(key)과 시작점(value)을 한 번에 사전에 넣는다.
    3. 그리고 value의 자료 형식을 set으로 설정하면 중복된 점을 제거할 수 있다.
    """
    for d in dirs:
        dx, dy = dir_dict[d]
        nx, ny = x + dx, y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            result_dict[(x, y)].add((nx, ny))
            result_dict[(nx, ny)].add((x, y))
            x, y = nx, ny
    
    return sum(len(v) for v in result_dict.values()) // 2
```