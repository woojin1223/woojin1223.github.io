---
title: "[HackerRank] Symmetric Pairs"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    * 
FROM (
    SELECT 
        x, y 
    FROM 
        functions 
    GROUP BY 
        x, y 
    HAVING 
        x = y AND 
        COUNT(*) = 2
    ) AS fn3 
UNION 
SELECT 
    * 
FROM (
    SELECT 
        fn1.x, 
        fn1.y 
    FROM 
        functions AS fn1 
        INNER JOIN functions AS fn2 
            ON (fn1.x, fn1.y) = (fn2.y, fn2.x) AND 
            (fn1.x, fn1.y) != (fn2.x, fn2.y)
    GROUP BY 
        x, y
    ) AS fn4 
WHERE 
    x <= y 
ORDER BY 
    x
```