---
title: "[HackerRank] Weather Observation Station 19"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    ROUND(SQRT(POWER(a - c, 2) + POWER(b - d, 2)), 4) 
FROM (
    SELECT 
        MIN(lat_n)  AS a, 
        MIN(long_w) AS b, 
        MAX(lat_n)  AS c, 
        MAX(long_w) AS d 
    FROM 
        station
    ) AS x
```