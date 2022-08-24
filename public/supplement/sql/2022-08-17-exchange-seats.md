---
title: "[LeetCode] Exchange Seats"
categories: SQL
tags: [LeetCode, MySQL]
---

## 문제 링크

<https://leetcode.com/problems/exchange-seats/>

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