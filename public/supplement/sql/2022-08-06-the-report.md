---
title: "[HackerRank] The Report"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/the-report/problem>

<br><br><br><br>

## 테이블 설명

### `Students`

`Students`는 학생들의 id, 이름과 점수가 있는 테이블이다.

(컬럼 설명)

- `id`: 지팡이 id에 해당한다. 지팡이마다 전부 다른 id를 가지고 있다.  
- `code`: 지팡이 종류에 해당한다.  
- `coins_needed`: 지팡이를 사기 위한 돈에 해당한다.  
- `power`: 지팡이의 품질을 수치로 표현한 값이다. 값이 클 수록 좋은 품질을 가진다.

(예시)

|ID|Name|Marks|
|:-:|:-:|:-:|
|1|Julia|88|
|2|Samantha|68|
|3|Maria|99|
|4|Scarlet|78|
|5|Ashley|63|
|6|Jane|81|

<br><br><br><br>

## 문제 설명

<br><br><br><br>

## 사고 과정

<br><br><br><br>

## 풀이

```sql
SELECT 
    CASE WHEN grade >= 8 THEN name ELSE NULL END AS name, 
    grade, 
    marks 
FROM 
    students 
    LEFT JOIN grades 
        ON marks BETWEEN min_mark AND max_mark 
ORDER BY 
    grade DESC, name, marks
```