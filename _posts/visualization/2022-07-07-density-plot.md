---
title: "R로 구현하는 밀도 그래프"
categories: 시각화
tags: [R, ggplot2, 밀도 그래프]
---

<div style="margin-bottom:100px;"></div>

## 밀도 그래프 (Density plot)

히스토그램은 막대를 그리는 구간인 bin의 개수 혹은 너비를 어떻게 잡는지에 따라 전혀 다른 모양이 될 수 있다 `goem_density()`로 시각화할 수 있는 밀도 그래프는 막대의 너비를 가정하지 않고 모든 점에서 데이터의 밀도, 즉 확률밀도함수를 추정한다.

```r
# load package and data
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# density plot
ggplot(mpg, aes(x = cty)) + 
  geom_density(aes(fill = factor(cyl)), alpha = 0.8) + 
  labs(x = "city mileage",
       title = "Density plot", 
       subtitle = "City mileage grouped by number of cylinders", 
       fill = "# cylinders",
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/density_plot-1.png)