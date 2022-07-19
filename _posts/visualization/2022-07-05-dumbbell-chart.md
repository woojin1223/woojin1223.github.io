---
title: "R로 구현하는 덤벨 차트"
categories: 시각화
tags: [R, ggplot2, 덤벨 차트]
---

<div style="margin-bottom:100px;"></div>

## 덤벨 차트 (Dumbbell chart)

덤벨 차트는 슬로프 차트와 동일한 정보를 전달하지만 두 시점에서 값의 증감을 덤벨 형태로 표현한다는 점에서 차이가 있다. `ggalt` 패키지의 `geom_dumbbell()`을 사용하여 시각화할 수 있다.

```r
# load package and data
library(ggplot2)
library(ggalt)
library(scales)
library(tidyr)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
health <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/health.csv")
health$Area <- factor(health$Area, levels = as.character(health$Area)) # for right ordering of the dumbbells
health2 <- gather(health, key = "year", value = "percent", -Area)

# dumbbell chart
ggplot(health) +
  geom_point(data = health2, aes(x = percent, y = Area, color = year), size = 3) +
  geom_dumbbell(aes(x = pct_2013, xend = pct_2014, y = Area), 
                size = 1, 
                color = "gray", colour_x = "blue", colour_xend = "red") +
  scale_color_manual(name = "Year",
                    values = c("pct_2013" = "blue", "pct_2014" = "red"),
                    labels = c("2013", "2014")) +
  scale_x_continuous(label =  percent) + 
  labs(x = "", 
       y = "", 
       title = "Dumbbell chart",
       subtitle = "Percent change: 2013 vs. 2014",
       caption = "source: https://github.com/hrbrmstr/ggalt")
```

![](/public/img/2022-06-22-visualization-summary/dumbbell_chart-1.png)