---
title: "R로 구현하는 계층적 덴드로그램"
categories: 시각화
tags: [R, ggplot2, 계층적 덴드로그램, 군집 분석]
---

<div style="margin-bottom:100px;"></div>

## 계층적 덴드로그램 (Hierarchical dendrogram)

계층적 군집 분석은 각 개체 하나하나를 군집으로 두고 매 단계에서 가장 근접한 2개의 군집들을 하나의 군집으로 병합하는 방법을 말한다. 이러한 군집화 과정을 간략하게 표현한 도표가 바로 덴드로그램이다. `hclust()`를 통해 계층적 군집 분석을 수행하고 `ggdendro` 패키지의 `ggdendrogram()`을 통해 계층적 덴드로그램을 시각화할 수 있다.

```r
# load package and data
library(ggplot2) 
library(ggdendro) 
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("USArrests")

hc <- hclust(dist(USArrests), method = "average") # hierarchical clustering 

# hierarchical dendrogram
ggdendrogram(hc, rotate = TRUE, size = 2)
```

![](/public/img/2022-06-22-visualization-summary/hierarchical_dendrogram-1.png)