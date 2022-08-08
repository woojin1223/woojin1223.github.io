---
title: "[HackerRank] Binary Tree Nodes"
categories: SQL
tags: [HackerRank, MySQL]
---

## 문제 링크

<https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true>

## 테이블 설명

`BST`는 이진트리 구조를 (자식 노드, 부모 노드) 형태의 2열로 구성된 테이블이다.  
테이블 예시는 다음과 같다.

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

## 풀이

```sql
SELECT 
    n, 
    'Root' AS node_type 
FROM 
    bst 
WHERE 
    P IS NULL 
UNION 
SELECT 
    n, 
    'Leaf' AS node_type 
FROM 
    bst 
WHERE 
    n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL) 
UNION 
SELECT 
    DISTINCT p AS n, 
    'Inner'    AS node_type 
FROM 
    bst 
WHERE 
    p IS NOT NULL AND 
    p != (SELECT n FROM bst WHERE P IS NULL) 
ORDER BY 
    n
```