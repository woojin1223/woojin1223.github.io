---
title: "[LeetCode] Exchange Seats"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/exchange-seats/>

## 풀이

```sql
SELECT 
    ROW_NUMBER() OVER (ORDER BY id) AS id, 
    student 
FROM (
    SELECT 
        IF(id % 2 = 0, id - 1, id + 1) AS id, 
        student 
    FROM 
        seat 
    ORDER BY 
        id
    ) AS x
```