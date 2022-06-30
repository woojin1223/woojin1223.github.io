---
title: "R로 구현하는 롤리팝 차트"
categories: 시각화
tags: [R, ggplot2, 롤리팝차트]
---

<div style="margin-bottom:100px;"></div>

## 롤리팝 차트 (Diverging lollipop chart)

Diverging lollipop chart는 diverging bar chart와 동일한 정보를 전달하지만 구체적으로 어떤 값을 가지는지 추가로 알 수 있다. `geom_point()`와 `geom_segment()`를 사용하여 시각화할 수 있다.

```r
# load package and data
library(ggplot2)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mtcars")

mtcars$`car name` <- rownames(mtcars) # create new column for car names
mtcars$mpg_z <- round((mtcars$mpg - mean(mtcars$mpg)) / sd(mtcars$mpg), 2) # compute normalized mpg
mtcars$mpg_type <- ifelse(mtcars$mpg_z < 0, "below", "above") # above / below avg flag
mtcars <- mtcars[order(mtcars$mpg_z), ] # sort
mtcars$`car name` <- factor(mtcars$`car name`, levels = mtcars$`car name`) # convert to factor to retain sorted order in plot

# diverging lollipop chart
ggplot(mtcars, aes(x = `car name`, y = mpg_z, col = mpg_type)) + 
  geom_point(size = 6) + 
  geom_segment(aes(x = `car name`, xend = `car name`, y = 0, yend = mpg_z)) +
  geom_text(aes(label = mpg_z), color = "black", size = 2) +
  scale_color_manual(name = "Normalized mileage", 
                    values = c("above" = "lightgoldenrod3", "below" = "skyblue"),
                    labels = c("Above average", "Below average")) + 
  labs(title = "Diverging lollipop chart", 
       subtitle = "Normalized mileage from mtcars") + 
  ylim(-2.5, 2.5) + 
  coord_flip()
```

![](/public/img/2022-06-22-visualization-summary/diverging_lollipop_chart-1.png)