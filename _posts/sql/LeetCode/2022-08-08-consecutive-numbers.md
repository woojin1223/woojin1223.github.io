---
title: "[LeetCode] Consecutive Numbers"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/consecutive-numbers/>

## 풀이

```sql
SELECT 
    DISTINCT MIN(num) AS ConsecutiveNums 
FROM (
    SELECT 
        num, 
        ROW_NUMBER() OVER (ORDER BY id)                  AS row_num1, 
        ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS row_num2 
    FROM 
        logs
    ) AS x 
GROUP BY 
    row_num1 - row_num2, num 
HAVING 
    COUNT(*) >= 3
```