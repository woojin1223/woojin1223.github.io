---
title: "[RMarkdown] 소개"
categories: 
    - RMarkdown
tags:
    - R
    - RMarkdown
toc: true
toc_sticky: true
toc_label: "목차"
---

## 소개

R 코드를 작성하다 보면 <u>코드에 대한 부연 설명</u>이 필요합니다.  
이는 본인이 작성한 코드를 다시 볼 때 쉽게 이해하기 위함도 있지만 여러 사람들과 같이 코딩할 때 그들을 쉽게 이해시키기 위함도 있습니다.  
프로젝트의 규모가 커질 수록 혼자 코딩하지 않고 여러 사람들과 협업을 하여 코딩을 하기 때문에 <u>코드에 대한 부연 설명은 선택이 아닌 필수</u>입니다.  

R 코드를 작성하는 파일인 **R Script**(`.R`)는 주석(#)으로 코드에 대한 설명을 넣을 수 있지만, 가시성이 좋지 않고 글자 크기를 조절하거나 굵게 하는 등 형식을 마음대로 바꿀 수 없다는 단점이 있습니다.  
즉, R script에는 코드가 메인이고 텍스트는 서브 기능을 할 뿐입니다.  

하지만, **R Markdown**(`.Rmd`) 파일에는 코드와 더불어 텍스트를 자유로운 형식으로 쓸 수 있습니다.  
즉, R Markdown을 사용하여 <u>R 코드를 곁들인 프로젝트 보고서</u>를 작성할 수 있습니다.  
그리고 `html` 과 `pdf` 등 다양한 파일 형식으로 보고서를 만들 수 있습니다.  
아래는 R Markdown 파일의 예시입니다.

## 예시

````
---
title: "R Markdown"
author: "Tong Nam"
date: "2021 04 25"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## R Markdown

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:

```{r cars}
summary(cars)
```

## Including Plots

You can also embed plots, for example:

```{r pressure, echo=FALSE}
plot(pressure)
```

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
````

RStudio의 상단 탭에 있는 _File > New File > R Markdown_ 에서 OK를 클릭하여 위 예시와 같이 기본적인 내용이 들어 있는 Rmd 파일을 만들 수 있습니다.  
그리고 Rmd 파일에서 `Knit` 버튼을 클릭하거나 `Ctrl + Shift + K` 를 누르면 HTML 형식의 보고서가 만들어집니다.

![rmd_tutorial](/assets/images/rmd_tutorial.PNG)  

R Markdown 파일은 다음과 같이 <u>세 가지 요소</u>로 구성되어 있습니다.

<ul>
<li><b>YAML Header</b>: YAML 형식으로 된 헤더로서, 다양한 렌더링 옵션을 추가할 수 있다. <code>---</code> 로 시작하여  <code>---</code> 로 끝남</li>
<li><b>Markdown Text</b>: Markdown 형식으로 된 텍스트로서, 코드에 대한 부연 설명 뿐만 아니라 ms word 파일처럼 일반적인 글쓰기를 할 수 있음</li>
<li><b>R Code Chunk</b>: R 코드가 들어있는 블럭으로서, 보고서를 만들 때 이 코드 블럭이 실행되어서 보고서에 R 결과물을 담을 수 있음. 그리고 YAML Header와 비슷하게 <code>```{r}</code> 로 시작하여 <code>```</code> 로 끝남</li>
</ul>

아래 그림을 참고하여 R Markdown의 세 가지 구성 요소를 쉽게 이해할 수 있습니다.  

![three_components](/assets/images/three_components.png)

---

## 참고

- [R for Data Science](https://r4ds.had.co.nz/)