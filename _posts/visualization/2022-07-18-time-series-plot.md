---
title: "R로 구현하는 시계열 그래프"
categories: 시각화
tags: [R, ggplot2, 시계열그래프]
---

<div style="margin-bottom:100px;"></div>

## 시계열 그래프 (Time series plot)

시간의 흐름에 따른 특정 값의 변화를 표현할 때 주로 활용된다. 

### Time series plot from a time series object (ts)

`ggfortify` 패키지를 사용하면 자동으로 시계열 객체(ts)를 시계열 그래프로 표현할 수 있다.

```r
# load package and data
library(ggplot2)
library(ggfortify)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("AirPassengers")

autoplot(AirPassengers) + 
  labs(title = "Air passengers") + 
  theme(plot.title = element_text(hjust = 0.5))
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_ts-1.png)

### Time series plot from a time dataframe

시각화하고자 하는 대상이 시계열 객체가 아닌 데이터프레임 형태일때에는 `geom_line()`을 사용하여 시계열 그래프로 표현할 수 있다.

```r
# load package and data
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no
data("economics", package = "ggplot2")

# compute percent returns
economics$returns_percent <- c(0, diff(economics$psavert)/economics$psavert[-length(economics$psavert)])

ggplot(economics) + 
  geom_line(aes(x = date, y = returns_percent)) + 
  labs(y = "returns %",
       title = "Time series plot",
       subtitle = "Returns percentage", 
       caption = "source: economics")
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_df-1.png)

### Time series plot for a yearly or monthly time series

`scale_x_date()`로 x축을 원하는 시간 간격으로 설정할 수 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
library(lubridate)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("economics", package = "ggplot2")

# compute percent returns
economics$returns_percent <- c(0, diff(economics$psavert)/economics$psavert[-length(economics$psavert)])

# prepare data
economics_m <- economics[1:24,] 
economics_y <- economics[1:90,]

# labels and breaks for x axis text
m_lbls <- paste0(month.abb[month(economics_m$date)], " ", year(economics_m$date)) 
m_brks <- economics_m$date 

# monthly time series plot
monthly <- ggplot(economics_m) + 
  geom_line(aes(x = date, y = returns_percent)) + 
  scale_x_date(labels = m_lbls, breaks = m_brks) + # change to monthly ticks and labels
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5), # rotate x axis text
        panel.grid.minor = element_blank()) + # turn off minor grid
  labs(y = "returns %", title = "Monthly time series")

# labels and breaks for x axis text
y_brks <- economics_y$date[seq(1, length(economics_y$date), 12)]
y_lbls <- year(y_brks)

# yearly time series 
yearly <- ggplot(economics_y) + 
  geom_line(aes(x = date, y = returns_percent)) +
  scale_x_date(labels = y_lbls, breaks = y_brks) + # change to monthly ticks and labels
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5), # rotate x axis text
        panel.grid.minor = element_blank()) + # turn off minor grid
  labs(y = "returns %", title = "Yearly time series")

grid.arrange(monthly, yearly, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_ym-1.png)

### Time series plot from a multiple columns of dataframe

두 개 이상의 그룹별 시계열 그래프를 시각화하고 싶을 때 `geom_line()` 안의 `aes()`의 `col` 인자를 설정하면 된다.

```r
# load package and data
library(ggplot2)
library(lubridate)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("economics_long")

# prepare data
df <- economics_long[economics_long$variable %in% c("psavert", "uempmed"), ] 
df <- df[year(df$date) %in% c(1967:1981),] 

# labels and breaks for x axis text 
brks <- df$date[seq(1, length(df$date), 12)] 
lbls <- year(brks) 

# time series plot 
ggplot(df) + 
  geom_line(aes(x = date, y = value, col = variable)) +
  scale_x_date(labels = lbls, breaks = brks) + # change to monthly ticks and labels 
  scale_color_manual(values = c("psavert" = "#00ba38", "uempmed" = "#f8766d")) + # line color 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, size = 8), # rotate x axis text 
        panel.grid.minor = element_blank()) + # turn off minor grid 
  labs(y = "returns %", 
       title = "Time series of returns percentage",
       caption = "source: economics", 
       color = NULL)
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_mc-1.png)
