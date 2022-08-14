---
title: "[HackerRank] Symmetric Pairs"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/symmetric-pairse/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    CAST(SUBSTRING_INDEX(tuple, ',', 1) AS SIGNED) AS x, 
    CAST(SUBSTRING_INDEX(tuple, ',', -1) AS SIGNED) AS y 
FROM (
    SELECT 
        CASE 
            WHEN x > y 
                THEN CONCAT_WS(',', y, x) 
            ELSE CONCAT_WS(',', x, y) 
        END AS tuple 
    FROM 
        functions
    ) AS x 
GROUP BY 
    tuple 
HAVING 
    COUNT(*) >= 2 
ORDER BY 
    x
```