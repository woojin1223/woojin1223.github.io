---
title: "[HackerRank] Binary Tree Nodes"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true>

## 문제 설명

![binary_tree_nodes](https://s3.amazonaws.com/hr-challenge-images/12888/1443773633-f9e6fd314e-simply_sql_bst.png)
*문제에서 주어진 이진트리 구조*

<figure>
    <img src='https://s3.amazonaws.com/hr-challenge-images/12888/1443773633-f9e6fd314e-simply_sql_bst.png'>    
    <figcaption>문제에서 주어진 이진트리 구조</figcaption>
</figure>

## 풀이

```sql
SELECT 
    n, 
    'Root' AS node_type 
FROM 
    bst 
WHERE 
    P IS NULL 
UNION 
SELECT 
    n, 
    'Leaf' AS node_type 
FROM 
    bst 
WHERE 
    n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL) 
UNION 
SELECT 
    DISTINCT p AS n, 
    'Inner'    AS node_type 
FROM 
    bst 
WHERE 
    p IS NOT NULL AND 
    p != (SELECT n FROM bst WHERE P IS NULL) 
ORDER BY 
    n
```