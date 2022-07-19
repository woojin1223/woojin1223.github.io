---
title: "R로 구현하는 인구 피라미드"
categories: 시각화
tags: [R, ggplot2, 인구 피라미드]
---

<div style="margin-bottom:100px;"></div>

## 인구 피라미드 (Population pyramid)

인구 피라미드는 특정 범주에 속하는 인구 수 또는 인구 비율을 시각화하는 방법이다. `geom_bar()`를 변형시켜서 구현할 수 있다. 아래는 이메일 마케팅 캠페인의 각 단계에서 유지되는 사용자 수에 대한 예시다.

```r
# load package and data
library(ggplot2)
library(ggthemes)
theme_set(theme_tufte()) # no border, no axis lines, no grids
email_campaign_funnel <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/email_campaign_funnel.csv")

# x axis breaks and labels
brks <- seq(-15000000, 15000000, 5000000)
lbls = paste0(as.character(c(seq(15, 0, -5), seq(5, 15, 5))), "m") 

# population pyramid
ggplot(email_campaign_funnel) +
  geom_bar(aes(x = Stage, y = Users, fill = Gender), stat = "identity", width = 0.6) + # draw the bars 
  scale_y_continuous(breaks = brks, labels = lbls) + # breaks and labels
  coord_flip() + # flip axes 
  labs(title = "Email campaign funnel") + 
  theme(plot.title = element_text(hjust = 0.5), # center plot title
        axis.ticks = element_blank()) + 
  scale_fill_brewer(palette = "Dark2") # color palette
```

![](/public/img/2022-06-22-visualization-summary/population_pyramid-1.png)