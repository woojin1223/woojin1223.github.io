---
title: "[HackerRank] Challenges"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/challenges/problem>

<br><br><br><br>

## 테이블 설명

### `Hackers`

`Hackers`는 학생의 정보가 있는 테이블이다.

(열 설명)

- `hacker_id`: 학생의 id에 해당한다.
- `name`: 학생의 이름에 해당한다.

(예시)

|hacker_id|name|
|:-:|:-:|
|5077|Rose|
|21283|Angela|
|62743|Frank|
|88255|Patrick|
|96196|Lisa|

### `Challenges`

`Challenges`는 코딩 테스트의 문제에 대한 테이블이다.

(열 설명)

- `challenge_id`: 문제의 id에 해당한다.
- `hacker_id`: 문제를 만든 학생의 id에 해당한다.

(예시)

|challenge_id|hacker_id|
|:-:|:-:|
|61654|5077|
|58302|21283|
|40587|88255|
|29477|5077|
|1220|21283|
|69514|21283|
|46561|62743|
|58077|62743|
|18483|88255|
|76766|21283|
|52382|5077|
|74467|21283|
|33625|96196|
|26053|88255|
|42665|62743|
|12859|62743|
|70094|21283|
|34599|88255|
|54680|88255|
|61881|5077|

<br><br><br><br>

## 문제 설명

학생별 `hacker_id`, `name`, 제작한 문제의 수(`challenges_created`)를 구하는 문제다.  
단, 두 학생 이상이 `challenges_created` 값이 같고 그 값이 `challenges_created`의 최댓값보다 작다면 해당 데이터를 제거한다. 그리고 `challenges_created`를 기준으로 내림차순, `hacker_id`를 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. 학생별 `hacker_id`, `name`, `challenges_created`를 구하고 `challenges_created`, `hacker_id`를 기준으로 정렬한다.

테이블 `Challenges`에는 학생의 이름에 대한 정보가 없기 때문에 테이블 `Hackers`와의 결합을 통해 `Challenges`에 `name` 열을 추가한다. 그리고 `hacker_id`, `name`을 기준으로 그룹화하여 각 그룹별 `challenge_id`의 개수, 즉 `challenges_created`를 구한다. 그러고 나서 `challenges_created`를 기준으로 내림차순, `hacker_id` 기준으로 오름차순 정렬한다.

```sql
SELECT 
    hacker_id, 
    name, 
    COUNT(challenge_id) AS challenges_created 
FROM 
    challenges 
    LEFT JOIN hackers 
        USING (hacker_id) 
GROUP BY 
    hacker_id, name 
ORDER BY 
    challenges_created DESC, hacker_id
```

(출력)

|hacker_id|name|challenges_created|
|:-:|:-:|:-:|
|21283|Angela|6|
|88255|Patrick|5|
|5077|Rose|4|
|62743|Frank|4|
|96196|Lisa|1|

### 2. 1.에서 만든 결과에서 두 학생 이상이 `challenges_created` 값이 같고 그 값이 `challenges_created`의 최댓값보다 작다면 해당 데이터를 제거한다.

데이터를 제거하는 조건은 아래와 같이 다르게 표현할 수 있다.

- `challenges_created`의 최댓값을 가진 데이터 혹은
- 중복되지 않은 `challenges_created` 값을 가진 데이터

1.에서 만든 결과에서 HAVING 절과 서브 쿼리를 이용해서 `challenges_created`의 최댓값을 가진 데이터 혹은 중복되지 않은 `challenges_created` 값을 가진 데이터를 추출할 수 있다.

`challenges_created`의 최댓값을 가진 데이터에 해당하는 서브 쿼리는 다음과 같다.

```sql
SELECT 
    MAX(challenges_created) 
FROM (
    SELECT 
        hacker_id, 
        COUNT(challenge_id) AS challenges_created 
    FROM 
        challenges 
    GROUP BY 
        hacker_id
    ) AS sub1
```

중복되지 않은 `challenges_created` 값을 가진 데이터에 해당하는 서브 쿼리는 다음과 같다.

```sql
SELECT 
    challenges_created 
FROM (
    SELECT 
        hacker_id, 
        COUNT(challenge_id) AS challenges_created 
    FROM 
        challenges 
    GROUP BY 
        hacker_id
    ) AS sub2 
GROUP BY 
    challenges_created 
HAVING 
    COUNT(*) = 1
```

위 두 서브 쿼리와 HAVING 절을 이용해서 1.에서 만든 결과에서 두 학생 이상이 `challenges_created` 값이 같고 그 값이 `challenges_created`의 최댓값보다 작다면 해당 데이터를 제거할 수 있다.

```sql
SELECT 
    hacker_id, 
    name, 
    COUNT(challenge_id) AS challenges_created 
FROM 
    challenges 
    LEFT JOIN hackers 
        USING (hacker_id) 
GROUP BY 
    hacker_id, name 
HAVING 
    challenges_created = (
        SELECT 
            MAX(challenges_created) 
        FROM (
            SELECT 
                hacker_id, 
                COUNT(challenge_id) AS challenges_created 
            FROM 
                challenges 
            GROUP BY 
                hacker_id
            ) AS sub1
    ) OR 
    challenges_created IN (
        SELECT 
            challenges_created 
        FROM (
            SELECT 
                hacker_id, 
                COUNT(challenge_id) AS challenges_created 
            FROM 
                challenges 
            GROUP BY 
                hacker_id
            ) AS sub2 
        GROUP BY 
            challenges_created 
        HAVING 
            COUNT(*) = 1
    ) 
ORDER BY 
    challenges_created DESC, hacker_id
```

<br><br><br><br>

## 풀이

```sql
SELECT 
    hacker_id, 
    name, 
    COUNT(challenge_id) AS challenges_created 
FROM 
    challenges 
    LEFT JOIN hackers 
        USING (hacker_id) 
GROUP BY 
    hacker_id, name 
HAVING 
    challenges_created = (
        SELECT 
            MAX(challenges_created) 
        FROM (
            SELECT 
                hacker_id, 
                COUNT(challenge_id) AS challenges_created 
            FROM 
                challenges 
            GROUP BY 
                hacker_id
            ) AS sub1
    ) OR 
    challenges_created IN (
        SELECT 
            challenges_created 
        FROM (
            SELECT 
                hacker_id, 
                COUNT(challenge_id) AS challenges_created 
            FROM 
                challenges 
            GROUP BY 
                hacker_id
            ) AS sub2 
        GROUP BY 
            challenges_created 
        HAVING 
            COUNT(*) = 1
    ) 
ORDER BY 
    challenges_created DESC, hacker_id
```