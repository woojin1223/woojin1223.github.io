---
title: "[HackerRank] The Report"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    CASE WHEN grade >= 8 THEN name ELSE NULL END, 
    grade, 
    marks 
FROM 
    students 
    INNER JOIN grades 
        ON marks BETWEEN min_mark AND max_mark 
ORDER BY 
    grade DESC, name, marks
```