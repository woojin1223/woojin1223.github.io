---
title: "[HackerRank] The Report"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/the-report/problem>

<br><br><br><br>

## 테이블 설명

<br><br><br><br>

## 문제 설명

<br><br><br><br>

## 사고 과정

<br><br><br><br>

## 풀이

```sql
SELECT 
    CASE WHEN grade >= 8 THEN name ELSE NULL END, 
    grade, 
    marks 
FROM 
    students 
    INNER JOIN grades 
        ON marks BETWEEN min_mark AND max_mark 
ORDER BY 
    grade DESC, name, marks
```