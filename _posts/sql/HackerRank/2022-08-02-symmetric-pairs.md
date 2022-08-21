---
title: "[HackerRank] Symmetric Pairs"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/symmetric-pairs/problem>

<br><br><br><br>

## 테이블 설명

`Functions` 테이블의 두 컬럼 x, y는 각각 데카르트 좌표계의 x 좌표값, y 좌표값을 의미한다.

(예시)

|x|y|
|:-:|:-:|
|20|20|
|20|20|
|20|21|
|23|22|
|22|23|
|21|20|

<br><br><br><br>

## 문제 설명

데카르트 좌표계의 두 점 $(x_1, y_1)$와 $(x_2, y_2)$가 $(x_1, y_1) = (y_2, x_2)$를 만족할 때 **symmetric pairs**라고 부른다.  
`Functions` 테이블에서 $x \leq y$를 만족하는 symmetric pairs $(x, y)$를 찾는 문제다.  
단, $x$ 값에 대해 오름차순으로 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. x와 y 중 작은 값을 x, 큰 값을 y로 하여 새롭게 x, y를 만든다.

$(x_1, y_1) = (y_2, x_2)$일 때 x와 y 중 작은 값을 x, 큰 값을 y으로 설정하면 $(x_1, y_1) = (x_2, y_2)$가 된다.  
즉, $(x_1, y_1)$와 $(x_2, y_2)$가 symmetric pairs라면 $x_1 \leq y_1$를 만족하는 $(x_1, y_1)$가 2개 이상 존재하게 된다.

(함수 설명)

- `LEAST(col1, col2, ...)`: col1, col2, ... 중 작은 값을 반환한다.
- `GREAST(col1, col2, ...)`: col1, col2, ... 중 큰 값을 반환한다.

```sql
SELECT 
    LEAST(x, y)    AS x, 
    GREATEST(x, y) AS y 
FROM 
    functions
```

### 2. x, y를 기준으로 그룹화하여 그룹 내의 행 수가 2 이상인 경우만 추출한다.

위 과정을 통해 x, y를 새롭게 만들고 나면, $(x, y)$의 중복 유무로 symmetric pairs를 찾을 수 있다.  
중복된 $(x, y)$는 x, y를 기준으로 그룹화한 후 그룹 내의 행 수가 2 이상인 $(x, y)$를 찾으면 된다.

```sql
SELECT 
    x, y
FROM (
    SELECT 
        LEAST(x, y)    AS x, 
        GREATEST(x, y) AS y 
    FROM 
        functions
    ) AS fns 
GROUP BY 
    x, y 
HAVING 
    COUNT(*) >= 2 
```

### 3. x 값을 기준으로 오름차순 정렬한다.

```sql
SELECT 
    x, y
FROM (
    SELECT 
        LEAST(x, y)    AS x, 
        GREATEST(x, y) AS y 
    FROM 
        functions
    ) AS fns 
GROUP BY 
  x, y 
HAVING 
  COUNT(*) >= 2 
ORDER BY x
```

<br><br><br><br>

## 풀이

```sql
SELECT 
    x, y
FROM (
    SELECT 
        LEAST(x, y)    AS x, 
        GREATEST(x, y) AS y 
    FROM 
        functions
    ) AS fns 
GROUP BY 
    x, y 
HAVING 
    COUNT(*) >= 2 
ORDER BY x
```