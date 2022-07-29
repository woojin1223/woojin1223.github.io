---
title: "[HackerRank] New Companies"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    * 
FROM 
    company 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT lead_manager_code) AS num_lead 
        FROM 
            lead_manager 
        GROUP BY 
            company_code
        ) AS a 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT senior_manager_code) AS num_senior 
        FROM 
            senior_manager 
        GROUP BY 
            company_code
        ) AS b 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT manager_code) AS num_manager 
        FROM 
            manager 
        GROUP BY 
            company_code
            ) AS c 
        USING (company_code) 
    LEFT JOIN (
        SELECT 
            company_code, 
            COUNT(DISTINCT employee_code) AS num_employee 
        FROM 
            employee 
        GROUP BY 
            company_code
        ) AS d 
        USING (company_code) 
ORDER BY 
    company_code
```