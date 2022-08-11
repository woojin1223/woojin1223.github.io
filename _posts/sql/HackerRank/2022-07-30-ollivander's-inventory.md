---
title: "[HackerRank] Ollivander's Inventory"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true>

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
    id, 
    age, 
    coins_needed, 
    power 
FROM (
    SELECT 
        age, 
        MIN(coins_needed) AS coins_needed, 
        power 
    FROM (
        SELECT 
            id, 
            age, 
            coins_needed, 
            power 
        FROM 
            wands 
            LEFT JOIN wands_property 
                USING (code) 
        WHERE 
            is_evil = 0
        ) AS x 
    GROUP BY 
        power, age
    ) AS y 
    LEFT JOIN wands_property 
        USING (age) 
    LEFT JOIN wands 
        USING (code, coins_needed, power) 
ORDER BY 
    power DESC, age DESC, coins_needed DESC
```