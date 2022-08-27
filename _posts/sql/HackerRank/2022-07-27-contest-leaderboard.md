---
title: "[HackerRank] Contest Leaderboard"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/contest-leaderboard/problem>

<br><br><br><br>

## 테이블 설명

### `Hackers`

`Hackers`는 <u>코딩 테스트 참가자</u>(해커)의 정보가 있는 테이블이다.

(열 설명)

- `hacker_id`: 해커의 id
- `name`: 해커의 이름

(예시)

|hacker_id|name|
|:-:|:-:|
|4071|Rose|
|4806|Angela|
|26071|Frank|
|49438|Patrick|
|74842|Lisa|
|80305|Kimberly|
|84072|Bonnie|
|87868|Michael|
|92118|Todd|
|95895|Joe|

### `Submissions`

`Submissions`는 코딩 테스트 제출 정보에 대한 테이블이다.

(열 설명)

- `submission_id`: 제출의 id
- `hacker_id`: 제출한 해커의 id
- `challenge_id`: 제출한 문제의 id
- `score`: 제출한 문제에서 해커가 얻은 점수

(예시)

![](https://s3.amazonaws.com/hr-challenge-images/19503/1458523388-0896218137-ScreenShot2016-03-21at6.51.45AM.png)

<br><br><br><br>

## 문제 설명

해커별 id와 이름과 코딩 테스트에서 얻은 총 점수를 찾는 문제다.  
여기서 총 점수는 코딩 테스트 각 문제에서 기록한 점수들의 최댓값을 다 더한 점수다.  
단, 총 점수가 0인 해커는 제외한다. 그리고 총 점수를 기준으로 내림차순, `hacker_id`를 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. 해커별로 각 문제에서 기록한 최댓값을 구한다.

`hacker_id`와 `challenge_id`를 기준으로 그룹화한 후 각 그룹별 점수의 최댓값을 구하여 `max_score`라는 열에 저장한다.

```sql
 SELECT 
     hacker_id, 
     challenge_id, 
     MAX(score) AS max_score 
 FROM 
     submissions 
 GROUP BY 
     hacker_id, challenge_id
```

(일부 출력)

|hacker_id|challenge_id|max_score|
|:-:|:-:|:-:|
|4071|19797|95|
|4071|49593|96|

### 2. 1.의 결과에서 해커별로 id, 이름, 총 점수를 구한다.

1.의 결과에서 해커별로 총 점수를 구하기 전에 `Hackers` 테이블과 결합하여 `name` 열을 추가한다.  
그러고 나서, `hacker_id`와 `name`을 기준으로 그룹화한 후 각 그룹별 점수의 합을 구하여 `total_score`라는 열에 저장한다.

```sql
SELECT 
    hacker_id, 
    name AS hacker_name, 
    SUM(max_score) AS total_score 
FROM (
    SELECT 
        hacker_id, 
        MAX(score) AS max_score 
    FROM 
        submissions 
    GROUP BY 
        hacker_id, challenge_id
    ) AS sub
    LEFT JOIN hackers 
        USING (hacker_id) 
GROUP BY 
    hacker_id, name
```

(일부 출력)

|hacker_id|hacker_name|total_score|
|:-:|:-:|:-:|
|4071|Rose|191|
|74842|Lisa|174|

### 3. 총 점수가 0인 해커를 제외하고 총 점수 기준으로 내림차순, `hacker_id` 기준으로 오름차순 정렬한다.

```sql
SELECT 
    hacker_id, 
    name AS hacker_name, 
    SUM(max_score) AS total_score 
FROM (
    SELECT 
        hacker_id, 
        MAX(score) AS max_score 
    FROM 
        submissions 
    GROUP BY 
        hacker_id, challenge_id
    ) AS sub
    LEFT JOIN hackers 
        USING (hacker_id) 
GROUP BY 
    hacker_id, name 
HAVING 
    total_score > 0 
ORDER BY 
    total_score DESC, hacker_id
```

<br><br><br><br>

## 풀이

```sql
SELECT 
    hacker_id, 
    name AS hacker_name, 
    SUM(max_score) AS total_score 
FROM (
    SELECT 
        hacker_id, 
        MAX(score) AS max_score 
    FROM 
        submissions 
    GROUP BY 
        hacker_id, challenge_id
    ) AS sub
    LEFT JOIN hackers 
        USING (hacker_id) 
GROUP BY 
    hacker_id, name 
HAVING 
    total_score > 0 
ORDER BY 
    total_score DESC, hacker_id
```