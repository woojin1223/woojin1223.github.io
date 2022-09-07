---
title: "[LeetCode] Second Highest Salary"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/second-highest-salary/>

<br><br><br><br>

## 테이블 설명

### `Employee`

`Employee`는 직원들의 연봉이 있는 테이블이다.

(열 설명)

- `id`: 직원의 id에 해당한다.
- `salary`: 직원의 연봉에 해당한다.

(예시 1)

|id|salary|
|:-:|:-:|
|1|100|
|2|200|
|3|300|

(예시 2)

|id|salary|
|:-:|:-:|
|1|100|

<br><br><br><br>

## 문제 설명

`Employee` 테이블에서 두 번째로 높은 연봉을 구하는 문제다.  
단, 해당하는 값이 없다면 `NULL`을 반환한다.  
(예시 1)은 200, (예시 2)는 `NULL`이 나온다.

<br><br><br><br>

## 사고 과정

### 1. 두 번째로 높은 연봉을 구한다.

`Employee` 테이블의 `salary` 열에서 중복된 값을 제거한 후, 내림차순으로 정렬한다.  
`LIMIT` 함수를 이용하여 테이블의 두 번째 행에 해당하는 값만을 추출할 수 있다.  

(참고)  
`LIMIT a, b`: 인덱스 a부터 시작하여 총 b개의 행을 가져온다.

```sql
SELECT 
    DISTINCT salary AS SecondHighestSalary
FROM 
    employee 
ORDER BY 
    salary DESC 
LIMIT 1, 1
```

(출력 1)

|SecondHighestSalary|
|:-:|
|200|

(출력 2)

|SecondHighestSalary|
|:-:|
||

### 2. 두 번째로 높은 연봉이 없는 경우 `NULL`을 반환한다.

`IFNULL` 함수를 이용하면 두 번째로 높은 연봉이 없는 경우 `NULL`을 반환할 수 있다.


(참고)  
`IFNULL(expr1, expr2)`: expr1에 해당하는 값이 있다면 expr1 반환, 해당하는 값이 없다면 expr2 반환

```sql
SELECT 
    IFNULL((SELECT 
               DISTINCT salary
           FROM 
               employee 
           ORDER BY 
               salary DESC 
           LIMIT 1, 1), NULL) AS SecondHighestSalary
```

(출력 1)

|SecondHighestSalary|
|:-:|
|200|

(출력 2)

|SecondHighestSalary|
|:-:|
|NULL|

<br><br><br><br>

## 풀이

```sql
SELECT 
    IFNULL((SELECT 
               DISTINCT salary
           FROM 
               employee 
           ORDER BY 
               salary DESC 
           LIMIT 1, 1), NULL) AS SecondHighestSalary
```