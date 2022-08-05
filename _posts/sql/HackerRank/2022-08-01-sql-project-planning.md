---
title: "[HackerRank] SQL Project Planning"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true>

## 풀이

```sql
 SELECT 
    start_date, 
    MIN(end_date) 
FROM 
    (SELECT start_date FROM projects WHERE start_date NOT IN (SELECT end_date FROM projects)) AS s, 
    (SELECT end_date FROM projects WHERE end_date NOT IN (SELECT start_date FROM projects)) AS e 
WHERE 
    start_date < end_date 
GROUP BY 
    start_date 
ORDER BY 
    DATEDIFF(MIN(end_date), start_date), start_date
```