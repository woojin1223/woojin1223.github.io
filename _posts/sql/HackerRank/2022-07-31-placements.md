---
title: "[HackerRank] Placements"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/placements/problem>

<br><br><br><br>

## 테이블 설명

### `Students`

`Students`는 학생들의 정보에 해당하는 테이블이다.

(열 설명)

- `ID`: 학생 id에 해당한다.  
- `Name`: 학생 이름에 해당한다.

(예시)

|ID|Name|
|:-:|:-:|
|1|Ashely|
|2|Samantha|
|3|Julia|
|4|Scarlet|

### `Friends`

학생들은 단 한 명의 친구가 있다.  
`Friends`는 학생이 누구와 친구인지를 알려 주는 테이블이다.

(열 설명)

- `ID`: 학생 id에 해당한다.
- `Friend_ID`: 친구 id에 해당한다.

(예시)

|ID|Friend_ID|
|:-:|:-:|
|1|2|
|2|3|
|3|4|
|4|1|

### `Packages`

`Packages`는 학생들의 월급에 해당하는 테이블이다.

(열 설명)

- `ID`: 학생 id에 해당한다.
- `Salary`: 제안받은 월급에 해당한다.

(예시)

|ID|Salary|
|:-:|:-:|
|1|15.20|
|2|10.06|
|3|11.55|
|4|12.12|

<br><br><br><br>

## 문제 설명

본인 월급보다 친구 월급이 더 많은 학생의 이름을 찾는 문제다.  
단, 친구 월급을 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. `Friends`와 `Students`, `Packages`를 결합한다.

본인 월급보다 친구 월급이 더 많은 학생의 이름을 찾으려면 테이블 `Friends`의 정보에다가 학생의 이름과 학생의 월급, 친구의 월급에 대한 정보가 필요하다. 연속된 테이블 결합을 통해서 `Friends`에 필요한 열을 추가할 수 있다.

1. 테이블 `Students`로부터 학생의 이름에 해당하는 `Name` 열을 가져 온다.
   - `Friends`의 `ID` 열과 `Students`의 `ID` 열을 공통의 키로 하는 것이 결합 조건이다.
2. 테이블 `Packages`로부터 학생의 월급에 해당하는 `Salary` 열을 가져 온다. (`p1.salary`에 해당)
   - `Friends`의 `ID` 열과 `Packages`의 `ID` 열을 공통의 키로 하는 것이 결합 조건이다.
3. 테이블 `Packages`로부터 친구의 월급에 해당하는 `Salary` 열을 가져 온다. (`p2.salary`에 해당)
   - `Friends`의 `Friend_ID` 열과 `Packages`의 `ID` 열을 공통의 키로 하는 것이 결합 조건이다.

```sql
SELECT 
    f.id, 
    name, 
    f.friend_id, 
    p1.salary, 
    p2.salary AS friend_salary
FROM 
    friends AS f 
    LEFT JOIN students 
        USING (id) 
    LEFT JOIN packages AS p1 
        USING (id) 
    LEFT JOIN packages AS p2 
        ON f.friend_id = p2.id
```

(출력)

|id|name|friend_id|salary|friend_salary|
|:-:|:-:|:-:|:-:|:-:|
|1|Ashely|2|15.20|10.06|
|2|Samantha|3|10.06|11.55|
|3|Julia|4|11.55|12.12|
|4|Scarlet|1|12.12|15.20|

### 2. 본인 월급보다 친구 월급이 더 많은 학생의 이름을 구한다.

WHERE 절을 이용하여 본인 월급(`p1.salary`)보다 친구 월급(`p2.salary`)이 더 많은 학생의 이름을 구할 수 있다.

```sql
SELECT 
    name 
FROM 
    friends AS f 
    LEFT JOIN students 
        USING (id) 
    LEFT JOIN packages AS p1 
        USING (id) 
    LEFT JOIN packages AS p2 
        ON f.friend_id = p2.id 
WHERE 
    p1.salary < p2.salary
```

(출력)

|name|
|:-:|
|Samantha|
|Julia|
|Scarlet|

### 3. 친구 월급을 기준으로 오름차순 정렬한다.

```sql
SELECT 
    name 
FROM 
    friends AS f 
    LEFT JOIN students 
        USING (id) 
    LEFT JOIN packages AS p1 
        USING (id) 
    LEFT JOIN packages AS p2 
        ON f.friend_id = p2.id 
WHERE 
    p1.salary < p2.salary 
ORDER BY 
    p2.salary
```

<br><br><br><br>

## 풀이

```sql
SELECT 
    name 
FROM 
    friends AS f 
    LEFT JOIN students 
        USING (id) 
    LEFT JOIN packages AS p1 
        USING (id) 
    LEFT JOIN packages AS p2 
        ON f.friend_id = p2.id 
WHERE 
    p1.salary < p2.salary 
ORDER BY 
    p2.salary
```