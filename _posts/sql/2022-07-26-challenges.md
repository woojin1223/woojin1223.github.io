---
title: "[HackerRank] Challenges"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    hacker_id, 
    name, 
    cnt AS challenges_created 
FROM (
    SELECT 
        hacker_id, 
        COUNT(DISTINCT challenge_id) AS cnt 
    FROM 
        challenges 
    GROUP BY 
        hacker_id 
    HAVING 
        cnt = (
            SELECT 
                MAX(cnt) 
            FROM (
                SELECT 
                    hacker_id, 
                    COUNT(*) AS cnt 
                FROM 
                    challenges 
                GROUP BY hacker_id
                ) AS x
            ) OR 
        cnt IN (
            SELECT 
                cnt 
            FROM (
                SELECT 
                    hacker_id, 
                    COUNT(DISTINCT challenge_id) AS cnt 
                FROM 
                    challenges 
                GROUP BY 
                    hacker_id
                ) AS y 
            GROUP BY 
                cnt 
            HAVING 
                COUNT(*) = 1
            )
    ) AS z
LEFT JOIN hackers 
    using (hacker_id) 
ORDER BY 
    challenges_created DESC, hacker_id
```