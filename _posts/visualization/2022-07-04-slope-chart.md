---
title: "R로 구현하는 슬로프 차트"
categories: 시각화
tags: [R, ggplot2, 슬로프차트]
---

<div style="margin-bottom:100px;"></div>

## 슬로프 차트 (Slope chart)

슬로프 차트는 두 시점에서 값의 증감을 기울기로 시각화하는 방법이다. `ggplot2`에는 슬로프 차트에 대한 내장 함수가 없기 때문에 아래와 같이 직접 커스터마이징해야 한다.

```r
# load package and data
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
df <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/gdppercap.csv")
colnames(df) <- c("continent", "1952", "1957")
left_label <- paste(df$continent, round(df$`1952`), sep = ", ")
right_label <- paste(df$continent, round(df$`1957`), sep = ", ")
df$class <- ifelse((df$`1957` - df$`1952`) < 0, "Down", "Up")

# slope chart
p <- ggplot(df) + 
  geom_segment(aes(x = 1, xend = 2, y = `1952`, yend = `1957`, col = class), 
               size = 0.75, 
               show.legend = FALSE) + 
  geom_vline(xintercept = 1, linetype = "dashed", size = 0.1) + 
  geom_vline(xintercept = 2, linetype = "dashed", size = 0.1) + 
  scale_color_manual(values = c("Up" = "#00ba38", "Down" = "#f8766d")) + # color of lines 
  labs(x = "", y = "mean GDP", title = "mean GDP per capita") +
  coord_cartesian(xlim = c(0.5, 02.5), ylim = c(0, 1.1 * max(df$`1952`, df$`1957`)))

# add texts
p <- p + geom_text(label = left_label, y = df$`1952`, x = rep(1, nrow(df)), hjust = 1.1, size = 3.5) 
p <- p + geom_text(label = right_label, y = df$`1957`, x = rep(2, nrow(df)), hjust = -0.1, size = 3.5) 
p <- p + geom_text(label = "Time 1(1952)", x = 1, y = 1.1 * (max(df$`1952`, df$`1957`)), hjust = 1.2, size = 4) # title 
p <- p + geom_text(label = "Time 2(1957)", x = 2, y = 1.1 * (max(df$`1952`, df$`1957`)), hjust = -0.1, size = 4) # title 

# simplify theme
p + theme(panel.grid = element_blank(), 
          axis.ticks = element_blank(),
          axis.text.x = element_blank())
```

![](/public/img/2022-06-22-visualization-summary/slope_chart-1.png)