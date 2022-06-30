---
title: "R로 구현하는 분산형 막대 그래프"
categories: 시각화
tags: [R, ggplot2, 막대그래프]
---

<div style="margin-bottom:100px;"></div>

## 분산형 막대 그래프 (Diverging bar chart)

분산형 막대 그래프는 양수의 값과 음수의 값을 가지는 데이터를 시각화할 때 사용된다. `geom_bar()`에 몇 가지 요소를 추가하여 만들 수 있다. 그리고 아래에 나오는 두 가지 사항을 주의하자.

- `aes()` 안에 x와 y를 모두 넣어 줘야 하고 x 변수는 범주형 변수, y 변수는 연속형 변수
- `stat = "identity"`

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

# diverging bar chart
ggplot(mtcars, aes(x = `car name`, y = mpg_z)) + 
  geom_bar(aes(fill = mpg_type), stat = "identity", width = 0.5) + 
  scale_fill_manual(name = "Normalized mileage", 
                    values = c("above" = "lightgoldenrod3", "below" = "lavender"),
                    labels = c("Above average", "Below average")) + 
  labs(title = "Diverging bar chart", 
       subtitle = "Normalized mileage from mtcars") + 
  coord_flip()
```

![](/public/img/2022-06-22-visualization-summary/diverging_bar_chart-1.png)