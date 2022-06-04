---
title: "[RMarkdown] R Code Chunk"
categories: 
    - RMarkdown
tags:
    - R
    - RMarkdown
    - RCodeChunk
toc: true
toc_sticky: true
toc_label: "목차"
---

## R Code Chunk

**R Markdown 소개** 글에서 R Markdown의 세 가지 구성 요소는 YAML Header, Markdown Text, R Code Chunk라고 언급을 했다.  
그리고 **R Markdown - Markdown** 글에서 가장 먼저 Markdown Text에 대한 내용을 설명했다.  
이번에는 R Markdown으로 만든 보고서에서 R Code를 구현하는 핵심 부분인 **R Code Chunk**에 대해서 알아보자. 

## Code Chunk 만드는 방법 + 단축키

<p>시작하기에 앞서, Rmd 파일에서 Knit하여 나온 파일은 <b>보고서</b>라는 단어로 통일하자.<br>
아래 그림에서 볼 수 있듯이 Code Chunk는 Rmd 파일에서 음영처리되어 Markdown Text와 구분된다.<br>
Code Chunk를 만드는 방법은 <b>Markdown에서 코드 블럭을 만드는 방법과 유사</b>하다. 즉, <code>```{r}</code> 와 <code>```</code>를 코드 위 아래에 감싸주면 Code Chunk가 된다.<br>
또한, 단축키 <code>Ctrl + Alt + I</code> 를 눌러서 Code Chunk를 빠르게 삽입할 수 있다.<br>
참고로 이 단축키는 R Script 파일에선 작동이 안되고 R Markdown 파일에서만 작동된다.</p>

![three_components](/assets/images/three_components.png)

## Code Chunk 실행

Code Chunk 안의 코드를 실행하는 방법은 R Script 안의 코드를 실행하는 방법과 같다.  
즉, 한 줄씩 실행하려면 `Ctrl + Enter` 를 누르면 되고 Code Chunk 안의 코드 전체를 실행하려면 `Ctrl + Shift + Enter` 또는 Code Chunk 우측 상단의 톱니바퀴 옆 화살표 버튼을 누르면 된다.

## Code Chunk 이름

<p><b>R - 기본 개념</b> 글에서 변수에 대해서 배웠다.<br>
각 변수는 다른 이름을 가지고 있어서 서로 구분이 되는 것이 특징이다.<br>
변수처럼 Code Chunk도 서로 구분을 할 수 있게 이름을 붙일 수 있다.<br>
이렇게 이름을 붙이면 Knit하는 과정에서 오류가 났을 때 어느 Code Chunk에서 그 오류가 생겼는지 빠르게 판단할 수 있다는 장점이 있다.<br>
단, Code Chunk에 이름을 붙이지 않아도 정상적으로 Knit가 되지만 같은 이름의 Code Chunk가 있으면 Knit가 안되니 주의해야 한다.<br>
Code Chunk에 이름을 붙이는 방법은 다음과 같다.<br>
<code>```{r chunk_name}</code>와 <code>```</code>를 코드 위 아래에 감싸준다.<br>
첫 번째 <code>```</code> 다음에 <code>{r}</code>이 아닌 <code>{r chunk_name}</code>이 온다는 점에서 Code Chunk를 만드는 것과 구별된다.</p>

## Code Chunk 옵션

<p>R을 전혀 모르는 사람 앞에서 발표할 때 보고서에 있는 R Code는 오히려 발표에 방해가 될 수 있기에 R Code만 보고서에 빼야 하는 상황이 있다.<br>
또는 Code Chunk를 보여주기만 하고 실행은 하지 않도록 Code만을 출력해야 하는 상황이 있다.<br>
이러한 경우엔 Code Chunk에 옵션을 추가하면 된다.<br>
즉, Code Chunk에 여러 옵션들을 추가하여 다양한 형태의 보고서를 만들 수 있다.<br>
Code Chunk에 옵션을 추가하는 방법은 다음과 같다.<br>
첫 번째 <code>```</code> 다음에 <code>{r}</code> 이 아닌 <code>{r, key=value1, key2=value2, ...}</code> 을 작성한다.<br>
다시 말하자면 <code>```{r, key1=value1, key2=value2, ...}</code> 와 <code>```</code>를 코드 위 아래에 감싸준다.<br>
얼핏 보기엔 Code Chunk에 이름을 붙이는 방법과 같은 것처럼 보이지만 다른 점은 쉼표(<code>,</code>)로 각 옵션을 구분한다는 것이다.<br>
참고로 옵션을 추가하는 것은 함수의 argument를 넣는 것과 같은 형태이다.<br><br>
이제 본격적으로 Code Chunk에 어떤 옵션들이 있는지 하나씩 예를 들어가며 알아보자.</p>

(1) `eval=FALSE`: 코드를 실행하지 않고 코드 블럭만 보고서에 보여주고 싶은 경우

(Rmd에서 `eval=FALSE` 설정을 안 한 경우)

````
```{r}
print("Welcome to my blog.")
```
````

(출력 결과)  
코드 블럭과 코드를 실행한 결과가 같이 출력된다.

```
print("Welcome to my blog.")
```

```
[1] "Welcome to my blog."
```

(Rmd에서 `eval=FALSE` 설정을 한 경우)

````
```{r, eval=FALSE}
print("Welcome to my blog.")
```
````

(출력 결과)  
코드가 실행되지 않고 코드 블럭만 출력된다.

```
print("Welcome to my blog.")
```

(2) `include=FALSE`: 코드를 실행하지만 그에 따른 모든 결과물(코드블럭, 출력값, 플롯, 메시지, 경고문 등)을 보고서에 보여주고 싶지 않은 경우

(Rmd에서 `include=FALSE` 설정을 안 한 경우)

````
```{r}
library(tidyverse)
```
````

(출력 결과)  
코드 블럭과 코드를 실행하면 나오는 메시지가 같이 출력된다.

```
library(tidyverse)
```

```
-- Attaching packages -------------------------- tidyverse 1.3.0 --
```

```
√ ggplot2 3.3.2     √ purrr   0.3.4
√ tibble  3.0.3     √ dplyr   1.0.2
√ tidyr   1.1.2     √ stringr 1.4.0
√ readr   1.3.1     √ forcats 0.4.0
```

```
-- Conflicts ----------------------------- tidyverse_conflicts() --
x dplyr::filter() masks stats::filter()
x dplyr::lag()    masks stats::lag()
```

(Rmd에서 `include=FALSE` 설정을 한 경우)

````
```{r, include=FALSE}
library(tidyverse)
```
````

(출력 결과)  

(보고서에 아무 것도 출력되지 않고 `tidyverse` 라는 패키지가 Rmd 내에서 실행된다.)

(3) `echo=FALSE`: 코드를 보여주지 않은 채 실행하여 그 결과물만 보고서에 보여주고 싶은 경우

- 코드 블럭만 출력되지 않는다.

(Rmd에서 `echo=FALSE` 설정을 안 한 경우)

````
```{r}
print("Welcome to my blog.")
```
````

(출력 결과)

```
print("Welcome to my blog.")
```

```
[1] "Welcome to my blog."
```

(Rmd에서 `echo=FALSE` 설정을 한 경우)

````
```{r, echo=FALSE}
print("Welcome to my blog.")
```
````

(출력 결과)

```
[1] "Welcome to my blog."
```

(4) `results="hide"`: 코드를 실행하여 나오는 출력물을 보고서에 보여주고 싶지 않은 경우

- `eval=FALSE` 는 코드를 실행하지 않는 옵션이고 `results="hide"` 는 코드를 실행하지만 출력물을 보여주지 않는 것이다.

(Rmd에서 `results="hide"` 설정을 안 한 경우)

````
```{r}
print("Welcome to my blog.")
```
````

(출력 결과)

```
print("Welcome to my blog.")
```

```
[1] "Welcome to my blog."
```

(Rmd에서 `results="hide"` 설정을 한 경우)

````
```{r, results="hide"}
print("Welcome to my blog.")
```
````

(출력 결과)

```
print("Welcome to my blog.")
```

(5) `fig.show="hide"`: 코드를 실행하여 나오는 그림을 보고서에 보여주고 싶지 않은 경우

(Rmd에서 `results="hide"` 설정을 안 한 경우)

````
```{r}
hist(rnorm(10))
```
````

(출력 결과)  
`hist(rnorm(10))` 를 실행하면 평균이 0이고 표준편차가 1인 정규 분포에서 임의 추출된 표본 10개에 대한 히스토그램이 출력된다. 

![histogram](/assets/images/histogram.png)

(Rmd에서 `results="hide"` 설정을 한 경우)

````
```{r, fig.show="hide"}
hist(rnorm(10))
```
````

(출력 결과)  

(히스토그램이 출력되지 않는다.)

(6) `message=FALSE`: 코드를 실행하여 나오는 모든 메시지를 보고서에 보여주고 싶지 않은 경우

- 패키지 로드할 때 나오는 메시지를 출력하고 싶지 않은 경우, 이 옵션을 사용한다.

(Rmd에서 `message=FALSE` 설정을 안 한 경우)

````
```{r}
library(tidyverse)
```
````

(출력 결과)

```
library(tidyverse)
```

```
-- Attaching packages -------------------------- tidyverse 1.3.0 --
```

```
√ ggplot2 3.3.2     √ purrr   0.3.4
√ tibble  3.0.3     √ dplyr   1.0.2
√ tidyr   1.1.2     √ stringr 1.4.0
√ readr   1.3.1     √ forcats 0.4.0
```

```
-- Conflicts ----------------------------- tidyverse_conflicts() --
x dplyr::filter() masks stats::filter()
x dplyr::lag()    masks stats::lag()
```

(Rmd에서 `message=FALSE` 설정을 한 경우)

````
```{r, message=FALSE}
library(tidyverse)
```
````

(출력 결과)  
`tidyverse` 라는 패키지가 Rmd 내에서 실행이 되지만 코드 실행 후 나오는 메시지는 출력되지 않는다. 

```
library(tidyverse)
```

(7) `warning=FALSE`: 코드를 실행하여 나오는 모든 경고문을 보고서에 보여주고 싶지 않은 경우

(Rmd에서 `warning=FALSE` 설정을 안 한 경우)

````
```{r}
as.numeric("Hello")
```
````

(출력 결과)

```
Warning: NAs introduced by coercion
```

```
[1] NA
```

(Rmd에서 `warning=FALSE` 설정을 안 한 경우)

````
```{r, warning=FALSE}
as.numeric("Hello")
```
````

(출력 결과)  
character 타입을 numeric 타입으로 바꾸면 경고 메시지가 출력되며 NA를 반환하는데, `warning=FALSE` 옵션을 주면 그 경고 메시지를 무시할 수 있다.

```
[1] NA
```

지금까지 설명한 옵션들을 표로 정리하면 다음과 같다.

Option	             |Run code|Show code|Output|Plots   |Messages|Warnings 
------------------- |-----------|----------|----------|-------|-----------|----------
`eval=FALSE`       |	x            |	              |     x       | x        | x	         | x
`include=FALSE`  |	              | 	  x  |     x       | x        | x              | x
`echo=FALSE`      |               |	x	      |             |           |                 |
`results="hide"`   |               |               |	x          |           |                 |
`fig.show="hide"`|               |               |              | x    	|                 |
`message=FALSE`|               |               |              |          | x               |
`warning=FALSE` |               |               |              |          |                  | x

 

### 전역 옵션 (Global option)

마지막으로 전역 옵션에 대해서 알아보자.  
전역 옵션은 말 그대로 Code Chunk 하나하나 옵션을 지정하기 힘들 때 모든 Code Chunk에 적용되는 옵션(default option)을 지정하는 것이다.  
Rmd 파일의 YAML Header 바로 아래에 `knitr::opts_chunk$set()` 라는 코드를 가진 Code Chunk를 삽입하면 전역 옵션이 적용된다.  
일반적으로 전역 옵션을 적용할 때 해당 Code Chunk에 `setup` 이라는 이름을 붙이고  `include=FALSE` 옵션을 사용하여 코드 실행만 되게 한다.  
아래는 모든 Code Chunk를 보고서에 보이게 하고(`echo=TRUE`), 코드 실행하며 나오는 에러까지 보고서에 보이게 하는(`error=TRUE`) 전역 옵션을 설정하는 예시이다.  

(젼역 옵션 예시)

1. 코드 이름: `setup`
2. 전역 옵션: `echo=TRUE` and `error=TRUE`

````
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE, error = TRUE)
```
````

### 인라인 Code Chunk

<p><b>R Markdown - Markdown</b> 포스트에서 인라인 코드에 대해서 배웠다.<br>
인라인 코드는 Markdown Text에서 코드 모습을 한 텍스트를 의미한다.<br>
인라인 Code Chunk는 코드 모습을 한 텍스트인 인라인 코드와 단어가 비슷해서 동의어라고 착각할 수 있다.<br>
하지만 그 의미는 다르다. <b>인라인 Code Chunk</b>는 Markdown Text에서 R Code가 실행된 결과를 텍스트로 보여준다.<br>
그렇다면 인라인 Code Chunk는 언제 사용할까?<br>
Rmd 파일 내에서 Markdown Text와 R Code Chunk는 구분되어 있어서 R Code 실행은 R Code Chunk에서만 할 수 있다.<br>
Markdown Text에서 R Code가 실행된 결과를 문장 안에 삽입하고 싶을 때가 있다.<br>
예를 들어, 보고서에서 다루고 있는 데이터의 행과 열의 개수를 설명할 때 직접 값을 구하여 숫자로 적는 방법이 있지만 분석을 하다보면 데이터는 자주 변형되기 때문에 데이터의 행과 열의 개수도 변할 때가 많다.<br>
그럴 때마다 직접 값을 구하여 숫자로 적으면 실수하기 쉽고 귀찮은 일이다.<br>
이 때 인라인 Code Chunk를 사용하면 쉽게 해결된다.<br>
인라인 Code Chunk를 사용하는 방법은 인라인 코드와 유사하다.<br>
차이점은 <code>```</code>와 <code>```</code>로 R Code를 감싸주는 게 아니라 <code>`r</code> 와 <code>`</code>로 R Code를 감싸줘야 한다.<br>
예를 들어,</p>

```
원주율을 소수점 아래 4 번째 숫자까지 반올림하여 나타내면 `r round(pi, 4)` 이다.  
```

를 출력하면

```
원주율을 소수점 아래 4 번째 숫자까지 반올림하여 나타내면 3.1416 이다.
```

가 나온다.  
다른 예시를 들어보자.  
`data` 라는 변수는 차원이 (500, 4)인 `data.frame` 이라고 하자.

```
이 데이터의 행의 개수는 `r nrow(data)` 이고 열의 개수는 `r ncol(data)` 이다.
```

를 출력하면

```
이 데이터의 행의 개수는 500 이고 열의 개수는 4 이다.
```

가 나온다.

---

## 참고

- [R for Data Science](https://r4ds.had.co.nz/)