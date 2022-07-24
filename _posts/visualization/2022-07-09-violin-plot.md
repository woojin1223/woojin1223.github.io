---
title: "R로 구현하는 바이올린 플롯"
categories: 시각화
tags: [R, ggplot2, 바이올린 플롯]
---

<div style="margin-bottom:100px;"></div>

## 바이올린 플롯 (Violin plot)

바이올린 플롯은 다섯가지 요약 수치를 보여주는 상자 그림과 다르게 **그룹별 밀도**를 보여준다. 그룹이 많은 경우, 바이올린 플롯이 밀도 그래프보다 그룹간 밀도를 비교하기 쉽다. `geom_violin()`을 사용하여 시각화할 수 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mpg", package = "ggplot2")

# violin plot
violin <- ggplot(mpg) + 
  geom_violin(aes(x = class, y = hwy), fill = "mediumseagreen") + 
  labs(x = "class of vehicle", 
       y = "highway mileage",
       title = "Violin plot", 
       subtitle = "highway mileage vs. class of vehicle", 
       caption = "source: mpg")

# density plot
density <- ggplot(mpg) + 
  geom_density(aes(x = hwy, fill = class), alpha = 0.8) + 
  labs(x = "city mileage",
       title = "Density plot", 
       subtitle = "highway mileage vs. class of vehicle", 
       fill = "class of vehicle",
       caption = "source: mpg")

grid.arrange(violin, density, nrow = 2)
```

![](/public/img/2022-06-22-visualization-summary/violin_plot-1.png)