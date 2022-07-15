---
title: "R로 구현하는 영역 차트"
categories: 시각화
tags: [R, ggplot2, 영역차트]
---

<div style="margin-bottom:100px;"></div>

## 영역 차트 (Area chart)

영역 차트는 꺾은 선 그래프(line graph)를 그린 후 꺾은 선과 x축 사이의 영역을 채우는 시각화 방법이다. `geom_area()`를 사용하여 구현할 수 있다.

```r
# load package and data
library(ggplot2)
library(lubridate)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("economics", package = "ggplot2")

# compute percent returns
economics$returns_perc <- c(0, diff(economics$psavert)/economics$psavert[-length(economics$psavert)])

# create break points and labels for axis ticks
brks <- economics$date[seq(1, length(economics$date), 12)]
lbls <- year(economics$date[seq(1, length(economics$date), 12)])

# area chart
ggplot(economics[1:50,]) +
  geom_area(aes(x = date, y = returns_perc)) + 
  scale_x_date(breaks = brks, labels = lbls) +
  labs(y = "percent returns",
       title = "Area chart", 
       subtitle = "Perent returns for personal savings",
       caption = "source: economics")
```

![](/public/img/2022-06-22-visualization-summary/area_chart-1.png)