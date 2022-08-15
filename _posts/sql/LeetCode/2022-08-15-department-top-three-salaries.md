---
title: "[LeetCode] Department Top Three Salaries"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/department-top-three-salaries/>

## 풀이

```sql
SELECT 
    Department, 
    Employee, 
    Salary 
FROM (
    SELECT 
        d.name AS 'department', 
        e.name AS 'employee', 
        Salary, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS d_rank 
    FROM 
        employee AS e 
        LEFT JOIN department AS d 
            ON e.departmentId = d.id
    ) AS x
WHERE 
    d_rank <= 3
```