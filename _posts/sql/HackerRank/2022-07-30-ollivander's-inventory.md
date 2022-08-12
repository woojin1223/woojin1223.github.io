---
title: "[HackerRank] Ollivander's Inventory"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true>

<br><br><br><br>

## 테이블 설명

`WANDS`는 Ollivander의 물품 목록에 해당하는 테이블이다.  
`id`는 지팡이 id에 해당한다. 지팡이마다 전부 다른 id를 가지고 있다.  
`code`는 지팡이 종류에 해당한다.  
`coins_needed`는 지팡이를 사기 위한 돈에 해당한다.  
`power`는 지팡이의 품질을 수치로 표현한 값이다. 값이 클 수록 좋은 품질을 가진다.

|id|code|coins_needed|power|
|:-:|:-:|:-:|:-:|
|1|4|3688|8|
|2|3|9365|3|
|3|3|7187|10|
|4|3|734|8|
|5|1|6020|2|
|6|2|6773|7|
|7|3|9873|9|
|8|3|7721|7|
|9|1|1647|10|
|10|4|504|5|
|11|2|7587|5|
|12|5|9897|10|
|13|3|4651|8|
|14|2|5408|1|
|15|2|6018|7|
|16|4|7710|5|
|17|2|8798|7|
|18|2|3312|3|
|19|4|7651|6|
|20|5|5689|3|

`WANDS_PROPERTY`는 지팡이 종류별 특징이 있는 테이블이다.  
`code`는 지팡이 종류에 해당한다.  
`age`는 지팡이 나이에 해당한다.  
`is_evil`은 흑마법에 관련이 있는지를 0과 1로 나타내는 변수로, 0은 non-evil을 의미한다.

|code|age|is_evil|
|:-:|:-:|:-:|
|1|45|0|
|2|40|0|
|3|4|1|
|4|20|0|
|5|17|0|

<br><br><br><br>

## 문제 설명

`age`와 `power`를 기준으로 지팡이를 그룹화한 후, 각 그룹에서 **non-evil**이고 **구매 가격이 가장 싼** 지팡이의 정보(`id`, `age`, `coins_needed`, `power`)를 구하는 문제다.

<br><br><br><br>

## 사고 과정

### 1. `WANDS`와 `WANDS_PROPERTY`를 `code`를 공통 키로 결합한다.

```sql
SELECT 
    * 
FROM 
    wands 
    LEFT JOIN wands_property 
      USING (code)
```

### 2. non-evil 지팡이만 추출한다.

```sql
SELECT 
    * 
FROM 
    wands 
    LEFT JOIN wands_property 
      USING (code)
WHERE 
    is_evil = 0
```

### 3. `code`, `age`, `power`를 기준으로 그룹화하여 가장 싼 구매 가격을 구한다.

`age`, `power`를 기준으로 그룹화하여 각 그룹에서 non-evil이고 구매 가격이 가장 싼 지팡이의 정보를 구해야 한다.  
`code`를 추가로 넣어서 그룹화하는 이유는 지팡이의 정보 중 `id`를 알기 위해서는 `code`, `coins_needed`, `power`의 값이 필요하기 때문이다.  
그리고 `code`와 `age`는 1대1 매핑되어 있기 때문에, `age`, `power`를 기준으로 그룹화한 것과 `code`, `age`, `power`를 기준으로 그룹화한 것의 결과는 같다.  

```sql
SELECT 
    code, 
    age, 
    MIN(coins_needed) AS coins_needed, 
    power 
FROM 
    wands 
    LEFT JOIN wands_property 
      USING (code)
WHERE 
    is_evil = 0
GROUP BY 
    code, age, power
```

### 4. 지팡이의 `id`를 구하기 위해 3.에서 구한 테이블과 `WANDS`를 `code`, `coins_needed`, `power`를 공통 키로 결합한다.

```sql
SELECT 
    id, 
    age, 
    coins_needed, 
    power 
FROM (
    SELECT 
        code, 
        age, 
        MIN(coins_needed) AS coins_needed, 
        power 
    FROM 
        wands 
        LEFT JOIN wands_property 
            USING (code) 
    WHERE 
        is_evil = 0 
    GROUP BY 
        code, age, power
    ) AS x 
    LEFT JOIN wands 
        USING (code, coins_needed, power)
```

### 5. `power` 값과 `age` 값을 기준으로 내림차순 정렬한다.

```sql
SELECT 
    id, 
    age, 
    coins_needed, 
    power 
FROM (
    SELECT 
        code, 
        age, 
        MIN(coins_needed) AS coins_needed, 
        power 
    FROM 
        wands 
        LEFT JOIN wands_property 
            USING (code) 
    WHERE 
        is_evil = 0 
    GROUP BY 
        code, age, power
    ) AS x 
    LEFT JOIN wands 
        USING (code, coins_needed, power) 
ORDER BY 
    power DESC, age DESC
```

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
        code, 
        age, 
        MIN(coins_needed) AS coins_needed, 
        power 
    FROM 
        wands 
        LEFT JOIN wands_property 
            USING (code) 
    WHERE 
        is_evil = 0 
    GROUP BY 
        code, age, power
    ) AS x 
    LEFT JOIN wands 
        USING (code, coins_needed, power) 
ORDER BY 
    power DESC, age DESC
```