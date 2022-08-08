---
title: "[HackerRank] Binary Tree Nodes"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true>

## 테이블 설명

이진트리는 각각의 노드의 자식이 최대 두 개인 트리 자료 구조이다.  
`BST`는 (자식 노드, 부모 노드) 형태의 행을 가지는 2열로 구성된 테이블이다.  
테이블 `BST`의 예시는 다음과 같다.

|N|P|
|-|-|
|1|2|
|3|2|
|6|8|
|9|8|
|2|5|
|8|5|
|5|null|

여기서 N은 자식 노드, P는 부모 노드에 해당한다.

## 문제 설명

위의 테이블을 이진트리 그림으로 나타내면 아래와 같다.
![binary_tree_nodes](https://s3.amazonaws.com/hr-challenge-images/12888/1443773633-f9e6fd314e-simply_sql_bst.png)

위와 같은 이진트리 구조에서 Root node, Leaf node, Inner node를 찾는 문제다.  
Root node는 부모 노드가 없는 노드를 말하며, 그림에서는 5번 노드가 이에 해당한다.  
Leaf node는 자식 노드가 없는 노드를 말하며, 그림에서는 1번, 3번, 6번, 9번 노드가 이에 해당한다.  
Inner node는 Root node와 Leaf node가 아닌 노드를 말하며, 그림에서는 2번, 8번 노드가 이에 해당한다.

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
|-|-|
|5|Root|

### 2. Leaf node에 해당하는 테이블을 구한다.

Leaf node는 자식 노드가 없는 노드다.  
다시 말하면, 자식 노드 중에서 부모 노드 역할을 한 번도 하지 않은 노드이다.  
즉, 자식 노드 집합을 A, 부모 노드 집합을 B라고 할 때 A - B에 해당한다.  
차집합 A - B는 아래와 같이 WHERE 절 안에 서브쿼리를 작성하여 구할 수 있다.  
부모 노드 집합 B는 `SELECT DISTINCT p FROM bst WHERE p IS NOT NULL`으로부터 구할 수 있다.

```sql
SELECT 
    n, 
    'Leaf' AS node_type 
FROM 
    bst 
WHERE 
    n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL)
```

(출력)

|n|node_type|
|-|-|
|1|Leaf|
|3|Leaf|
|6|Leaf|
|9|Leaf|

### 3. Inner node에 해당하는 테이블을 구한다.

Inner node는 Root node와 Leaf node가 아닌 노드다.  
다시 말하면, 부모 노드 집합 중에서 Root node가 아닌 노드다.
부모 노드 집합  `SELECT DISTINCT p FROM bst WHERE p IS NOT NULL`에서 Root node가 아닌 노드를 구하는 WHERE 절 `WHERE p != (SELECT n FROM bst WHERE p IS NULL)`을 추가하면 된다.  
참고로 위 WHERE 절 안의 서브쿼리 `SELECT n FROM bst WHERE p IS NULL`는 Root node를 출력한다.

```sql
SELECT 
    DISTINCT p AS n, 
    'Inner'    AS node_type 
FROM 
    bst 
WHERE 
    p IS NOT NULL AND 
    p != (SELECT n FROM bst WHERE p IS NULL)
```

(출력)

|n|node_type|
|-|-|
|2|Inner|
|8|Inner|

### 4. 위 세 개의 테이블을 `UNION`을 이용하여 세로 방향으로 결합한다.

WITH 절을 이용하여 1.에서 구한 Root node를 `root_node` 이름을 가진 임시 테이블에 저장하고 2.에서 구한 Leaf node는 `leaf_node` 이름을 가진 임시 테이블에 저장하고 1.에서 구한 Inner node를 `inner_node` 이름을 가진 임시 테이블에 저장하자.

```sql
WITH root_node AS (
    SELECT 
        n, 
        'Root' AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NULL
), leaf_node AS (
    SELECT 
        n, 
        'Leaf' AS node_type 
    FROM 
        bst 
    WHERE 
        n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL)
), inner_node AS (
    SELECT 
        DISTINCT p AS n, 
        'Inner'    AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NOT NULL AND 
        p != (SELECT n FROM bst WHERE p IS NULL)
) 
```

그 후에 `UNION`을 이용하여 세 개의 임시 테이블 `root_node`, `leaf_node`, `inner_node`을 세로 방향으로 결합한 MySQL 코드는 다음과 같다.

```sql
SELECT * FROM root_node 
UNION 
SELECT * FROM leaf_node 
UNION 
SELECT * FROM inner_node
```

### 5. Node 값을 기준으로 오름차순 정렬한다.

```sql
SELECT * FROM root_node 
UNION 
SELECT * FROM leaf_node 
UNION 
SELECT * FROM inner_node 
ORDER BY n
```

(출력)

|n|node_type|
|-|-|
|1|Leaf|
|2|Inner|
|3|Leaf|
|5|Root|
|6|Leaf|
|8|Inner|
|9|Leaf|

## 풀이

```sql
-- with 절로 root_node, leaf_node, inner_node 임시 테이블 생성
WITH root_node AS (
    SELECT 
        n, 
        'Root' AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NULL
), leaf_node AS (
    SELECT 
        n, 
        'Leaf' AS node_type 
    FROM 
        bst 
    WHERE 
        n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL)
), inner_node AS (
    SELECT 
        DISTINCT p AS n, 
        'Inner'    AS node_type 
    FROM 
        bst 
    WHERE 
        p IS NOT NULL AND 
        p != (SELECT n FROM bst WHERE p IS NULL)
)

-- UNION으로 root_node, leaf_node, inner_node 결합 후 정렬
SELECT * FROM root_node 
UNION 
SELECT * FROM leaf_node 
UNION 
SELECT * FROM inner_node 
ORDER BY n
```