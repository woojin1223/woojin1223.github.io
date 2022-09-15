---
title: "[HackerRank] Interviews"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/interviews/problem>

<br><br><br><br>

## 테이블 설명

### `Contests`

`Contests`는 코딩 테스트 대회에 관한 테이블이다.

(열 설명)

- `contest_id`: 대회 id에 해당한다.
- `hacker_id`: 대회를 만든 해커 id에 해당한다.
- `name`: 대회를 만든 해커 이름에 해당한다.

(예시)

|contest_id|hacker_id|name|
|:-:|:-:|:-:|
|66406|17973|Rose|
|66556|79153|Angela|
|94828|80275|Frank|

### `Colleges`

`Colleges`는 코딩 테스트 대회를 개최한 대학에 대한 테이블이다.  
단, `college_id`와 `contest_id`는 다대일로 매칭된다.

(열 설명)

- `college_id`: 대회를 개최한 대학 id에 해당한다.
- `contest_id`: 대회 id에 해당한다.

(예시)

|college_id|contest_id|
|:-:|:-:|
|11219|66406|
|32473|66556|
|56685|94828|

### `Challenges`

`Challenges`는 코딩 테스트 대회를 개최한 대학이 출제한 문제에 대한 테이블이다.  
단, `challenge_id`와 `college_id`는 다대일로 매칭된다.

(열 설명)

- `challenge_id`: 문제 id에 해당한다.
- `college_id`: 대학 id에 해당한다.

(예시)

|challenge_id|college_id|
|:-:|:-:|
|18765|11219|
|47127|11219|
|60292|32473|
|72974|56685|

### `View_Stats`

`View_Stats`는 코딩 테스트 문제를 열람한 통계에 대한 테이블이다.

(열 설명)

- `challenge_id`: 문제 id에 해당한다.
- `total_views`: 지원자들이 해당 문제를 열람한 총 횟수에 해당한다.
- `total_unique_views`: 중복을 제외한 지원자들이 해당 문제를 열람한 총 횟수에 해당한다.

(예시)

|challenge_id|total_views|total_unique_views|
|:-:|:-:|:-:|
|47127|26|19|
|47127|15|14|
|18765|43|10|
|18765|72|13|
|75516|35|17|
|60292|11|10|
|72974|41|15|
|75516|75|11|

### `Submission_Stats`

`Submission_Stats`는 코딩 테스트 문제를 제출한 통계에 대한 테이블이다.

(열 설명)

- `challenge_id`: 문제 id에 해당한다.
- `total_submissions`: 지원자들이 해당 문제를 제출한 총 횟수에 해당한다.
- `total_accepted_submissions`: 해당 문제를 제출하여 만점을 받은 지원자 수에 해당한다.

(예시)

|challenge_id|total_submissions|total_accepted_submissions|
|:-:|:-:|:-:|
|75516|34|12|
|47127|27|10|
|47127|56|18|
|75516|74|12|
|75516|83|8|
|72974|68|24|
|72974|82|14|
|47127|28|11|

<br><br><br><br>

## 문제 설명

대회별로 `contest_id`, `hacker_id`, `name`, `total_submissions`의 합, `total_accepted_submissions`의 합, `total_view`의 합, `total_unique_views`의 합을 구하는 문제다.  
단, `contest_id` 열을 기준으로 정렬하고 위 네 개의 합이 모두 0인 데이터를 제외해야 한다.

<br><br><br><br>

## 사고 과정

### 1. 테이블 `Colleges`, `Challenges`, `Submission_Stats`를 결합하여 대회별로 `total_submissions`의 합, `total_accepted_submissions`의 합을 구한다.

하나의 `contest_id`에 여러 개의 `college_id`가 매칭될 수 있고, 하나의 `college_id`에 여러 개의 `challenge_id`가 매칭될 수 있으므로 테이블 `Colleges`, `Challenges`, `Submission_Stats` 순으로 `LEFT JOIN`을 이용하여 결합한다.  
그러고 나서 `GROUP BY contest_id`를 이용하여 대회별로 `total_submissions`의 합, `total_accepted_submissions`의 합을 구한다.

(SQL 코드)

```sql
SELECT 
    contest_id, 
    SUM(total_submissions)          AS total_submissions, 
    SUM(total_accepted_submissions) AS total_accepted_submissions 
FROM 
    colleges 
    LEFT JOIN challenges 
        USING (college_id) 
    LEFT JOIN submission_stats 
        USING (challenge_id) 
GROUP BY 
    contest_id
```

(실행 결과)

|contest_id|total_submissions|total_accepted_submissions|
|:-:|:-:|:-:|
|66406|111|39|
|66556|NULL|NULL|
|94828|150|38|

### 2. 테이블 `Colleges`, `Challenges`, `View_Stats`를 결합하여 대회별로 `total_views`의 합, `total_unique_views`의 합을 구한다.

1.에서의 과정과 동일하게 테이블 `Colleges`, `Challenges`, `View_Stats` 순으로 `LEFT JOIN`을 이용하여 결합한다.  
그러고 나서 `GROUP BY contest_id`를 이용하여 대회별로 `total_views`의 합, `total_unique_views`의 합을 구한다.

(SQL 코드)

```sql
SELECT 
    contest_id, 
    SUM(total_views)        AS total_views, 
    SUM(total_unique_views) AS total_unique_views 
FROM 
    colleges 
    LEFT JOIN challenges 
        USING (college_id) 
    LEFT JOIN view_stats 
        USING (challenge_id) 
GROUP BY 
    contest_id
```

(실행 결과)

|contest_id|total_views|total_unique_views|
|:-:|:-:|:-:|
|66406|156|56|
|66556|11|10|
|94828|41|15|

### 3. 1.과 2.에서 만든 두 테이블과 테이블 `Contests` 을 결합한다.

테이블 `Contests`에 각 `contest_id`에 대응하는 `hacker_id`, `name`이 있기 때문에 1.과 2.에서 만든 두 테이블을 `INNER JOIN`으로 결합한 후 `Contests` 테이블과 결합해야 한다.

(SQL 코드)

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
        colleges 
        LEFT JOIN challenges 
            USING (college_id) 
        LEFT JOIN submission_stats 
            USING (challenge_id) 
    GROUP BY 
        contest_id
    ) AS sub1 
    INNER JOIN (
        SELECT 
            contest_id, 
            SUM(total_views)        AS total_views, 
            SUM(total_unique_views) AS total_unique_views 
        FROM 
            colleges 
            LEFT JOIN challenges 
                USING (college_id) 
            LEFT JOIN view_stats 
                USING (challenge_id) 
        GROUP BY 
            contest_id
        ) AS sub2 
        USING (contest_id) 
    LEFT JOIN contests 
        USING (contest_id)
```

(실행 결과)

|contest_id|hacker_id|name|total_submissions|total_accepted_submissions|total_views|total_unique_views|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|66406|17973|Rose|111|39|156|56|
|66556|79153|Angela|NULL|NULL|11|10|
|94828|80275|Frank|150|38|41|15|

### 4. 네 개의 합이 모두 0인 데이터를 제외하고, `contest_id` 열을 기준으로 정렬한다.

1.과 2.에서 구한 `total_submissions`의 합, `total_accepted_submissions`의 합, `total_view`의 합, `total_unique_views`의 합이 0인 경우는 곧 NULL인 경우와 같다.  
따라서, `COALESCE` 함수를 이용하여 네 개의 합이 모두 0인 데이터를 제외할 수 있다.  
참고: `COALESCE(a, b, c, d)`: a가 NULL인 경우 b를 반환, b가 NULL인 경우 c를 반환, c가 NULL인 경우 d를 반환, d가 NULL인 경우 NULL을 반환

(SQL 코드)

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
        colleges 
        LEFT JOIN challenges 
            USING (college_id) 
        LEFT JOIN submission_stats 
            USING (challenge_id) 
    GROUP BY 
        contest_id
    ) AS sub1 
    INNER JOIN (
        SELECT 
            contest_id, 
            SUM(total_views)        AS total_views, 
            SUM(total_unique_views) AS total_unique_views 
        FROM 
            colleges 
            LEFT JOIN challenges 
                USING (college_id) 
            LEFT JOIN view_stats 
                USING (challenge_id) 
        GROUP BY 
            contest_id
        ) AS sub2 
        USING (contest_id) 
    LEFT JOIN contests 
        USING (contest_id) 
WHERE 
    COALESCE(total_submissions, total_accepted_submissions, total_views, total_unique_views) IS NOT NULL 
ORDER BY 
    contest_id
```

(실행 결과)

|contest_id|hacker_id|name|total_submissions|total_accepted_submissions|total_views|total_unique_views|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|66406|17973|Rose|111|39|156|56|
|66556|79153|Angela|NULL|NULL|11|10|
|94828|80275|Frank|150|38|41|15|

<br><br><br><br>

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
        colleges 
        LEFT JOIN challenges 
            USING (college_id) 
        LEFT JOIN submission_stats 
            USING (challenge_id) 
    GROUP BY 
        contest_id
    ) AS sub1 
    INNER JOIN (
        SELECT 
            contest_id, 
            SUM(total_views)        AS total_views, 
            SUM(total_unique_views) AS total_unique_views 
        FROM 
            colleges 
            LEFT JOIN challenges 
                USING (college_id) 
            LEFT JOIN view_stats 
                USING (challenge_id) 
        GROUP BY 
            contest_id
        ) AS sub2 
        USING (contest_id) 
    LEFT JOIN contests 
        USING (contest_id) 
WHERE 
    COALESCE(total_submissions, total_accepted_submissions, total_views, total_unique_views) IS NOT NULL 
ORDER BY 
    contest_id
```