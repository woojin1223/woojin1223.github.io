---
title: "[R] 기본 개념"
categories: 
    - R
tags: 
    - R
toc: true
toc_sticky: true
toc_label: "목차"
---

![Rlogo](https://www.r-project.org/Rlogo.png)

## 소개

- 통계학자가 만든 프로그래밍 언어
- 오픈소스로 배포되고 있어 무료로 사용가능
- 통계 소프트웨어 개발과 데이터 분석에 널리 사용됨
- 사용자가 직접 만든 함수 꾸러미인 [패키지](https://cran.r-project.org/web/packages/available_packages_by_name.html)를 통해 다양한 작업을 손쉽게 할 수 있음

### 장점

- 무료로 사용가능
- 대부분의 통계 기법을 구현할 수 있음
- 데이터 핸들링에 최적화되어 있음
- 사용자가 많아 참고할 자료가 많음

### 단점

- 자유도가 높음 → 배우기 어려움
- 다른 언어(C, Matlab, Python, Julia 등)에 비해 컴퓨팅 속도가 느림
- 특히, for 문  속도가 느림

## 특징

### 1. 계산기

R에서 사칙연산이 가능합니다.  

- ex1) 괄호를 추가하여 괄호 안의 계산을 먼저 할 수 있습니다. 

```r
1 / 200 * 30 # 나눗셈을 먼저 수행하고 곱셈을 수행한다.
```

```
[1] 0.15
```

```r
1 / (200 * 30) # 곱셈을 먼저 수행하고 나눗셈을 수행한다.
```

```
[1] 0.0001666667
```

- ex2) R의 기본 함수 `round()`를 사용하여 계산 결과를 반올림할 수 있습니다.

```r
(59 + 73 + 2) / 3
```

```
[1] 44.66667
```

```r
round((59 + 73 + 2) / 3) # (참고) round off: 반올림하다.
```

```
[1] 45
```

- ex3) `pi`는 R에서 기본으로 제공하는 변수입니다.

```r
pi
```

```
[1] 3.141593
```

```r
sin(pi / 2) # R의 기본 함수 sin() 사용
```

```
[1] 1
```

- ex4) `0 / 0`은 **NaN**(Not a Number)을 반환합니다.

```r
0 / 0
```

```
[1] NaN
```

- ex5) `1 / 0`은 **Inf**($\infty$)을 반환합니다.

```r
1 / 0
```

```
[1] Inf
```

### 2. 변수

#### 정의  

변수는 나중에 사용할 값들을 저장하는 박스입니다.  
변수는 다음과 같이 만들 수 있습니다.

```r
variable <- value # assign the value to the variable.
```

위의 작업을 **변수 할당**(variable assignment)이라고 합니다. 

#### 규칙

`<-` 를 사용하여 새로운 변수를 만들 수 있습니다.  
변수 이름은 반드시 글자로 시작해야 합니다.  
그리고 숫자와 `_` 와 `.` 같은 특수기호를 포함할 수 있습니다.

```r
r_rocks <- 2 ^ 3   # This is preferred. 
                   # RStudio shortcut: Alt + - (minus sign).
r_rocks = 2 ^ 3    # This is possible, but it will cause confusion later. 
                   # Avoid using =.
2 ^ 3 -> r_rocks   # This works but is weird. Avoid using ->.

r_rocks            # Inspecting a variable.
```

```
[1] 8
```

```r
r_rokcs  # Watch out typos.
```

```
Error in eval(expr, envir, enclos): 객체 'r_rokcs'를 찾을 수 없습니다
```

### 3.  함수

R에서는 다양한 종류의 함수들이 있고 다음과 같이 함수를 사용할 수 있습니다.

```r
function_name(arg1 = val1, arg2 = val2, ...)
```

다음의 코드는 `seq()` 함수를 실행하여 그 결과를 변수 `y`에 저장하고 `y`의 내용을 출력하는 것입니다.

```r
y <- seq(from = 1, to = 10, length.out = 5) # (참고) sequence: 수열
y
```

```
[1]  1.00  3.25  5.50  7.75 10.00
```

아래의 방법으로도 변수 할당 후에 바로 출력할 수 있습니다.

```r
(y <- seq(1, 10, length.out = 5)) # 변수 할당하는 코드를 괄호로 감싸 줌
```

```
[1]  1.00  3.25  5.50  7.75 10.00
```

## Style Guide

R에서도 _coding convention_ 이 있습니다.  
이를 **R Style Guide**라고 하는데, 다음의 두 가이드가 유명합니다.

- [Google’s R Style Guide](https://google.github.io/styleguide/Rguide.html)
- [Tidyverse Style Guide](https://style.tidyverse.org/)

두 가이드 모두 **사람이 이해할 수 있게 코드를 작성**해야 한다는 것을 강조하고 있습니다.  
여기서는 간단한 예시로 변수 이름을 만드는 방법에 대해서 알아 보겠습니다.

```r
this_is_a_snake_case            # Snake Case
camelCaseLooksLikeThis          # Camel Case
r.programmers.often.use.periods # Dot Case
```

위와 같이 크게 세 가지 경우가 있습니다.  
여기서 가장 추천하는 방법은 **Snake Case**입니다.  
왜냐하면  `_` 가 빈칸의 기능을 하여 가독성에 도움이 되고, Python과 같은 다른 언어에도 사용할 수 있는 방법이기 때문입니다.  
(Dot Case는 Python에서 사용 불가능)

---

## 참고

- [R for Data Science](https://r4ds.had.co.nz/)