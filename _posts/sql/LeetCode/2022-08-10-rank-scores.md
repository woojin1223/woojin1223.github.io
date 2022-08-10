---
title: "[LeetCode] Rank Scores"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/rank-scores/>

## 풀이

```sql
SELECT 
    score, 
    DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank' 
FROM 
    scores 
ORDER BY 
    score DESC
```