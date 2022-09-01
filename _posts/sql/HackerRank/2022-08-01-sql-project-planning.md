---
title: "[HackerRank] SQL Project Planning"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/sql-projects/problem>

<br><br><br><br>

## 테이블 설명

### `Projects`

`Projects`는 일을 시작한 날짜와 끝낸 날짜가 있는 테이블이다.  
각 행에서 시작한 날짜와 끝낸 날짜의 차이는 1일로 모두 동일하다.

(열 설명)

- `Task_ID`: 일의 id에 해당한다.
- `Start_Date`: 일을 시작한 날짜에 해당한다.
- `End_Date`: 일을 끝낸 날짜에 해당한다.

(예시)

|Task_ID|Start_Date|End_Date|
|:-:|:-:|:-:|
|1|2015-10-01|2015-10-02|
|2|2015-10-02|2015-10-03|
|3|2015-10-03|2015-10-04|
|4|2015-10-13|2015-10-14|
|5|2015-10-14|2015-10-15|
|6|2015-10-28|2015-10-29|
|7|2015-10-30|2015-10-31|

<br><br><br><br>

## 문제 설명

테이블 `Projects`의 일들을 프로젝트 단위로 묶어서 각 프로젝트의 시작한 날짜와 끝낸 날짜를 구하는 문제다.  
일의 끝낸 날짜가 연속적인 경우, 해당 일들을 하나의 프로젝트로 취급한다.  
단, 프로젝트의 기간과 시작한 날짜를 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. `start_date`와 `end_date`의 [대칭 차집합](https://ko.wikipedia.org/wiki/%EB%8C%80%EC%B9%AD%EC%B0%A8)을 구한다.


일들을 프로젝트 단위로 묶기 위해서는 열 `start_date`와 열 `end_date`에서 같은 값이 나오는지 확인 후 연속적으로 같은 값이 나오는 행들을 하나의 그룹으로 보고 각 그룹에서 `start_date`의 최솟값과 `end_date`의 최댓값을 구해야 한다.  
이 복잡한 작업을 쉽게 하기 위해서 열 `start_date`와 열 `end_date`에서 공통적으로 나오는 데이터를 제외한다.  
그러고 나서 공통 원소가 없는 `start_date`와 `end_date`를 각각 정렬하여 열 방향으로 결합하면 된다.  
우선, 열 `start_date`와 열 `end_date`의 대칭 차집합을 구하자.  
먼저, 차집합 `start_date` - `end_date`을 구한 후 날짜 순으로 행 번호를 매긴 열 `row_num`을 추가한다.

```sql
SELECT 
    start_date, 
    ROW_NUMBER() OVER (ORDER BY start_date) AS row_num 
FROM 
    projects 
WHERE 
    start_date NOT IN (SELECT end_date FROM projects)
```

(출력)

|start_date|row_num|
|:-:|:-:|
|2015-10-01|1|
|2015-10-13|2|
|2015-10-28|3|
|2015-10-30|4|

다음으로, 차집합 `end_date` - `start_date`을 구한 후 날짜 순으로 행 번호를 매긴 열 `row_num`을 추가한다.

```sql
SELECT 
    end_date, 
    ROW_NUMBER() OVER (ORDER BY end_date) AS row_num 
FROM 
    projects 
WHERE 
    end_date NOT IN (SELECT start_date FROM projects)
```

(출력)

|end_date|row_num|
|:-:|:-:|
|2015-10-04|1|
|2015-10-15|2|
|2015-10-29|3|
|2015-10-31|4|

### 2. 열 `row_num`을 공통의 키로 하여, 1.에서 구한 두 차집합을 열 방향으로 합친다.

```sql
SELECT 
    start_date, 
    end_date 
FROM (
    SELECT 
        start_date, 
        ROW_NUMBER() OVER (ORDER BY start_date) AS row_num 
    FROM 
        projects 
    WHERE 
        start_date NOT IN (SELECT end_date FROM projects)
    ) AS start_dates 
    INNER JOIN (
        SELECT 
            end_date, 
            ROW_NUMBER() OVER (ORDER BY end_date) AS row_num 
        FROM 
            projects 
        WHERE 
            end_date NOT IN (SELECT start_date FROM projects)
        ) AS end_dates 
        USING (row_num) 
```

(출력)

|start_date|end_date|
|:-:|:-:|
|2015-10-01|2015-10-04|
|2015-10-13|2015-10-15|
|2015-10-28|2015-10-29|
|2015-10-30|2015-10-31|

### 3. 프로젝트의 기간과 시작한 날짜를 기준으로 오름차순 정렬한다.

2.에서 만든 두 열은 DATE 형식이기 때문에 `DATEDIFF` 함수를 이용하여 두 열의 차이값을 계산할 수 있다.

```sql
SELECT 
    start_date, 
    end_date 
FROM (
    SELECT 
        start_date, 
        ROW_NUMBER() OVER (ORDER BY start_date) AS row_num 
    FROM 
        projects 
    WHERE 
        start_date NOT IN (SELECT end_date FROM projects)
    ) AS start_dates 
    INNER JOIN (
        SELECT 
            end_date, 
            ROW_NUMBER() OVER (ORDER BY end_date) AS row_num 
        FROM 
            projects 
        WHERE 
            end_date NOT IN (SELECT start_date FROM projects)
        ) AS end_dates 
        USING (row_num) 
ORDER BY 
    DATEDIFF(end_date, start_date), start_date
```

(출력)

|start_date|end_date|
|:-:|:-:|
|2015-10-28|2015-10-29|
|2015-10-30|2015-10-31|
|2015-10-13|2015-10-15|
|2015-10-01|2015-10-04|

<br><br><br><br>

## 풀이

```sql
SELECT 
    start_date, 
    end_date 
FROM (
    SELECT 
        start_date, 
        ROW_NUMBER() OVER (ORDER BY start_date) AS row_num 
    FROM 
        projects 
    WHERE 
        start_date NOT IN (SELECT end_date FROM projects)
    ) AS start_dates 
    INNER JOIN (
        SELECT 
            end_date, 
            ROW_NUMBER() OVER (ORDER BY end_date) AS row_num 
        FROM 
            projects 
        WHERE 
            end_date NOT IN (SELECT start_date FROM projects)
        ) AS end_dates 
        USING (row_num) 
ORDER BY 
    DATEDIFF(end_date, start_date), start_date
```