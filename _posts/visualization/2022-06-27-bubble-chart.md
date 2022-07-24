---
title: "R로 구현하는 버블 차트"
categories: 시각화
tags: [R, ggplot2, 산점도]
---

<div style="margin-bottom:100px;"></div>

## 버블 차트 (Bubble chart)

산점도로 두 수치형 변수 간의 관계를 파악할 수 있다. 버블 차트는 x축, y축의 변수 외에도 다음 변수들을 추가로 시각화할 수 있다.

- 색상을 통한 범주형 변수 
- 크기를 통한 수치형 변수

```r
# load package and data
library(ggplot2)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mpg", package = "ggplot2")

# prepare data
mpg_select <- mpg[mpg$manufacturer %in% c("audi", "ford", "honda", "hyundai"),]

# bubble chart
ggplot(mpg_select) +
  geom_jitter(aes(x = displ, y = cty, col = manufacturer, size = hwy)) +
  labs(title = "Bubble chart", 
       subtitle = "displacement vs. city mileage")
```

![](/public/img/2022-06-22-visualization-summary/bubble_chart-1.png)