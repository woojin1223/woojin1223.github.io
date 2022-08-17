---
title: "[HackerRank] Binary Tree Nodes"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/binary-search-tree-1/problem>

<br><br><br><br>

## 테이블 설명

이진트리는 각각의 노드의 자식이 최대 두 개인 트리 자료 구조이다.  
`BST`는 (자식 노드, 부모 노드) 형태의 행을 가지는 2열로 구성된 테이블이다.  
테이블 `BST`의 예시는 다음과 같다.

|n|p|
|:-:|:-:|
|1|2|
|3|2|
|6|8|
|9|8|
|2|5|
|8|5|
|5|null|

여기서 n은 자식 노드, p는 부모 노드에 해당한다.

<br><br><br><br>

## 문제 설명

위의 테이블 `BST`를 이진트리 그림으로 나타내면 아래와 같다.

![binary_tree_nodes](https://s3.amazonaws.com/hr-challenge-images/12888/1443773633-f9e6fd314e-simply_sql_bst.png)

위와 같은 이진트리 구조에서 Root node, Leaf node, Inner node를 찾는 문제다.  

- Root node: 부모 노드가 없는 노드를 말하며, 그림에서는 5번 노드가 이에 해당한다.  
- Leaf node: 자식 노드가 없는 노드를 말하며, 그림에서는 1번, 3번, 6번, 9번 노드가 이에 해당한다.  
- Inner node: Root node와 Leaf node가 아닌 노드를 말하며, 그림에서는 2번, 8번 노드가 이에 해당한다.

단, 노드 값을 기준으로 오름차순 정렬해야 한다.

<br><br><br><br>

## 사고 과정

### 1. Root node에 해당하는 테이블을 구한다.

Root node는 부모 노드가 없는 노드다.  
즉, `WHERE p IS NULL`을 이용하여 Root node를 구할 수 있다.

```sql
SELECT 
    n, 
    'Root' AS node_type 
FROM 
    bst 
WHERE 
    p IS NULL
```

(출력)

|n|node_type|
|:-:|:-:|
|5|Root|

### 2. Inner node에 해당하는 테이블을 구한다.

Inner node는 부모 노드 집합 중에서 Root node가 아닌 노드다.  
1.의 쿼리 결과를 임시 테이블 `root_node`에 저장했다고 가정하자.  
부모 노드 집합을 구하는 쿼리 `SELECT DISTINCT p FROM bst WHERE p IS NOT NULL`에서 Root node가 아닌 노드를 구하는 WHERE 절 `WHERE p != (SELECT n FROM root_node)`을 추가하여 Inner node를 구할 수 있다.

```sql
SELECT 
    DISTINCT p AS n, 
    'Inner'    AS node_type 
FROM 
    bst 
WHERE 
    p IS NOT NULL AND 
    p != (SELECT n FROM root_node)
```

(출력)

|n|node_type|
|:-:|:-:|
|2|Inner|
|8|Inner|

### 3. Leaf node에 해당하는 테이블을 구한다.

Leaf node는 Root node와 Inner node가 아닌 노드다.  
1.의 쿼리 결과를 임시 테이블 `root_node`, 2.의 쿼리 결과를 임시 테이블 `inner_node`에 저장했다고 가정하자.  
Root node와 Inner node가 아닌 노드를 구하는 WHERE 절 `WHERE n NOT IN (SELECT n FROM root_node UNION SELECT n FROM inner_node)`을 추가하여 Leaf node를 구할 수 있다.

```sql
SELECT 
    n, 
    'Leaf' AS node_type 
FROM 
    bst 
WHERE 
    n NOT IN (SELECT n FROM root_node UNION SELECT n FROM inner_node)
```

(출력)

|n|node_type|
|:-:|:-:|
|1|Leaf|
|3|Leaf|
|6|Leaf|
|9|Leaf|

### 4. 위 세 개의 테이블을 `UNION`을 이용하여 세로 방향으로 결합한다.

WITH 절을 이용하여 1.에서 구한 Root node를 임시 테이블 `root_node`에 저장하고 2.에서 구한 Inner node는 임시 테이블 `inner_node`에 저장하고 3.에서 구한 Leaf node를 임시 테이블 `leaf_node`에 저장하자.

```sql
WITH root_node AS (
    SELECT 
        n, 
        'Root' AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NULL
), inner_node AS (
    SELECT 
        DISTINCT p AS n, 
        'Inner'    AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NOT NULL AND 
        p != (SELECT n FROM root_node)
), leaf_node AS (
    SELECT 
        n, 
        'Leaf' AS node_type 
    FROM 
        bst 
    WHERE 
        n NOT IN (SELECT n FROM root_node UNION SELECT n FROM inner_node)
)
```

그 후에 `UNION`을 이용하여 세 개의 임시 테이블 `root_node`, `inner_node`, `leaf_node`을 세로 방향으로 결합한다.

```sql
SELECT * FROM root_node 
UNION 
SELECT * FROM inner_node 
UNION 
SELECT * FROM leaf_node
```

### 5. 마지막으로, Node 값을 기준으로 오름차순 정렬한다.

```sql
SELECT * FROM root_node 
UNION 
SELECT * FROM inner_node 
UNION 
SELECT * FROM leaf_node 
ORDER BY n
```

(출력)

|n|node_type|
|:-:|:-:|
|1|Leaf|
|2|Inner|
|3|Leaf|
|5|Root|
|6|Leaf|
|8|Inner|
|9|Leaf|

<br><br><br><br>

## 풀이

```sql
-- WITH 절로 임시 테이블 root_node, inner_node, leaf_node 생성
WITH root_node AS (
    SELECT 
        n, 
        'Root' AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NULL
), inner_node AS (
    SELECT 
        DISTINCT p AS n, 
        'Inner'    AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NOT NULL AND 
        p != (SELECT n FROM root_node)
), leaf_node AS (
    SELECT 
        n, 
        'Leaf' AS node_type 
    FROM 
        bst 
    WHERE 
        n NOT IN (SELECT n FROM root_node UNION SELECT n FROM inner_node)
)

-- UNION으로 root_node, inner_node, leaf_node 결합 후 정렬
SELECT * FROM root_node 
UNION 
SELECT * FROM inner_node 
UNION 
SELECT * FROM leaf_node 
ORDER BY n
```