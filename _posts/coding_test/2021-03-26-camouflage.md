---
title: "[프로그래머스][파이썬] 위장"
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

<https://programmers.co.kr/learn/courses/30/lessons/42578>

## 문제 설명

스파이들은 **매일 다른 옷을 조합하여 입어 자신을 위장**합니다.  
예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

|종류|이름|
|----|----|
|얼굴|동그란 안경, 검정 선글라스|
|상의|파란색 티셔츠|
|하의|청바지|
|겉옷|긴 코트|

스파이가 가진 의상들이 담긴 2차원 배열 `clothes`가 주어질 때 **서로 다른 옷의 조합의 수**를 return 하도록 `solution` 함수를 작성해주세요.

## 제한사항

- `clothes`의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
- 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
- 같은 이름을 가진 의상은 존재하지 않습니다.
- `clothes`의 모든 원소는 문자열로 이루어져 있습니다.
- 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
- 스파이는 **하루에 최소 한 개의 의상**은 입습니다.

## 입출력 예

|clothes|return|
|-------|------|
|[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]|5|
|[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]|3|

## 입출력 예 설명

### 예제 #1

headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

```
1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
```

### 예제 #2

face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

```
1. crow_mask
2. blue_sunglasses
3. smoky_makeup
```

## 풀이

고등학생 때 배웠던 전형적인 **경우의 수** 문제입니다.  
우선, 2차원 배열 `clothes`로부터 key가 의상 종류, value가 의상 이름인 dictionary를 만듭니다.  
예제 #1의 경우에는 아래와 같습니다.

```
(2차원 배열)
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

->

(dictionary)
{"headgear": {"yellowhat", "green_turban"}, "eyewear": {bluesunglasses"}}
```

저는 value의 type으로 set을 사용했지만, 제한사항에서 같은 이름을 가진 의상은 존재하지 않는다고 명시했으므로 list를 사용해도 상관없습니다.  
이제 위 dictionary로부터 서로 다른 옷의 조합의 수를 구할 수 있습니다.  
의상 종류(key)에서 서로 다른 옷의 조합을 고르는 경우의 수는 **해당 의상 종류에 속하는 의상의 개수에 1을 더한 값**(`len(value) + 1`)입니다.  
왜냐하면, 해당 의상 종류를 선택하지 않아도 되기 때문입니다.  
그렇게 구한 경우의 수를 `answer`에 할당한 후, 1을 빼줘야 합니다.  
스파이는 하루에 최소 한 개의 의상을 입어야 하므로 각 key에서 모두 선택하지 않은 경우는 제외해야 하기 때문입니다.

```python
from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(set)
    answer = 1

    for clothe_name, clothe_type in clothes:
        clothes_dict[clothe_type].add(clothe_name)
    
    for clothe_names in clothes_dict.values():
        answer *= len(clothe_names) + 1
        
    return answer - 1
```