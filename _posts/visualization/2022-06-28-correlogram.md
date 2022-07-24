---
title: "R로 구현하는 상관관계 그래프"
categories: 시각화
tags: [R, ggplot2, 상관관계]
---

<div style="margin-bottom:100px;"></div>

## 상관관계 그래프 (Correlogram)

동일한 데이터 내에 존재하는 여러 개의 수치형 변수의 상관관계 표 형태로 확인할 수 있다. `ggcorplot` 패키지를 사용하여 편리하게 구현 가능하다.

```r
# load package and data
library(ggcorrplot)
data("mtcars")

# correlation matrix
corr_matrix <- round(cor(mtcars), 2)

# correlogram
ggcorrplot(corr_matrix, 
           hc.order = TRUE, 
           type = "lower", 
           lab = TRUE, 
           lab_size = 3, 
           method = "square", 
           colors = c("skyblue", "white", "lightpink"),
           title = "Correlogram of mtcars", 
           ggtheme = theme_bw)
```

![](/public/img/2022-06-22-visualization-summary/correlogram-1.png)