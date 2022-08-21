---
title: "[HackerRank] Top Competitors"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/full-score/problem>

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
    h.hacker_id, 
    h.name 
FROM 
    submissions AS s 
    LEFT JOIN challenges 
        USING (challenge_id) 
    LEFT JOIN difficulty AS d 
        USING (difficulty_level) 
    LEFT JOIN hackers AS h 
        ON s.hacker_id = h.hacker_id 
WHERE 
    s.score = d.score 
GROUP BY 
    h.hacker_id, h.name 
HAVING 
    COUNT(*) > 1 
ORDER BY 
    COUNT(*) DESC, h.hacker_id
```