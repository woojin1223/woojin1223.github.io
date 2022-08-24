---
title: "[Codility] SqlWorldCup"
categories: SQL
tags: [Codility, PostgreSQL]
---

## 문제 링크

<https://app.codility.com/programmers/trainings/6/sql_world_cup/start/>

<br><br><br><br>

## 테이블 설명

<br><br><br><br>

## 문제 설명

<br><br><br><br>

## 풀이

```sql
SELECT 
    team_id, 
    team_name, 
    COALESCE(num_points, 0) AS num_points 
FROM (
    SELECT 
        host_team, 
        SUM(score) AS num_points 
    FROM (
        SELECT 
            host_team, 
            CASE 
                WHEN host_goals > guest_goals 
                    THEN 3 
                WHEN host_goals = guest_goals 
                    THEN 1 
                ELSE 0
            END AS score 
        FROM (
            SELECT 
                * 
            FROM 
                matches 
            UNION 
            SELECT 
                match_id, 
                guest_team  AS host_team, 
                host_team   AS guest_team, 
                guest_goals AS host_goals, 
                host_goals  AS guest_goals 
            FROM 
                matches
            ) AS x
        ) AS y 
    GROUP BY 
        host_team
    ) AS z 
    RIGHT JOIN teams 
        ON z.host_team = teams.team_id 
ORDER BY 
    num_points DESC, team_id
```