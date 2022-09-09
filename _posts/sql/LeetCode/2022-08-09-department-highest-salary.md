---
title: "[LeetCode] Department Highest Salary"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/department-highest-salary/>

<br><br><br><br>

## 테이블 설명

### `Employee`

`Employee`는 직원들의 연봉이 있는 테이블이다.

(열 설명)

- `id`: 직원의 id에 해당한다.
- `name`: 직원의 이름에 해당한다.
- `salary`: 직원의 연봉에 해당한다.
- `departmentId`: 직원이 속한 부서의 id에 해당한다.

(예시)

|id|name|salary|departmentId|
|:-:|:-:|:-:|:-:|
|1|Joe|70000|1|
|2|Jim|90000|1|
|3|Henry|80000|2|
|4|Sam|60000|2|
|5|Max|90000|1|

### `Department`

`Department`는 부서의 정보가 있는 테이블이다.

(열 설명)

- `id`: 부서의 id에 해당한다.
- `name`: 부서의 이름에 해당한다.

(예시)

|id|name|
|:-:|:-:|
|1|IT|
|2|Sales|

<br><br><br><br>

## 문제 설명

각 부서별로 제일 높은 연봉을 받는 인원들을 구하는 문제다.  
단, 연봉이 같은 경우도 포함한다.

<br><br><br><br>

## 사고 과정

### 1. `Employee`와 `Department`를 결합한 후, 각 부서별로 연봉 순위를 매긴다.

`DENSE_RANK() OVER ()`을 이용하면 같은 연봉이면 공동 순위로 기록된다.

```sql
SELECT 
    d.name AS department, 
    e.name AS employee, 
    salary, 
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS d_rank 
FROM 
    employee AS e 
    LEFT JOIN department AS d 
        ON e.departmentId = d.id
```

(출력)

|department|employee|salary|d_rank|
|:-:|:-:|:-:|:-:|
|IT|Max|90000|1|
|IT|Jim|90000|1|
|IT|Joe|70000|2|
|Sales|Henry|80000|1|
|Sales|Sam|60000|2|

### 2. 위 테이블에서 각 부서별 제일 높은 연봉을 받는 인원들을 추출한다.

WHERE 절을 이용하면 제일 높은 연봉을 받는 인원들을 추출할 수 있다.

```sql
SELECT 
    Department, 
    Employee, 
    Salary 
FROM (
    SELECT 
        d.name AS department, 
        e.name AS employee, 
        salary, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS d_rank 
    FROM 
        employee AS e 
        LEFT JOIN department AS d 
            ON e.departmentId = d.id
    ) AS sub 
WHERE 
    d_rank = 1
```

(출력)

|Department|Employee|Salary|
|:-:|:-:|:-:|
|IT|Max|90000|
|IT|Jim|90000|
|Sales|Henry|80000|

<br><br><br><br>

## 풀이

```sql
SELECT 
    Department, 
    Employee, 
    Salary 
FROM (
    SELECT 
        d.name AS department, 
        e.name AS employee, 
        salary, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS d_rank 
    FROM 
        employee AS e 
        LEFT JOIN department AS d 
            ON e.departmentId = d.id
    ) AS sub 
WHERE 
    d_rank = 1
```