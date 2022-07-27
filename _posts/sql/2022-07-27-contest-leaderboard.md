---
title: "[HackerRank] Contest Leaderboard"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true>

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
        using (hacker_id) 
WHERE 
    total_score > 0 
ORDER BY 
    total_score DESC, hacker_id
```