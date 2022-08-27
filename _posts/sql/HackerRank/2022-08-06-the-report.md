---
title: "[HackerRank] The Report"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/the-report/problem>

<br><br><br><br>

## 테이블 설명

### `Students`

`Students`는 학생들의 id, 이름과 점수가 있는 테이블이다.

(열 설명)

- `ID`: 학생의 id에 해당한다.
- `Name`: 학생의 이름에 해당한다.
- `Marks`: 학생의 점수에 해당한다.

(예시)

|ID|Name|Marks|
|:-:|:-:|:-:|
|1|Julia|88|
|2|Samantha|68|
|3|Maria|99|
|4|Scarlet|78|
|5|Ashley|63|
|6|Jane|81|

### `Grades`

`Grades`는 등급의 기준이 있는 테이블이다.

(열 설명)

- `Grade`: 등급에 해당한다.
- `Min_Mark`: 해당 등급을 받기 위한 최소 점수에 해당한다.
- `Max_Mark`: 해당 등급을 받기 위한 최대 점수에 해당한다.

(예시)

|Grade|Min_Mark|Max_Mark|
|:-:|:-:|:-:|
|1|0|9|
|2|10|19|
|3|20|29|
|4|30|39|
|5|40|49|
|6|50|59|
|7|60|69|
|8|70|79|
|9|80|89|
|10|90|100|

<br><br><br><br>

## 문제 설명

학생별 점수에 해당하는 등급을 구하는 문제다.  
단, 아래의 조건을 만족해야 한다.

- 1 ~ 7 등급을 받은 학생의 이름은 `NULL`로 기록한다.
- 복수의 정렬 기준을 만족해야 한다. 
  1. 등급을 기준으로 내림차순 정렬해야 한다.
  2. 등급이 같다면 이름을 기준으로 오름차순 정렬해야 한다.
  3. 이름이 `NULL`이라면 점수를 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. `Students`와 `Grades`를 결합한다.

학생별 점수에 해당하는 등급을 구하려면 테이블 `Students`의 `Marks`가 테이블 `Grades`의 `Min_Mark`와 `Max_Mark` 사이에 있는 행만을 결합한다는 조건으로 두 테이블을 결합해야 한다.  
이는 `BETWEEN ... AND ...` 함수를 이용하여 구할 수 있다.

```sql
SELECT 
    * 
FROM 
    students 
    LEFT JOIN grades 
        ON marks BETWEEN min_mark AND max_mark
```

(출력)

|ID|Name|Marks|Grade|Min_Mark|Max_Mark|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|Julia|88|9|80|89|
|2|Samantha|68|7|60|69|
|3|Maria|99|10|90|100|
|4|Scarlet|78|8|70|79|
|5|Ashley|63|7|60|69|
|6|Jane|81|9|80|89|

### 2. 1 ~ 7 등급을 받은 학생의 이름은 `NULL`로 기록한다.

IF 절을 이용하여 8등급 이상이면 학생의 이름을 그대로 기록하고 8등급 미만인 학생의 이름은 `NULL`로 기록할 수 있다.

```sql
SELECT 
    IF(grade >= 8, name, NULL) AS name, 
    grade, 
    marks 
FROM 
    students 
    LEFT JOIN grades 
        ON marks BETWEEN min_mark AND max_mark
```

(출력)

|Name|Grade|Marks|
|:-:|:-:|:-:|
|Julia|9|88|
|NULL|7|68|
|Maria|10|99|
|Scarlet|8|78|
|NULL|7|63|
|Jane|9|81|

### 3. 복수의 정렬 기준을 적용한다.

`grade`, `name`, `marks` 순으로 정렬하되 `grade`는 내림차순, `name`, `marks`는 오름차순 정렬한다.

```sql
SELECT 
    IF(grade >= 8, name, NULL) AS name, 
    grade, 
    marks 
FROM 
    students 
    LEFT JOIN grades 
        ON marks BETWEEN min_mark AND max_mark 
ORDER BY 
    grade DESC, name, marks
```

<br><br><br><br>

## 풀이

```sql
SELECT 
    IF(grade >= 8, name, NULL) AS name, 
    grade, 
    marks 
FROM 
    students 
    LEFT JOIN grades 
        ON marks BETWEEN min_mark AND max_mark 
ORDER BY 
    grade DESC, name, marks
```