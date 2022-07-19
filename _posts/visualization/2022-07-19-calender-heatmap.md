---
title: "R로 구현하는 캘린더 히트맵"
categories: 시각화
tags: [R, ggplot2, 캘린더 히트맵]
---

<div style="margin-bottom:100px;"></div>

## 캘린더 히트맵 (Calender heatmap)

캘린더 히트맵은 많은 양의 시계열 값의 변동을 색으로 시각화하는 방법이다. 주가의 변동을 확인할 때 캘린더 히트 맵이 훌륭한 도구가 된다. 실제 값 자체보다는 시간에 따른 값의 변화를 색으로 강조한다. `geom_tile()`과 `facet_grid()`를 통해 구현할 수 있지만 그 전에 캘린더 히트맵에 맞는 데이터의 형태를 갖추는 것이 더욱 중요한 작업이다.

```r
# load package and data
library(plyr)
library(ggplot2)
library(zoo)
df <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/yahoo.csv")

# prepare data
df$date <- as.Date(df$date)
df <- df[df$year >= 2012,]
df$weekdayf <- factor(df$weekdayf, levels = c("Mon", "Tue", "Wed", "Thu", "Fri"))
df$monthf <- factor(df$monthf, levels = c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
df$yearmonth <- as.yearmon(df$date) # compute year and month
df <- ddply(df, .(yearmonth), transform, monthweek = 1 + week - min(week)) # compute week number of month

# calender heatmap
ggplot(df) + 
  geom_tile(aes(x = monthweek, y = weekdayf, fill = VIX.Close), color = "white") + 
  facet_grid(year ~ monthf) + 
  scale_fill_gradient(low = "blue", high = "red") + 
  labs(x = "week of month", 
       y = "", 
       title = "Calendar heatmap", 
       subtitle = "Yahoo closing price", 
       fill = "closing price")
```

![](/public/img/2022-06-22-visualization-summary/calender_heatmap-1.png)