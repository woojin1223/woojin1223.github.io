---
title: "[LeetCode] Consecutive Numbers"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/consecutive-numbers/>

<br><br><br><br>

## 테이블 설명

### `Logs`

`Logs`는 id와 숫자가 있는 테이블이다.

(열 설명)

- `id`: id에 해당한다.
- `num`: 숫자에 해당한다.

(예시)

|id|num|
|:-:|:-:|
|1|1|
|2|1|
|3|1|
|4|2|
|5|1|
|6|2|
|7|2|

<br><br><br><br>

## 문제 설명

`Logs`에서 같은 숫자가 연속으로 세 번 이상 나오는 경우, 그 숫자를 구하는 문제다.

<br><br><br><br>

## 사고 과정

### 1. `id` 순으로 행 번호를 매긴 열 `row_num1`을 만든다.

주어진 예시에서는 `id`와 `row_num1`의 결과가 같다.  
하지만, 다른 예시에서는 `id`가 1부터 시작하여 하나씩 증가하는 형태가 아닐 수 있으므로 `id` 순으로 행 번호를 매긴 `row_num1`을 만들었다.

```sql
SELECT 
    num, 
    ROW_NUMBER() OVER(ORDER BY id) AS row_num1 
FROM 
    logs
```

(출력)

|num|row_num1|
|:-:|:-:|
|1|1|
|1|2|
|1|3|
|2|4|
|1|5|
|2|6|
|2|7|

### 2. `num`을 기준으로 그룹화하여 그룹 내에서 `id` 순으로 행 번호를 매긴 열 `row_num2`를 만든다.

`row_num1`과는 다른 방법을 이용하여 `row_num2`를 만든다.  
즉, 같은 `num` 값 내에서 `id` 순으로 행 번호를 매긴다.

```sql
SELECT 
    num, 
    ROW_NUMBER() OVER(ORDER BY id) AS row_num1, 
    ROW_NUMBER() OVER(PARTITION BY num ORDER BY id) AS row_num2 
FROM 
    logs
```

(출력)

|num|row_num1|row_num2|
|:-:|:-:|:-:|
|1|1|1|
|1|2|2|
|1|3|3|
|2|4|1|
|1|5|4|
|2|6|2|
|2|7|3|

### 3. `row_num1`과 `row_num2`를 이용하여 연속으로 최소 세 번 나오는 숫자를 구한다.

위에서 만든 `row_num1`과 `row_num2`를 이용하면 연속으로 같은 숫자가 나오는 것을 그룹화할 수 있다.  
즉, `row_num1 - row_num2`와 `num`을 기준으로 그룹화하면 연속적이고 같은 값을 가진 숫자들을 그룹화할 수 있다.

```sql
SELECT 
    row_num1 - row_num2, 
    num, 
    COUNT(*) AS cnt 
FROM (
    SELECT 
        num, 
        ROW_NUMBER() OVER(ORDER BY id) AS row_num1, 
        ROW_NUMBER() OVER(PARTITION BY num ORDER BY id) AS row_num2 
    FROM 
        logs
    ) AS sub 
GROUP BY 
    row_num1 - row_num2, num
```

(출력)

|row_num1 - row_num2|num|cnt|
|:-:|:-:|:-:|
|0|1|3|
|1|1|1|
|3|2|1|
|4|2|2|

위의 `num` 열이 연속적으로 같은 값을 가지는 숫자에 해당하고 `cnt` 열이 연속으로 나온 횟수에 해당한다.  
따라서, 연속으로 나오는 횟수가 3 이상인 `num`을 추출하면 된다.  
즉, `row_num1 - row_num2`와 `num`을 기준으로 그룹화하여 그룹에 속한 데이터의 개수가 3 이상인 경우를 구하면 된다.

```sql
SELECT 
    DISTINCT MIN(num) AS ConsecutiveNums 
FROM (
    SELECT 
        num, 
        ROW_NUMBER() OVER (ORDER BY id)                  AS row_num1, 
        ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS row_num2 
    FROM 
        logs
    ) AS sub 
GROUP BY 
    row_num1 - row_num2, num 
HAVING 
    COUNT(*) >= 3
```

(출력)

|ConsecutiveNums|
|:-:|
|1|

<br><br><br><br>

## 풀이

```sql
SELECT 
    DISTINCT MIN(num) AS ConsecutiveNums 
FROM (
    SELECT 
        num, 
        ROW_NUMBER() OVER (ORDER BY id)                  AS row_num1, 
        ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS row_num2 
    FROM 
        logs
    ) AS sub 
GROUP BY 
    row_num1 - row_num2, num 
HAVING 
    COUNT(*) >= 3
```