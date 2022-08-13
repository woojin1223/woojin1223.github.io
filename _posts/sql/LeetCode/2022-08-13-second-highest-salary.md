---
title: "[LeetCode] Second Highest Salary"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/second-highest-salary/>

## 풀이 1

```sql
SELECT 
    IFNULL((SELECT 
               DISTINCT salary
           FROM 
               employee 
           ORDER BY 
               salary DESC 
           LIMIT 1, 1), NULL) AS SecondHighestSalary
```

## 풀이 2

```sql
SELECT 
    CASE WHEN COUNT(*) >= 1 THEN salary ELSE NULL END AS SecondHighestSalary 
FROM (
    SELECT 
        salary 
    FROM (
        SELECT 
            salary, 
            DENSE_RANK() OVER(ORDER BY salary DESC) AS row_num 
        FROM 
            employee
        ) AS x
    WHERE 
        row_num = 2
    ) AS y
```