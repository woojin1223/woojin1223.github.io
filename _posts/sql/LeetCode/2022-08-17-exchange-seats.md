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

`Seat` 테이블에서 연속된 두 학생들끼리 서로 위치를 바꾼 결과를 구하는 문제다.  
단, 학생의 수가 홀수인 경우 맨 끝의 학생의 위치는 바뀌지 않는다. 예시 테이블에서 학생들의 위치를 바꾼 결과는 다음과 같다.

|id|student|
|:-:|:-:|
|1|Doris|
|2|Abbot|
|3|Green|
|4|Emerson|
|5|Jeames|

<br><br><br><br>

## 사고 과정

### 1. 연속된 두 학생의 id 값을 서로 바꾼 결과를 `swapped_id` 열에 저장한다.

IF 문을 이용하여 `id` 값이 짝수인 경우 `id` 값에 1을 뺀 `id - 1`로 대체하고 `id` 값이 홀수인 경우 `id` 값에 1을 더한 `id + 1`로 대체하면 연속된 두 학생의 id를 서로 바꿀 수 있다.  
단, 학생의 수가 홀수인 경우 마지막 학생의 `id`를 따로 처리해야 한다.

```sql
SELECT 
    id, 
    student, 
    IF(id % 2 = 0, id - 1, id + 1) AS swapped_id, 
FROM 
    seat
```

(출력)

|id|student|swapped_id|
|:-:|:-:|:-:|
|1|Abbot|2|
|2|Doris|1|
|3|Emerson|4|
|4|Green|3|
|5|Jeames|6|

### 2. `swapped_id`의 값과 같은 순서로 행 번호를 매겨 `id` 열에 저장한다.

위의 예시처럼 학생의 수가 홀수인 경우 마지막 학생의 `swapped_id` 값이 5가 아닌 6이 나온다.  
이를 처리하기 위해서 마지막 학생의 `swapped_id` 값만을 변경하는 건 힘들다.  
하지만 `swapped_id`의 순위와 문제에서 구하고자 하는 `id`의 순위는 동일하므로 `swapped_id`의 값과 같은 순서로 행 번호를 매겨 학생의 수가 홀수일 때 마지막 학생의 `id` 값까지 변경되는 문제를 해결할 수 있다.

```sql
SELECT 
    ROW_NUMBER() OVER (ORDER BY swapped_id) AS id, 
    student 
FROM (
    SELECT 
        IF(id % 2 = 0, id - 1, id + 1) AS swapped_id, 
        student 
    FROM 
        seat
    ) AS sub
```

(출력)

|id|student|
|:-:|:-:|
|1|Doris|
|2|Abbot|
|3|Green|
|4|Emerson|
|5|Jeames|

<br><br><br><br>

## 풀이

```sql
SELECT 
    ROW_NUMBER() OVER (ORDER BY swapped_id) AS id, 
    student 
FROM (
    SELECT 
        IF(id % 2 = 0, id - 1, id + 1) AS swapped_id, 
        student 
    FROM 
        seat
    ) AS sub
```