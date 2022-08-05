---
title: "[HackerRank] Interviews"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true>

## 풀이

```sql
SELECT 
    contest_id, 
    hacker_id, 
    name, 
    total_submissions, 
    total_accepted_submissions, 
    total_views, 
    total_unique_views 
FROM (
    SELECT 
        contest_id, 
        SUM(total_submissions)          AS total_submissions, 
        SUM(total_accepted_submissions) AS total_accepted_submissions 
    FROM 
        contests 
        LEFT JOIN colleges 
            USING (contest_id) 
        LEFT JOIN challenges 
            USING (college_id) 
        LEFT JOIN submission_stats 
            USING (challenge_id) 
    GROUP BY 
        contest_id
    ) AS x 
    INNER JOIN (
        SELECT 
        contest_id, 
        SUM(total_views)        AS total_views, 
        SUM(total_unique_views) AS total_unique_views 
    FROM 
        contests  
        LEFT JOIN colleges 
            USING (contest_id) 
        LEFT JOIN challenges 
            USING (college_id) 
        LEFT JOIN view_stats 
            USING (challenge_id) 
    GROUP BY 
        contest_id
        ) AS y
        USING (contest_id) 
    LEFT JOIN contests 
        USING (contest_id) 
WHERE 
    COALESCE(total_submissions, total_accepted_submissions, total_views, total_unique_views) IS NOT NULL 
ORDER BY 
    contest_id
```