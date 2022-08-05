---
title: "[HackerRank] Top Competitors"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    hacker_id, 
    name 
FROM (
    SELECT 
        hacker_id, 
        COUNT(DISTINCT challenge_id) AS cnt 
    FROM (
        SELECT 
            s.hacker_id, 
            s.challenge_id, 
            s.score AS s_score, 
            d.score AS d_score 
        FROM 
            submissions AS s 
            LEFT JOIN challenges 
                USING (challenge_id) 
            LEFT JOIN difficulty AS d 
                USING (difficulty_level) 
        WHERE 
            s.score = d.score
        ) AS x 
    GROUP BY 
        hacker_id
    ) AS y 
    LEFT JOIN hackers 
        USING (hacker_id) 
WHERE 
    cnt > 1 
ORDER BY 
    cnt DESC, hacker_id
```