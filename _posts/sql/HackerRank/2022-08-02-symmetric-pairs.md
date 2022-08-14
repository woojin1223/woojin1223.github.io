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
    x, y
FROM (
    SELECT 
        LEAST(x, y)    AS x, 
        GREATEST(x, y) AS y 
    FROM 
        functions
    ) AS fns 
GROUP BY 
    x, y 
HAVING 
    COUNT(*) >= 2 
ORDER BY x
```