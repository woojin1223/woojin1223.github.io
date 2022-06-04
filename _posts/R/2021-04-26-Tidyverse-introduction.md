---
title: "[Tidyverse] 소개"
categories: 
    - Tidyverse
tags:
    - R
    - Tidyverse
toc: true
toc_sticky: true
toc_label: "목차"
---
# Tidyverse - 소개

<center><img src="https://www.tidyverse.org/images/hex-tidyverse.png" height="100px" alt="tidyverse_logo"></center>

[Tidyverse 공식 홈페이지](https://www.tidyverse.org/)에 있는 tidyverse 소개 문구를 인용하면서 이 글을 시작하겠습니다.

> The tidyverse is an opinionated collection of R packages designed for data science. All packages share an underlying design philosophy, grammar, and data structures.

한마디로 Tidyverse는 데이터 과학을 위한 R 패키지입니다.  
이 패키지를 잘 다룰 수 있다면 저장된 데이터 파일을 불러오고 시각화하고 전처리하는 등, 데이터를 가지고 행하는 모든 작업을 손쉽게 할 수 있습니다.

## 특징

- RStudio에서 직접 개발하고 관리하는 패키지
- 8 개의 핵심 패키지로 이루어진 메타 패키지
- 각 패키지의 공식 문서가 매우 잘 되어 있음
- 사용자층이 두터워 영어로 검색하면 많은 질의응답을 찾을 수 있음
- tidyverse 사상에 영감을 얻어 제작한 개인 패키지가 많음
    + ex) tidyquant, tidytext 등

## 핵심 패키지

### ggplot2

- [The Grammar of Graphics](https://books.google.co.kr/books/about/The_Grammar_of_Graphics.html?id=_kRX4LoFfGQC&redir_esc=y)의 사상을 기반으로 하는 **데이터 시각화** 패키지
- R에서 가장 인기가 많은 패키지
- 층(layer)을 쌓아 올리는 방법으로 그래프를 커스터마이징할 수 있음

### dplyr

- **데이터 전처리** 패키지
- 데이터의 행과 열을 조작하는데 쓰이는 패키지

### tidyr

- 주어진 데이터를 **tidy data** 형태로 만드는 패키지
- tidy data란 아래 세 가지 특성을 가지는 데이터
    1. 모든 열은 변수 (Every column is variable.)
    2. 모든 행은 관측치 (Every row is an observation.)
    3. 모든 원소는 하나의 값 (Every cell is a single value.)

### readr

- 직사각형 모양의 데이터 파일을 빠르고 편리하게 불러오는 패키지
- 대다수의 데이터 확장자 파일을 불러올 수 있음
    - csv, tsv, fwf 등

### purrr

- 데이터의 각 행이나 각 열에 특정 함수를 반복적으로 적용하는 함수들로 구성됨
- map 계열의 함수를 제공함
    - R 기본 패키지의 apply 계열의 함수들보다 실행 속도가 빠르고 유연함

### tibble

- tibble을 생성하는 패키지
- tibble이란
    - 데이터 객체에 대한 자료형(class)
    - R에서 데이터를 표현하는 데 전통적으로 쓰였던 data.frame보다 더 유연함

### stringr

- **문자열 조작** 패키지
- 정규표현식을 지원함

### forcats

- **factor 조작** 패키지
- R에서는 factor라는 자료형으로 범주형 자료를 표현함

---

## 참고

- [Tidyverse](https://www.tidyverse.org/)
- [R for Data Science](https://r4ds.had.co.nz/)