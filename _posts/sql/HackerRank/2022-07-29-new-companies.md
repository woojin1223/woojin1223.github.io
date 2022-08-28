---
title: "[HackerRank] New Companies"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/the-company/problem>

<br><br><br><br>

## 테이블 설명

### `Company`

`Company`는 회사 정보에 해당하는 테이블이다.

(열 설명)

- `company_code`: 회사 코드에 해당한다.
- `founder`: 회사 설립자에 해당한다.

(예시)

|company_code|founder|
|:-:|:-:|
|C1|Monika|
|C2|Samantha|

### `Lead_Manager`

`Lead_Manager`는 lead manager가 포함된 회사 조직도 테이블이다.

(열 설명)

- `lead_manager_code`: lead manager 코드에 해당한다.
- `company_code`: 회사 코드에 해당한다.

(예시)

|lead_manager_code|company_code|
|:-:|:-:|
|LM1|C1|
|LM2|C2|

### `Senior_Manager`

`Senior_Manager`는 senior manager가 포함된 회사 조직도 테이블이다.

(열 설명)

- `senior_manager_code`: senior manager 코드에 해당한다.
- `lead_manager_code`: lead manager 코드에 해당한다.
- `company_code`: 회사 코드에 해당한다.

(예시)

|senior_manager_code|lead_manager_code|company_code|
|:-:|:-:|:-:|
|SM1|LM1|C1|
|SM2|LM1|C1|
|SM3|LM2|C2|

### `Manager`

`Manager`는 manager가 포함된 회사 조직도 테이블이다.

(열 설명)

- `manager_code`: manager 코드에 해당한다.
- `senior_manager_code`: senior manager 코드에 해당한다.
- `lead_manager_code`: lead manager 코드에 해당한다.
- `company_code`: 회사 코드에 해당한다.

(예시)

|manager_code|senior_manager_code|lead_manager_code|company_code|
|:-:|:-:|:-:|:-:|
|M1|SM1|LM1|C1|
|M2|SM3|LM2|C2|
|M3|SM3|LM2|C2|

### `Employee`

`Employee`는 employee가 포함된 회사 조직도 테이블이다.

(열 설명)

- `employee_code`: employee 코드에 해당한다.
- `manager_code`: manager 코드에 해당한다.
- `senior_manager_code`: senior manager 코드에 해당한다.
- `lead_manager_code`: lead manager 코드에 해당한다.
- `company_code`: 회사 코드에 해당한다.

(예시)

|employee_code|manager_code|senior_manager_code|lead_manager_code|company_code|
|:-:|:-:|:-:|:-:|:-:|
|E1|M1|SM1|LM1|C1|
|E2|M1|SM1|LM1|C1|
|E3|M2|SM3|LM2|C2|
|E4|M3|SM3|LM2|C2|

<br><br><br><br>

## 문제 설명

회사별 설립자 이름, lead manager 수, senior manager 수, manager 수, employee 수를 구하는 문제다.  
단, 각 테이블은 중복된 데이터가 있을 수도 있다. 그리고 `company_code` 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. 회사별 lead manager 수를 구한다.

`Lead_Manager` 테이블에서 `company_code` 기준으로 그룹화하여, 각 그룹에서 lead manager 수를 구한다.  
각 테이블은 중복된 데이터가 있을 수 있기에 `DISTINCT`와 `COUNT`를 이용하여 중복을 제외한 lead manager 수를 구해야 한다.

```sql
SELECT 
    company_code, 
    COUNT(DISTINCT lead_manager_code) AS num_lead 
FROM 
    lead_manager 
GROUP BY 
    company_code
```

(출력)

|company_code|num_lead|
|:-:|:-:|
|C1|1|
|C2|1|

### 2. 회사별 senior manager 수를 구한다.

`Senior_Manager` 테이블에서 `company_code` 기준으로 그룹화하여, 각 그룹에서 senior manager 수를 구한다.  
각 테이블은 중복된 데이터가 있을 수 있기에 `DISTINCT`와 `COUNT`를 이용하여 중복을 제외한 senior manager 수를 구해야 한다.

```sql
SELECT 
    company_code, 
    COUNT(DISTINCT senior_manager_code) AS num_senior 
FROM 
    senior_manager 
GROUP BY 
    company_code
```

(출력)

|company_code|num_senior|
|:-:|:-:|
|C1|2|
|C2|1|

### 3. 회사별 manager 수를 구한다.

`Manager` 테이블에서 `company_code` 기준으로 그룹화하여, 각 그룹에서 manager 수를 구한다.  
각 테이블은 중복된 데이터가 있을 수 있기에 `DISTINCT`와 `COUNT`를 이용하여 중복을 제외한 manager 수를 구해야 한다.

```sql
SELECT 
    company_code, 
    COUNT(DISTINCT manager_code) AS num_manager 
FROM 
    manager 
GROUP BY 
    company_code
```

(출력)

|company_code|num_manager|
|:-:|:-:|
|C1|1|
|C2|2|

### 4. 회사별 employee 수를 구한다.

`Employee` 테이블에서 `company_code` 기준으로 그룹화하여, 각 그룹에서 employee 수를 구한다.  
각 테이블은 중복된 데이터가 있을 수 있기에 `DISTINCT`와 `COUNT`를 이용하여 중복을 제외한 employee 수를 구해야 한다.

```sql
SELECT 
    company_code, 
    COUNT(DISTINCT employee_code) AS num_employee 
FROM 
    employee 
GROUP BY 
    company_code
```

(출력)

|company_code|num_employee|
|:-:|:-:|
|C1|2|
|C2|2|

### 5. `Company`와 위에서 만든 네 개의 테이블을 결합한 후 `company_code`를 기준으로 정렬한다.

테이블 `Company`와 위에서 만든 테이블들을 연속적으로 결합해야 한다. `Company`와 위에서 만든 테이블은 공통적으로 `company_code` 열을 가지고 있기 때문에 `USING (company_code)`가 테이블 결합 조건이다.  
그러고 나서 `company_code`를 기준으로 오름차순 정렬한다.

```sql
SELECT 
    * 
FROM 
    company 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT lead_manager_code) AS num_lead 
        FROM 
            lead_manager 
        GROUP BY 
            company_code
        ) AS sub1 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT senior_manager_code) AS num_senior 
        FROM 
            senior_manager 
        GROUP BY 
            company_code
        ) AS sub2 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT manager_code) AS num_manager 
        FROM 
            manager 
        GROUP BY 
            company_code
            ) AS sub3 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT employee_code) AS num_employee 
        FROM 
            employee 
        GROUP BY 
            company_code
        ) AS sub4 
        USING (company_code) 
ORDER BY 
    company_code
```

<br><br><br><br>

## 풀이

```sql
SELECT 
    * 
FROM 
    company 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT lead_manager_code) AS num_lead 
        FROM 
            lead_manager 
        GROUP BY 
            company_code
        ) AS sub1 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT senior_manager_code) AS num_senior 
        FROM 
            senior_manager 
        GROUP BY 
            company_code
        ) AS sub2 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT manager_code) AS num_manager 
        FROM 
            manager 
        GROUP BY 
            company_code
            ) AS sub3 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT employee_code) AS num_employee 
        FROM 
            employee 
        GROUP BY 
            company_code
        ) AS sub4 
        USING (company_code) 
ORDER BY 
    company_code
```