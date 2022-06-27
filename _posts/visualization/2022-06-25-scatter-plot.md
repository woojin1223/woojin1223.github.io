---
title: "R로 구현하는 산점도"
categories: 시각화
tags: [R, ggplot2, 산점도]
---

<div style="margin-bottom:100px;"></div>

## 산점도 (Scatter plot)

두 변수 사이의 관계 특성을 이해하고자 할 때 첫 번째로 떠올릴 수 있는 것은 산점도이다.
`geom_point()`를 사용하여 기본적인 산점도를 그리고 `geom_smooth()`를 통해서 스무딩 선을 표현할 수 있다.

```r
options(scipen = 999) # turn-off scientific notation like 1e+48
library(ggplot2)
theme_set(theme_bw()) # pre-set the bw theme.
data("midwest", package = "ggplot2")

# scatter plot with smooth plot
ggplot(midwest, aes(x = area, y = poptotal)) + 
  geom_point() + 
  geom_smooth(method = "loess", se = FALSE) + 
  coord_cartesian(xlim = c(0, 0.1), ylim = c(0, 500000)) +
  labs(x = "area", 
       y = "population", 
       title = "Scatter plot", 
       subtitle = "area vs. population", 
       caption = "source: midwest")
```

![](/public/img/2022-06-22-visualization-summary/scatter_plot-1.png)