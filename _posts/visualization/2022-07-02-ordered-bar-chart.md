---
title: "R로 구현하는 순위 막대 그래프"
categories: 시각화
tags: [R, ggplot2, 막대 그래프]
---

<div style="margin-bottom:100px;"></div>

## 순위 막대 그래프 (Ordered bar chart)

순위 막대 그래프는 y값이 정렬된 막대 그래프이다. y값의 크기 순서대로 x 변수의 순서를 지정하려면 `reorder()`를 사용하면 된다. 그리고 아래에 나오는 두 가지 사항을 주의하자.

- x축이 범주형 변수
- y축이 수치형 변수이고 이를 기준으로 정렬

```r
# load package and data
library(dplyr)
library(ggplot2)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mpg", package = "ggplot2")

# ordered bar chart
mpg %>%
  group_by(manufacturer) %>%
  summarise(mileage = mean(cty)) %>%
  ggplot() +
  geom_bar(aes(reorder(x = manufacturer, -mileage), y = mileage), 
           stat = "identity", width = 0.5, fill = "tomato3") +
  theme(axis.text.x = element_text(angle = 45, vjust = 0.5)) +
  labs(x = "manufacturer",
       title = "Ordered bar chart",
       subtitle = "manufacturer vs. avg. mileage",
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/ordered_bar_chart-1.png)