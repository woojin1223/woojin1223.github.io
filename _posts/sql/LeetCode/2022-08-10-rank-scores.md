---
title: "[LeetCode] Rank Scores"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/rank-scores/>

<br><br><br><br>

## 테이블 설명

### `Scores`

`Scores`는 게임의 점수가 있는 테이블이다.

(열 설명)

- `id`: id에 해당한다.
- `score`: 점수에 해당한다.

(예시)

|id|score|
|:-:|:-:|
|1|3.50|
|2|3.65|
|3|4.00|
|4|3.85|
|5|4.00|
|6|3.65|

<br><br><br><br>

## 문제 설명

게임 점수의 순위를 매기는 문제다. 단, 순위는 다음의 규칙을 따른다.

1. 점수가 감소하는 방향으로 순위를 매긴다. 즉, 높은 점수가 높은 순위를 가진다.
2. 같은 점수인 경우 동일한 순위를 가진다.
3. 동일한 순위를 매기고 난 후, 다음으로 매길 순위는 바로 다음 번호다. 즉, 순위를 매길 때 번호의 끊김없이 연속적으로 매긴다.

<br><br><br><br>

## 사고 과정

### 1. 점수의 순위를 매긴다.

`DENSE_RANK() OVER ()`을 이용하면 같은 점수면 공동 순위로 기록되고 번호의 끊김없이 연속적으로 매길 수 있다.  
그리고 그렇게 매긴 순위를 기준으로 오름차순 정렬이 된다.

```sql
SELECT 
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank' 
FROM 
    scores
```

(출력)

|score|rank|
|:-:|:-:|
|4.00|1|
|4.00|1|
|3.85|2|
|3.65|3|
|3.65|3|
|3.50|4|

<br><br><br><br>

## 풀이

```sql
SELECT 
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank' 
FROM 
    scores
```