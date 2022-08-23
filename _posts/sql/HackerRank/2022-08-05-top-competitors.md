---
title: "[HackerRank] Top Competitors"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/full-score/problem>

<br><br><br><br>

## 테이블 설명

### `Hackers`

`Hackers`는 <u>코딩 테스트 참가자</u>(해커)의 정보가 있는 테이블이다.

(컬럼 설명)

- `hacker_id`: 해커의 id
- `name`: 해커의 이름

(예시)

|hacker_id|name|
|:-:|:-:|
|5580|Rose|
|8439|Angela|
|27205|Frank|
|52243|Patrick|
|52348|Lisa|
|57645|Kimberly|
|77726|Bonnie|
|83082|Michael|
|86870|Todd|
|90411|Joe|

### `Difficulty`

`Difficulty`는 코딩 테스트 문제의 난이도에 대한 테이블이다.

(컬럼 설명)

- `difficulty_level`: 문제의 난이도
- `score`: 만점에 해당하는 점수

(예시)

|difficulty_level|score|
|:-:|:-:|
|1|20|
|2|30|
|3|40|
|4|60|
|5|80|
|6|100|
|7|120|

### `Challenges`

`Challenges`는 코딩 테스트의 문제에 대한 테이블이다.

(컬럼 설명)

- `challenge_id`: 문제의 id
- `hacker_id`: 문제를 만든 해커의 id (사용하지 않는 열)
- `difficulty_level`: 문제의 난이도

(예시)

|challenge_id|hacker_id|difficulty_level|
|:-:|:-:|:-:|
|4810|77726|4|
|21089|27205|1|
|36566|5580|7|
|66730|52243|6|
|71055|52243|2|

### `Submissions`

`Submissions`는 코딩 테스트 제출 정보에 대한 테이블이다.

(컬럼 설명)

- `submission_id`: 제출의 id
- `hacker_id`: 제출한 해커의 id
- `challenge_id`: 제출한 문제의 id
- `score`: 제출한 문제에서 해커가 얻은 점수

(예시)

![](https://s3.amazonaws.com/hr-challenge-images/19504/1458527812-479a74b99f-ScreenShot2016-03-21at8.06.05AM.png)

<br><br><br><br>

## 문제 설명

코딩 테스트에서 **두 문제 이상 만점을 받은 해커**의 id와 이름을 찾는 문제다.  
단, 만점을 받은 문제의 개수를 기준으로 내림차순, `hacker_id`를 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. `Submissions`와 `Challenges`, `Difficulty`, `Hackers`를 결합한다.

두 문제 이상 만점을 받은 해커의 id와 이름을 찾으려면 테이블 `Submissions`의 정보에다가 해커의 이름과 제출한 문제의 만점에 해당하는 점수가 필요하다. 연속된 테이블 결합을 통해서 `Submissions`에 필요한 열을 추가할 수 있다.

1. 테이블 `Challenges`로부터 각 문제의 난이도에 해당하는 `difficulty_level` 열을 가져 온다.
2. 테이블 `Difficulty`로부터 각 문제의 난이도별 만점에 해당하는 점수인 `score` 열을 가져 온다. (`Submissions`의 `score` 열과 다름)
3. 테이블 `Hackers`로부터 해커의 이름에 해당하는 `name` 열을 가져 온다.

```sql
SELECT 
    submission_id, 
    h.hacker_id, 
    h.name AS hacker_name, 
    s.challenge_id, 
    d.difficulty_level, 
    s.score AS score, 
    d.score AS full_score 
FROM 
    submissions AS s 
    LEFT JOIN challenges 
        USING (challenge_id) 
    LEFT JOIN difficulty AS d 
        USING (difficulty_level) 
    LEFT JOIN hackers AS h 
        ON s.hacker_id = h.hacker_id
```

(일부 출력)

|submission_id|hacker_id|hacker_name|challenge_id|difficulty_level|score|full_score|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|68628|77726|Bonnie|36566|7|30|120|
|65300|77726|Bonnie|21089|1|10|20|

### 2. 1.의 결과에서 만점을 받은 경우만 필터링한다.

`Submissions`의 `score` 값과 `Difficulty`의 `score` 값이 같으면 제출한 문제에서 만점을 받은 것이다.  
즉, WHERE 절 `WHERE s.score = d.score`를 추가하여 만점을 받은 제출만 필터링한다.

```sql
SELECT 
    submission_id, 
    h.hacker_id, 
    h.name AS hacker_name, 
    s.challenge_id, 
    d.difficulty_level, 
    s.score AS score, 
    d.score AS full_score 
FROM 
    submissions AS s 
    LEFT JOIN challenges 
        USING (challenge_id) 
    LEFT JOIN difficulty AS d 
        USING (difficulty_level) 
    LEFT JOIN hackers AS h 
        ON s.hacker_id = h.hacker_id 
WHERE 
    s.score = d.score
```

(출력)

|submission_id|hacker_id|hacker_name|challenge_id|difficulty_level|score|full_score|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|94613|86870|Todd|71055|2|30|30|
|97397|90411|Joe|66730|6|100|100|
|97431|90411|Joe|71055|2|30|30|

### 3. 두 문제 이상 만점을 받은 해커의 id와 이름을 구한다.

**두 문제 이상** 만점을 받은 해커의 id와 이름을 구하기 위해 2.의 결과에서 `hacker_id`와 `name`을 기준으로 그룹화하여 그룹에 속한 행이 두 개 이상인 경우만 필터링한다.  
아래와 같이 `GROUP BY ... HAVING ...`을 추가하여 구할 수 있다.

```sql
SELECT 
    h.hacker_id, 
    h.name AS hacker_name 
FROM 
    submissions AS s 
    LEFT JOIN challenges 
        USING (challenge_id) 
    LEFT JOIN difficulty AS d 
        USING (difficulty_level) 
    LEFT JOIN hackers AS h 
        ON s.hacker_id = h.hacker_id 
WHERE 
    s.score = d.score 
GROUP BY 
    h.hacker_id, h.name 
HAVING 
    COUNT(*) > 1
```

(출력)

|hacker_id|hacker_name|
|:-:|:-:|
|90411|Joe|

### 4. 만점을 받은 문제의 개수를 기준으로 내림차순, `hacker_id` 기준으로 오름차순 정렬한다.

```sql
SELECT 
    h.hacker_id, 
    h.name AS hacker_name 
FROM 
    submissions AS s 
    LEFT JOIN challenges 
        USING (challenge_id) 
    LEFT JOIN difficulty AS d 
        USING (difficulty_level) 
    LEFT JOIN hackers AS h 
        ON s.hacker_id = h.hacker_id 
WHERE 
    s.score = d.score 
GROUP BY 
    h.hacker_id, h.name 
HAVING 
    COUNT(*) > 1 
ORDER BY 
    COUNT(*) DESC, h.hacker_id
```

<br><br><br><br>

## 풀이

```sql
SELECT 
    h.hacker_id, 
    h.name AS hacker_name 
FROM 
    submissions AS s 
    LEFT JOIN challenges 
        USING (challenge_id) 
    LEFT JOIN difficulty AS d 
        USING (difficulty_level) 
    LEFT JOIN hackers AS h 
        ON s.hacker_id = h.hacker_id 
WHERE 
    s.score = d.score 
GROUP BY 
    h.hacker_id, h.name 
HAVING 
    COUNT(*) > 1 
ORDER BY 
    COUNT(*) DESC, h.hacker_id
```