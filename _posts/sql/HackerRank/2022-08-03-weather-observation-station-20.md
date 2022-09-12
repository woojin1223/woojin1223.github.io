---
title: "[HackerRank] Weather Observation Station 20"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/weather-observation-station-20/problem>

<br><br><br><br>

## 테이블 설명

<br><br><br><br>

## 문제 설명

<br><br><br><br>

## 사고 과정

<br><br><br><br>

## 풀이

```sql
SELECT COUNT(*) FROM station INTO @row_num;

SELECT 
    ROUND(AVG(lat_n), 4) AS median 
FROM (
    SELECT 
        lat_n, 
        ROW_NUMBER() OVER (ORDER BY lat_n) AS num 
    FROM 
        station
    ) AS sub 
WHERE 
    num IN (FLOOR((@row_num+1) / 2), CEIL((@row_num+1) / 2))
```