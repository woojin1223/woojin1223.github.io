---
title: "[HackerRank] Binary Tree Nodes"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    n, 
    'Root' AS name 
FROM 
    bst 
WHERE 
    P IS NULL 
UNION 
SELECT 
    n, 
    'Leaf' AS name 
FROM 
    bst 
WHERE 
    n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL) 
UNION 
SELECT 
    DISTINCT p AS n, 
    'Inner'    AS name 
FROM 
    bst 
WHERE 
    p IS NOT NULL AND 
    p != (SELECT n FROM bst WHERE P IS NULL) 
ORDER BY 
    n
```