---
title: "R로 구현하는 와플 차트"
categories: 시각화
tags: [R, ggplot2, 와플차트]
---

<div style="margin-bottom:100px;"></div>

## 와플 차트 (Waffle chart)

와플 차트는 범주별 구성을 시각화하는 좋은 방법이다. `geom_tile()`를 사용하여 구현할 수 있다.

```r
# load package and data
library(ggplot2)
library(RColorBrewer)
data("mpg", package = "ggplot2")

# prepare data
waff_data <- mpg$class # categorical data
nrows <- 10
df <- expand.grid(y = 1:nrows, x = 1:nrows)
waff_table <- round(table(waff_data) * (nrows^2/length(waff_data)))
df$category <- factor(rep(names(waff_table), waff_table)) 
# NOTE: if sum(waff_table) is not 100 (i.e. nrows^2), it will need adjustment to make the sum to 100. 

# waffle chart
ggplot(df) + 
  geom_tile(aes(x = x, y = y, fill = category),color = "black", size = 0.5) + 
  scale_fill_brewer(palette = "Set3") +
  scale_x_continuous(expand = c(0, 0)) + 
  scale_y_continuous(expand = c(0, 0)) +
  theme(plot.title = element_text(size = rel(1.2)), 
        axis.text = element_blank(),
        axis.title = element_blank(), 
        axis.ticks = element_blank(), 
        legend.title = element_blank()) +
  labs(title = "Waffle chart", 
       subtitle = "Class of vehicles", 
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/waffle_chart-1.png)