---
title: "[Codility] SqlEventsDelta"
categories: SQL
tags: [Codility, PostgreSQL]
---

## 문제 링크

<https://app.codility.com/programmers/trainings/6/sql_events_delta/start/>

<br><br><br><br>

## 테이블 설명

<br><br><br><br>

## 문제 설명

<br><br><br><br>

## 사고 과정

<br><br><br><br>

## 풀이 1

```sql
SELECT 
    event_type, 
    SUM(CASE WHEN row_num = 1 THEN value ELSE 0 END) - SUM(CASE WHEN row_num = 2 THEN value ELSE 0 END) 
FROM (
    SELECT 
        event_type, 
        value, 
        row_num 
    FROM (
        SELECT 
            *, 
            ROW_NUMBER() OVER (PARTITION BY event_type ORDER BY time DESC) AS row_num 
        FROM 
            events
        ) AS x 
    WHERE 
        row_num <= 2
    ) AS y 
GROUP BY 
    event_type 
HAVING 
    COUNT(*) = 2 
ORDER BY 
    event_type
```

## 풀이 2
```sql
SELECT 
    * 
FROM (
    SELECT 
        event_type, 
        value - LEAD(value) OVER (PARTITION BY event_type ORDER BY event_type) AS value 
    FROM (
        SELECT 
            *, 
            ROW_NUMBER() OVER (PARTITION BY event_type ORDER BY time DESC) AS row_num 
        FROM 
            events
        ) AS x
    WHERE 
        row_num <= 2
    ) AS y 
WHERE 
    value IS NOT NULL
```