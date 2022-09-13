---
title: "[HackerRank] Weather Observation Station 20"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/weather-observation-station-20/problem>

<br><br><br><br>

## 테이블 설명

### `STATION`

`STATION`는 기상 관측소의 정보가 있는 테이블이다.

(열 설명)

- `ID`: 행의 id에 해당한다.
- `CITY`: 기상 관측소가 있는 도시에 해당한다.
- `STATE`: 기상 관측소가 있는 주에 해당한다.
- `LAT_N`: 기상 관측소의 위치 정보 중 북위도에 해당한다.
- `LONG_W`: 기상 관측소의 위치 정보 중 서경도에 해당한다.

<br><br><br><br>

## 문제 설명

테이블 `STATION`의 열 `LAT_N`의 중앙값을 구하는 문제다.  
단, 결과는 소수점 아래 넷째 자리까지 반올림한다.

<br><br><br><br>

## 사고 과정

### 1. 테이블 `STATION`의 행의 길이를 구한다.

중앙값을 구하기 위해서는 테이블 행의 길이와 `LAT_N`을 정렬한 후 번호를 매긴 열이 필요하다.  
우선, 테이블 `STATION`의 행의 길이를 구하여 변수 `row_num`에 할당한다.  
이 변수는 `@row_num`을 이용하여 불러 올 수 있다.

```sql
SELECT COUNT(*) FROM station INTO @row_num
```

### 2. 열 `LAT_N`가 증가하는 순서대로 번호를 매긴다.

데이터를 순서대로 정렬했을 때 중간 위치에 있는 값이 곧 중앙값이므로 데이터를 순서대로 정렬한 후 번호를 매길 필요가 있다.  
따라서, 열 `LAT_N`가 증가하는 순서대로 번호를 매긴 값을 열 `num`에 저장한다.

```sql
SELECT 
    lat_n, 
    ROW_NUMBER() OVER (ORDER BY lat_n) AS num 
FROM 
    station
```

### 3. 위에서 구한 행의 길이와 행 번호로 열 `LAT_N`의 중앙값을 구한다.

행의 길이와 행 번호로 중앙값을 구하는 방법은 다음과 같다.  
길이가 n인 데이터를 순서대로 나열했을 때, 중앙값은 ⌊(n+1)/2⌋  번째 수와 ⌈(n+1)/2⌉ 번째 수의 평균값이다.  
예를 들어, 

- 데이터가 [1, 2, 3](즉, n = 3)인 경우, 중앙값은 2 번째 수인 2다.
- 데이터가 [1, 2, 3, 4](즉, n = 4)인 경우, 중앙값은 2 번째 수와 3 번째 수의 평균인 2.5다.

위에서 설명한 중앙값을 구하는 방법을 코드로 구현하면 다음과 같다.  

```sql
SELECT COUNT(*) FROM station INTO @row_num;

SELECT 
    ROUND(AVG(lat_n), 4) AS median 
FROM (
    SELECT 
        lat_n, 
        ROW_NUMBER() OVER (ORDER BY lat_n) AS num 
    FROM 
        station
    ) AS sub 
WHERE 
    num IN (FLOOR((@row_num+1) / 2), CEIL((@row_num+1) / 2))
```

참고: MySQL에서는 `FLOOR` 함수, `CEIL` 함수를 이용하여 내림과 올림을 구현할 수 있다.

<br><br><br><br>

## 풀이

```sql
SELECT COUNT(*) FROM station INTO @row_num;

SELECT 
    ROUND(AVG(lat_n), 4) AS median 
FROM (
    SELECT 
        lat_n, 
        ROW_NUMBER() OVER (ORDER BY lat_n) AS num 
    FROM 
        station
    ) AS sub 
WHERE 
    num IN (FLOOR((@row_num+1) / 2), CEIL((@row_num+1) / 2))
```