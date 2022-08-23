---
title: "[HackerRank] Contest Leaderboard"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/contest-leaderboard/problem>

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
    hacker_id, 
    name, 
    total_score 
FROM (
    SELECT 
        hacker_id, 
        SUM(score) AS total_score 
    FROM (
        SELECT 
            hacker_id, 
            MAX(score) AS score 
        FROM 
            submissions 
        GROUP BY 
            hacker_id, challenge_id
        ) AS x
    GROUP BY 
        hacker_id
    ) AS y
    LEFT JOIN hackers 
        USING (hacker_id) 
WHERE 
    total_score > 0 
ORDER BY 
    total_score DESC, hacker_id
```