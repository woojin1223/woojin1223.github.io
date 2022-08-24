---
title: "[LeetCode] Rank Scores"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/rank-scores/>

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
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank' 
FROM 
    scores 
ORDER BY 
    score DESC
```