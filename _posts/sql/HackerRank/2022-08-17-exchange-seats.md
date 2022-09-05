---
title: "[LeetCode] Exchange Seats"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/exchange-seats/>

<br><br><br><br>

## 테이블 설명

### `Seat`

`Seat`는 학생의 id와 이름이 있는 테이블이다.

(열 설명)

- `id`: 학생의 id에 해당한다.
- `num`: 학생의 이름에 해당한다.

(예시)

|id|student|
|:-:|:-:|
|1|Abbot|
|2|Doris|
|3|Emerson|
|4|Green|
|5|Jeames|

<br><br><br><br>

## 문제 설명

<br><br><br><br>

## 사고 과정

<br><br><br><br>

## 풀이

```sql
SELECT 
    ROW_NUMBER() OVER (ORDER BY id) AS id, 
    student 
FROM (
    SELECT 
        IF(id % 2 = 0, id - 1, id + 1) AS id, 
        student 
    FROM 
        seat 
    ORDER BY 
        id
    ) AS sub
```