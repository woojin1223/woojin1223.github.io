---
title: "[LeetCode] Consecutive Numbers"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/consecutive-numbers/>

<br><br><br><br>

## 테이블 설명

<br><br><br><br>

## 문제 설명

<br><br><br><br>

## 사고 과정

<br><br><br><br>

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