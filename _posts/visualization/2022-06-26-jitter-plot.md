---
title: "R로 구현하는 지터 플롯"
categories: 시각화
tags: [R, ggplot2, 산점도]
---

<div style="margin-bottom:100px;"></div>

## 지터 플롯 (Jitter plot)

지터는 데이터 값에 약간의 노이즈를 추가하는 방법을 말한다. 노이즈를 추가하면 데이터 값이 조금씩 움직여서 같은 값을 가지는 데이터가 그래프에 여러 번 겹쳐진 채 표시되는 것을 막아준다. `geom_point()`를 사용하는 대신 `geom_jitter()`를 사용하여 시각화할 수 있다. `geom_point()`와 `geom_jitter()` 둘 다 산점도를 그리지만 겹쳐진 점을 표시하는 방법에 차이가 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
theme_set(theme_bw()) # pre-set the bw theme.
data("mpg", package = "ggplot2")

g <- ggplot(mpg, aes(cty, hwy))

# scatter plot
point <- g + geom_point() + 
  labs(title = "Scatter plot with overlapping points", 
       subtitle = "city vs. highway mileage")

# jitter plot
jitter <- g + geom_jitter(width = 0.5, size = 1) +
  labs(title = "Jittered scatter plot",
       subtitle = "city vs. highway mileage")

grid.arrange(point, jitter, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/jitter_plot-1.png)