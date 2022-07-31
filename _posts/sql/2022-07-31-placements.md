---
title: "[HackerRank] Placements"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    name 
FROM (
    SELECT 
        f.id, 
        f.friend_id, 
        p.salary, 
        p2.salary AS friend_salary 
    FROM (
        friends AS f 
        LEFT JOIN packages AS p 
            USING (id) 
        LEFT JOIN packages AS p2 
            ON f.friend_id = p2.id
        ) 
    WHERE 
        p.salary < p2.salary
    ) AS x 
    LEFT JOIN students 
        USING (id) 
ORDER BY 
    friend_salary
```