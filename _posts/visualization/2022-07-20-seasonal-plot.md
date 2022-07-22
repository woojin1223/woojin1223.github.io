---
title: "R로 구현하는 계절성 차트"
categories: 시각화
tags: [R, ggplot2, 계절성 차트]
---

<div style="margin-bottom:100px;"></div>

## 계절성 차트 (Seasonal plot)

`forecast` 패키지의 `ggseasonplot()`를 사용하면 시계열 객체(ts)를 대상으로 연도별 시계열 그래프를 표현할 수 있다.

```r
# load package and data
library(forecast)
library(ggplot2)
library(gridExtra)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("nottem")
data("AirPassengers")

# subset data 
nottem_small <- window(nottem, start = c(1920, 1), end = c(1925, 12)) # subset a smaller time window 

# seasonal plot 
airpassenger <- ggseasonplot(AirPassengers) + 
  theme(axis.text.x = element_text(angle = 60, vjust = 0.5))
nottem <- ggseasonplot(nottem_small) +
  theme(axis.text.x = element_text(angle = 60, vjust = 0.5))

grid.arrange(airpassenger, nottem, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/seasonal_plot-1.png)