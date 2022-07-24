---
title: "R로 구현하는 히스토그램"
categories: 시각화
tags: [R, ggplot2, 히스토그램]
---

<div style="margin-bottom:100px;"></div>

## 히스토그램 (Histogram)

히스토그램은 **도수분포표를 그래프로 시각화**한 것이다. 즉, 수치형 변수에 대해서 구간별 빈도 수를 보여준다. `geom_histogram()`을 통해서 구현할 수 있으며 `bins` 혹은 `binwidth`를 통해 구간의 범위를 조정할 수 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# histogram
g <- ggplot(mpg, aes(x = hwy, fill = class)) + 
  scale_fill_brewer(palette = "BrBG")

hist_binwidth <- g + geom_histogram(binwidth = 2, col = "black", size = 0.1) + # set width of bin
  labs(title = "Histogram with auto binning", 
       subtitle = "Highway mileage across vehicle classes")

hist_bins <- g + geom_histogram(bins = 8, col = "black", size = 0.1) + # set number of bins 
  labs(title = "Histogram with fixed bins", 
       subtitle = "Highway mileage across vehicle classes")

grid.arrange(hist_binwidth, hist_bins, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/histogram-1.png)