---
title: "R로 구현하는 시각화 방법론 정리"
categories: 시각화
tags: [R, ggplot2]
---

<div style="margin-bottom:100px;"></div>

# 시각화를 해야 하는 이유

- 효과적인 정보 전달
- 정확한 분석을 위한 탐색적 데이터 분석

<div style="margin-bottom:100px;"></div>

# 효과적인 시각화란 무엇인가?

- 사실을 왜곡하지 않고 올바른 정보를 전달하는 것
- 단순하지만 필요한 정보가 모두 담겨있는 것
- 정보 전달의 목적을 해치지 않는 적절한 미적 요소를 추가하는 것
- 하나의 시각화에 정보가 과부하되지 않는 것

<div style="margin-bottom:100px;"></div>

# 여덟 가지의 대표적인 시각화 유형

1. 상관관계 (Correlation)
2. 편차 (Deviation)
3. 순위 (Ranking)
4. 분포 (Distribution)
5. 구성 (Composition)
6. 변화 (Change)
7. 군집 (Clustering)
8. 공간 (Spatial)

<div style="margin-bottom:100px;"></div>

# 상관관계 (Correlation)

두 수치형 변수의 상관관계를 파악하는 데 도움이 된다.

## 산점도 (Scatter plot)

**두 수치형 변수의 관계**를 살펴 보고자 할 때 가장 기본이 되는 도표는 산점도이다. 
`geom_point()`를 사용하여 기본적인 산점도를 그리고 `geom_smooth()`를 통해서 스무딩 선을 시각화할 수 있다.

```r
# load package and data
library(ggplot2)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("midwest", package = "ggplot2")

# scatter plot with smooth plot
ggplot(midwest, aes(x = area, y = poptotal)) + 
  geom_point() + 
  geom_smooth(method = "loess", se = FALSE) + 
  coord_cartesian(xlim = c(0, 0.1), ylim = c(0, 500000)) +
  labs(x = "area", 
       y = "population", 
       title = "Scatter plot", 
       subtitle = "area vs. population", 
       caption = "source: midwest")
```

![](/public/img/2022-06-22-visualization-summary/scatter_plot-1.png)

## 지터 플롯 (Jitter plot)

지터는 데이터 값에 약간의 노이즈를 추가하는 방법을 말한다. 지터로 산점도를 그리면 데이터 값이 조금 움직여서 같은 값을 가지는 데이터가 그래프에 겹쳐져 표시되지 않는다. `geom_point()`를 사용하는 대신 `geom_jitter()`를 사용하여 시각화할 수 있다. `geom_point()`와 `geom_jitter()` 둘 다 산점도를 그리지만 **겹쳐진 점을 표시하는 방법에 차이**가 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mpg", package = "ggplot2")

g <- ggplot(mpg, aes(cty, hwy))

# scatter plot
point <- g + geom_point() + 
  labs(title = "Scatter plot with overlapping points", 
       subtitle = "city vs. highway mileage")

# jitter plot
jitter <- g + geom_jitter(width = 0.5, size = 1) +
  labs(title = "Jittered scatter plot",
       subtitle = "city vs. highway mileage")

grid.arrange(point, jitter, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/jitter_plot-1.png)

## 버블 차트 (Bubble chart)

산점도로 두 수치형 변수 간의 관계를 파악할 수 있다. 버블 차트는 x축, y축의 변수 외에도 다음 변수들을 추가로 시각화할 수 있다.

- 색상을 통한 범주형 변수 
- 크기를 통한 수치형 변수

```r
# load package and data
library(ggplot2)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mpg", package = "ggplot2")

# prepare data
mpg_select <- mpg[mpg$manufacturer %in% c("audi", "ford", "honda", "hyundai"),]

# bubble chart
ggplot(mpg_select) +
  geom_jitter(aes(x = displ, y = cty, col = manufacturer, size = hwy)) +
  labs(title = "Bubble chart", 
       subtitle = "displacement vs. city mileage")
```

![](/public/img/2022-06-22-visualization-summary/bubble_chart-1.png)

## 상관관계 그래프 (Correlogram)

동일한 데이터 내에 존재하는 여러 개의 수치형 변수의 상관관계 표 형태로 확인할 수 있다. `ggcorplot` 패키지를 사용하여 편리하게 구현 가능하다.

```r
# load package and data
library(ggcorrplot)
data("mtcars")

# correlation matrix
corr_matrix <- round(cor(mtcars), 2)

# correlogram
ggcorrplot(corr_matrix, 
           hc.order = TRUE, 
           type = "lower", 
           lab = TRUE, 
           lab_size = 3, 
           method = "square", 
           colors = c("skyblue", "white", "lightpink"),
           title = "Correlogram of mtcars", 
           ggtheme = theme_bw)
```

![](/public/img/2022-06-22-visualization-summary/correlogram-1.png)

<div style="margin-bottom:200px;"></div>

# 편차 (Deviation)

고정된 값과 관련하여 여러 개의 범주형 변수 간의 차이를 비교 설명할 수 있다.

## 분산형 막대 그래프 (Diverging bar chart)

분산형 막대 그래프는 양수의 값과 음수의 값을 가지는 데이터를 시각화할 때 사용된다. `geom_bar()`에 몇 가지 요소를 추가하여 만들 수 있다. 그리고 아래에 나오는 두 가지 사항을 주의하자.

- `aes()` 안에 x와 y를 모두 넣어 줘야 하고 x 변수는 범주형 변수, y 변수는 수치형 변수
- `stat = "identity"`

```r
# load package and data
library(ggplot2)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mtcars")

# prepare data
mtcars$`car name` <- rownames(mtcars) # create new column for car names
mtcars$mpg_z <- round((mtcars$mpg - mean(mtcars$mpg)) / sd(mtcars$mpg), 2) # compute normalized mpg
mtcars$mpg_type <- ifelse(mtcars$mpg_z < 0, "below", "above") # above / below avg flag
mtcars <- mtcars[order(mtcars$mpg_z),] # sort
mtcars$`car name` <- factor(mtcars$`car name`, levels = mtcars$`car name`) # convert to factor to retain sorted order in plot

# diverging bar chart
ggplot(mtcars) + 
  geom_bar(aes(x = `car name`, y = mpg_z, fill = mpg_type), 
           stat = "identity", width = 0.5) + 
  scale_fill_manual(name = "Normalized mileage", 
                    values = c("above" = "lightgoldenrod3", "below" = "lavender"),
                    labels = c("Above average", "Below average")) + 
  labs(title = "Diverging bar chart", 
       subtitle = "Normalized mileage from mtcars") + 
  coord_flip() # flip axes
```

![](/public/img/2022-06-22-visualization-summary/diverging_bar_chart-1.png)

## 롤리팝 차트 (Diverging lollipop chart)

롤리팝 차트는 분산형 막대 그래프와 동일한 정보를 전달하지만 구체적으로 어떤 값을 가지는지 추가로 알 수 있다. `geom_point()`와 `geom_segment()`를 사용하여 시각화할 수 있다.

```r
# load package and data
library(ggplot2)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mtcars")

# prepare data
mtcars$`car name` <- rownames(mtcars) # create new column for car names
mtcars$mpg_z <- round((mtcars$mpg - mean(mtcars$mpg)) / sd(mtcars$mpg), 2) # compute normalized mpg
mtcars$mpg_type <- ifelse(mtcars$mpg_z < 0, "below", "above") # above / below avg flag
mtcars <- mtcars[order(mtcars$mpg_z), ] # sort
mtcars$`car name` <- factor(mtcars$`car name`, levels = mtcars$`car name`) # convert to factor to retain sorted order in plot

# diverging lollipop chart
ggplot(mtcars, aes(x = `car name`, y = mpg_z, col = mpg_type)) + 
  geom_point(size = 7) + 
  geom_segment(aes(x = `car name`, xend = `car name`, y = 0, yend = mpg_z)) +
  geom_text(aes(label = mpg_z), color = "black", size = 3) +
  scale_color_manual(name = "Normalized mileage", 
                    values = c("above" = "lightgoldenrod3", "below" = "skyblue"),
                    labels = c("Above average", "Below average")) + 
  ylim(-2.5, 2.5) + 
  labs(title = "Diverging lollipop chart", 
       subtitle = "Normalized mileage from mtcars") +
  coord_flip() # flip axes
```

![](/public/img/2022-06-22-visualization-summary/diverging_lollipop_chart-1.png)

<div style="margin-bottom:200px;"></div>

# 순위 (Ranking)

여러 항목의 위치 또는 성능을 서로 비교하는 데 사용되는 시각화 방법이다. 실제 값보다 항목간 순위 비교가 중요하다고 생각될 때 많이 쓰인다.

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

## 점 그래프 (Dot plot)

점 그래프는 순위 막대 그래프와 동일한 정보를 전달한다. 하지만 순위 막대 그래프와 정반대로 x축에는 수치형 변수, y축에는 범주형 변수가 들어간다. 점으로 시각화함으로서 **항목들이 서로 얼마나 멀리 떨어져 있는지가 강조**된다.

```r
# load package and data
library(dplyr)
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# dot plot
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mileage = mean(cty)) %>%
  ggplot() +
  geom_point(aes(reorder(x = manufacturer, -mileage), y = mileage), 
             col = "tomato2", size = 3) + # draw points
  geom_segment(aes(x = manufacturer, xend = manufacturer, 
                   y = min(mileage), yend = max(mileage)), 
               linetype = "dashed", size = 0.1) + # draw dashed lines 
  labs(x = "manufacturer",
       title = "Dot plot", 
       subtitle = "manufacturer vs. avg. mileage", 
       caption = "source: mpg") + 
  coord_flip() # flip axes
```

![](/public/img/2022-06-22-visualization-summary/dot_plot-1.png)

## 슬로프 차트 (Slope chart)

슬로프 차트는 두 시점에서 값의 증감을 기울기로 시각화하는 방법이다. `ggplot2`에는 슬로프 차트에 대한 내장 함수가 없기 때문에 아래와 같이 직접 커스터마이징해야 한다.

```r
# load package and data
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
df <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/gdppercap.csv")

# prepare data
colnames(df) <- c("continent", "1952", "1957")
left_label <- paste(df$continent, round(df$`1952`), sep = ", ")
right_label <- paste(df$continent, round(df$`1957`), sep = ", ")
df$class <- ifelse((df$`1957` - df$`1952`) < 0, "Down", "Up")

# slope chart
p <- ggplot(df) + 
  geom_segment(aes(x = 1, xend = 2, 
                   y = `1952`, yend = `1957`, 
                   col = class),
               size = 0.75, show.legend = FALSE) + 
  geom_vline(xintercept = 1, linetype = "dashed", size = 0.1) + 
  geom_vline(xintercept = 2, linetype = "dashed", size = 0.1) + 
  scale_color_manual(values = c("Up" = "#00ba38", "Down" = "#f8766d")) + # color of lines 
    coord_cartesian(xlim = c(0.5, 02.5), 
                  ylim = c(0, 1.1 * max(df$`1952`, df$`1957`))) +
  labs(x = "", y = "mean GDP", title = "mean GDP per capita")


# add texts
p <- p + geom_text(label = left_label, y = df$`1952`, x = rep(1, nrow(df)), hjust = 1.1, size = 3.5) 
p <- p + geom_text(label = right_label, y = df$`1957`, x = rep(2, nrow(df)), hjust = -0.1, size = 3.5) 
p <- p + geom_text(label = "Time 1(1952)", x = 1, y = 1.1 * max(df$`1952`, df$`1957`), hjust = 1.2, size = 4) # title 
p <- p + geom_text(label = "Time 2(1957)", x = 2, y = 1.1 * max(df$`1952`, df$`1957`), hjust = -0.1, size = 4) # title 

# simplify theme
p + theme(panel.grid = element_blank(), 
          axis.ticks = element_blank(),
          axis.text.x = element_blank())
```

![](/public/img/2022-06-22-visualization-summary/slope_chart-1.png)

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

# prepare data
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

<div style="margin-bottom:200px;"></div>

# 분포 (Distribution)

많은 데이터 포인트가 존재할 때, 데이터 포인트가 어디에 어떻게 분포되어 있는지 파악하고 싶을 때 사용된다.

## 히스토그램 (Histogram)

히스토그램은 **도수분포표를 그래프로 시각화**한 것이다. 즉, 수치형 변수에 대해서 구간별 빈도 수를 보여준다. `geom_histogram()`을 통해서 구현할 수 있으며 `bins` 혹은 `binwidth`를 통해 구간의 범위를 조정할 수 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# histogram
g <- ggplot(mpg, aes(x = hwy, fill = class)) + 
  scale_fill_brewer(palette = "BrBG")

hist_binwidth <- g + geom_histogram(binwidth = 2, col = "black", size = 0.1) + # set width of bin
  labs(title = "Histogram with auto binning", 
       subtitle = "Highway mileage across vehicle classes")

hist_bins <- g + geom_histogram(bins = 8, col = "black", size = 0.1) + # set number of bins 
  labs(title = "Histogram with fixed bins", 
       subtitle = "Highway mileage across vehicle classes")

grid.arrange(hist_binwidth, hist_bins, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/histogram-1.png)

## 밀도 그래프 (Density plot)

히스토그램은 막대를 그리는 구간인 bin의 개수 혹은 너비를 어떻게 잡는지에 따라 전혀 다른 모양이 될 수 있다. `goem_density()`로 시각화할 수 있는 밀도 그래프는 막대의 너비를 가정하지 않고 **모든 점에서 데이터의 밀도, 즉 확률밀도함수를 추정**한다.

```r
# load package and data
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# density plot
ggplot(mpg) + 
  geom_density(aes(x = cty, fill = factor(cyl)), alpha = 0.8) + 
  labs(x = "city mileage",
       title = "Density plot", 
       subtitle = "City mileage grouped by number of cylinders", 
       fill = "# cylinders",
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/density_plot-1.png)

## 상자 그림 (Box plot)

상자 그림은 (min, Q1, Q2, Q3, max)인 **다섯가지 요약 수치를 시각화**하는 방법이다. 또한, 이상치(있는 경우)를 알 수 있다. `geom_boxplot()`을 사용하여 시각화하고 `varwidth = TRUE`는 상자의 너비가 데이터 수에 비례하도록 조정하는 기능을 한다.

```r
# load package and data
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# box plot
ggplot(mpg) + 
  geom_boxplot(aes(x = class, y = hwy), varwidth = TRUE, fill = "olivedrab4") + 
  labs(x = "class of vehicle", 
       y = "highway mileage",
       title = "Box plot", 
       subtitle = "Highway mileage grouped by class of vehicle", 
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/box_plot-1.png)

## 바이올린 플롯 (Violin plot)

바이올린 플롯은 다섯가지 요약 수치를 보여주는 상자 그림과 다르게 **그룹별 밀도**를 보여준다. 그룹이 많은 경우, 바이올린 플롯이 밀도 그래프보다 그룹간 밀도를 비교하기 쉽다. `geom_violin()`을 사용하여 시각화할 수 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("mpg", package = "ggplot2")

# violin plot
violin <- ggplot(mpg) + 
  geom_violin(aes(x = class, y = hwy), fill = "mediumseagreen") + 
  labs(x = "class of vehicle", 
       y = "highway mileage",
       title = "Violin plot", 
       subtitle = "highway mileage vs. class of vehicle", 
       caption = "source: mpg")

# density plot
density <- ggplot(mpg) + 
  geom_density(aes(x = hwy, fill = class), alpha = 0.8) + 
  labs(x = "city mileage",
       title = "Density plot", 
       subtitle = "highway mileage vs. class of vehicle", 
       fill = "class of vehicle",
       caption = "source: mpg")

grid.arrange(violin, density, nrow = 2)
```

![](/public/img/2022-06-22-visualization-summary/violin_plot-1.png)

## 인구 피라미드 (Population pyramid)

인구 피라미드는 **특정 범주에 속하는 인구 수 또는 인구 비율을 시각화**하는 방법이다. `geom_bar()`를 변형시켜서 구현할 수 있다. 아래는 이메일 마케팅 캠페인의 각 단계에서 유지되는 사용자 수에 대한 예시다.

```r
# load package and data
library(ggplot2)
library(ggthemes)
theme_set(theme_tufte()) # no border, no axis lines, no grids
email_campaign_funnel <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/email_campaign_funnel.csv")

# x axis breaks and labels
brks <- seq(-15000000, 15000000, 5000000)
lbls <- paste0(as.character(c(seq(15, 0, -5), seq(5, 15, 5))), "m") 

# population pyramid
ggplot(email_campaign_funnel) +
  geom_bar(aes(x = Stage, y = Users, fill = Gender), stat = "identity", width = 0.6) + # draw the bars 
  scale_fill_brewer(palette = "Dark2") + # color palette
  scale_y_continuous(breaks = brks, labels = lbls) + # breaks and labels
  theme(plot.title = element_text(hjust = 0.5), # center the plot title
        axis.ticks = element_blank()) +
  labs(title = "Email campaign funnel") +
  coord_flip() # flip axes 
```

![](/public/img/2022-06-22-visualization-summary/population_pyramid-1.png)

<div style="margin-bottom:200px;"></div>

# 구성 (Composition)

여러 개의 범주가 전체에서 차지하는 비중이 얼마나 되는지를 표현하고 싶을 때 사용할 수 있는 시각화 방법이다.

## 막대 그래프 (Bar chart)

**범주별 수치를 시각화**하는 가장 기본적인 그래프로 `geom_bar()`로 구현할 수 있다. 그리고 아래에 나오는 두 가지 사항을 주의하자.

- x축은 범주형 변수, y축은 수치형 변수로 설정
- `stat = "identity"`로 설정

```r
# load package and data
library(dplyr)
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# bar chart 
mpg %>% 
  group_by(manufacturer, class) %>% 
  summarise(N = n()) %>% 
  ggplot() + 
  geom_bar(aes(x = manufacturer, y = N, fill = class), 
           stat = "identity", width = 0.5) + 
  theme(axis.text.x = element_text(angle = 65, vjust = 0.6)) + 
  labs(title = "Category wise bar chart", 
       subtitle = "Manufacturer of vehicles")
```

![](/public/img/2022-06-22-visualization-summary/bar_chart-1.png)

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

## 원형 차트 (Pie chart)

원형 차트는 정보 전달의 관점에서 와플 차트와 거의 동일하다. `geom_bar()`와 `coord_polar()`을 사용하여 구현할 수 있다.

```r
# load package and data
library(dplyr)
library(forcats)
library(ggplot2)
library(ggrepel)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("mpg", package = "ggplot2")

# prepare data
df <- mpg %>% 
  group_by(class) %>% 
  summarize(cnt = n()) %>% 
  mutate(prop = round((cnt/sum(cnt)) * 100, 1)) %>% 
  arrange(prop)

text_df <- df %>% 
    mutate(csum = rev(cumsum(rev(prop))), 
         pos = prop/2 + lead(csum, 1),
         pos = if_else(is.na(pos), prop/2, pos))

# pie chart
ggplot(df, aes(x = "", y = prop, fill = fct_inorder(class))) +
  geom_bar(color = "black", stat = "identity") +
  coord_polar(theta = "y", start = 0) +
  geom_label_repel(data = text_df,
                   aes(y = pos, label = paste0(prop, "%")),
                   size = 4.5, nudge_x = 1, show.legend = FALSE) +
  scale_fill_brewer(palette = "Pastel1") +
  guides(fill = guide_legend(reverse = TRUE)) +
  theme(axis.line = element_blank(), 
        axis.text = element_blank(), 
        plot.title = element_text(hjust = 0.5)) +
  labs(x = "", 
       y = "", 
       title = "Pie chart of class", 
       fill = "class")
```

![](/public/img/2022-06-22-visualization-summary/pie_chart-1.png)

## 트리맵 (Tree map)

트리맵은 **계층 구조를 가진 데이터를 시각화**하는 좋은 방법이다. 계층적으로 사각형의 넓이를 다르게 하여 구성을 표현한다. `treemapify` 패키지의 `geom_treemap()`과 `geom_treemap_text()`를 사용하여 구현할 수 있다. 고려해야 할 중요 사항은 다음과 같다.

- 트리맵의 영역(넓이)을 나타내는 변수가 존재해야 한다. (`area`, `label`)
- 트리맵 안의 색을 채울 수 있는 변수가 존재해야 한다. (`fill`)
- 각 트리들을 묶을 수 있는 부모 그룹이 존재해야 한다. (`subgroup`)

```r
# load package and data
library(ggplot2)
library(treemapify)
proglangs <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/proglanguages.csv")

# treemap
ggplot(proglangs, aes(area = value, 
                      label = id,
                      fill = parent, 
                      subgroup = parent)) + 
  geom_treemap() + 
  geom_treemap_text() + 
  scale_fill_brewer(palette = "Dark2")
```

![](/public/img/2022-06-22-visualization-summary/treemap-1.png)

<div style="margin-bottom:200px;"></div>

# 변화 (Change)

## 영역 차트 (Area chart)

영역 차트는 꺾은 선 그래프(line graph)를 그린 후 꺾은 선과 x축 사이의 영역을 채우는 시각화 방법이다. `geom_area()`를 사용하여 구현할 수 있다.

```r
# load package and data
library(ggplot2)
library(lubridate)
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("economics", package = "ggplot2")

# compute percent returns
economics$returns_percent <- c(0, diff(economics$psavert)/economics$psavert[-length(economics$psavert)])

# create break points and labels for axis ticks
brks <- economics$date[seq(1, length(economics$date), 12)]
lbls <- year(economics$date[seq(1, length(economics$date), 12)])

# area chart
ggplot(economics[1:50,]) +
  geom_area(aes(x = date, y = returns_percent)) + 
  scale_x_date(breaks = brks, labels = lbls) +
  labs(y = "returns %",
       title = "Area chart", 
       subtitle = "Perent returns for personal savings",
       caption = "source: economics")
```

![](/public/img/2022-06-22-visualization-summary/area_chart-1.png)

## 시계열 그래프 (Time series plot)

**시간의 흐름에 따른 특정 값의 변화**를 표현할 때 주로 활용된다. 

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

시각화하고자 하는 대상이 시계열 객체가 아닌 데이터프레임 형태일때 `geom_line()`을 사용하여 시계열 그래프로 표현할 수 있다.

```r
# load package and data
library(ggplot2)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
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

## 캘린더 히트맵 (Calender heatmap)

캘린더 히트맵은 **많은 양의 시계열 값의 변동을 색으로 시각화**하는 방법이다. 주가의 변동을 확인할 때 캘린더 히트 맵이 훌륭한 도구가 된다. 실제 값 자체보다는 시간에 따른 값의 변화를 색으로 강조한다. `geom_tile()`과 `facet_grid()`를 통해 구현할 수 있지만 그 전에 캘린더 히트맵에 맞는 데이터의 형태를 갖추는 것이 더욱 중요한 작업이다.

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

## 계절성 차트 (Seasonal plot)

`forecast` 패키지의 `ggseasonplot()`를 사용하면 시계열 객체(ts)를 대상으로 연도별 시계열 그래프를 표현할 수 있다.

```r
# load package and data
library(forecast)
library(ggplot2)
library(gridExtra)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("nottem")
data("AirPassengers")

# subset data 
nottem_small <- window(nottem, start = c(1920, 1), end = c(1925, 12)) # subset a smaller time window 

# seasonal plot 
airpassenger <- ggseasonplot(AirPassengers)
nottem <- ggseasonplot(nottem_small)

grid.arrange(airpassenger, nottem, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/seasonal_plot-1.png)

<div style="margin-bottom:200px;"></div>

# 군집 (Clustering)

군집 분석은 소속 집단을 모르는(unlabeled) 데이터들을 서로 동질적인 집단으로 분류하는 방법이다. 데이터 사이의 유사성에 근거하여 한 군집 안에 있는 데이터들은 유사하고, 다른 군집에 있는 데이터와는 서로 다르게 군집을 형성한다. 초기 데이터를 탐색할 때에도 매우 유용한 시각화 방법 중 하나이다.

## 계층적 덴드로그램 (Hierarchical dendrogram)

계층적 군집 분석은 각 개체 하나하나를 군집으로 두고 매 단계에서 가장 근접한 2개의 군집들을 하나의 군집으로 병합하는 방법을 말한다. 이러한 군집화 과정을 간략하게 표현한 도표가 바로 덴드로그램이다. `hclust()`를 통해 계층적 군집 분석을 수행하고 `ggdendro` 패키지의 `ggdendrogram()`을 통해 계층적 덴드로그램을 시각화할 수 있다.

```r
# load package and data
library(ggplot2) 
library(ggdendro) 
theme_set(theme_bw()) # set the classic dark-on-light ggplot2 theme
data("USArrests")

hc <- hclust(dist(USArrests), method = "average") # hierarchical clustering 

# hierarchical dendrogram
ggdendrogram(hc, rotate = TRUE, size = 2)
```

![](/public/img/2022-06-22-visualization-summary/hierarchical_dendrogram-1.png)

## 비계층적 군집 분석 (Non-hierarchical clustering)

분할 군집으로도 불리는 비계층적 군집 분석에서는 먼저 군집의 개수 K를 정한 후 데이터를 무작위로 K개의 군집으로 배정한다. 그리고 배정된 군집의 중심으로부터의 거리를 계산한다. 가장 가까운 중심으로 군집을 다시 배정한다. 그러한 과정을 군집이 더 이상 변하지 않을 때까지 반복한다. 군집이 설정된 후, 데이터의 변수가 많을 경우에는 주성분인 PC1과 PC2를 x축과 y축으로 사용하여 산점도로 표현한다. `ggalt` 패키지의 `geom_encircle()`을 사용하면 각 그룹을 구분하여 시각화할 수 있다.

```r
# load package and data
library(ggplot2)
library(ggalt)
theme_set(theme_classic()) # set a classic-looking theme, with x and y axis lines and no grid lines
data("iris")

# compute data with principal components
df <- iris[c(1, 2, 3, 4)]
pca_mod <- prcomp(df, center = TRUE) # compute principal components

# dataframe of principal components
df_pc <- data.frame(pca_mod$x, Species = iris$Species) # dataframe of principal components 
df_pc_vir <- df_pc[df_pc$Species == "virginica",]  # df for 'virginica'
df_pc_set <- df_pc[df_pc$Species == "setosa",]     # df for 'setosa'
df_pc_ver <- df_pc[df_pc$Species == "versicolor",] # df for 'versicolor' 

# clustering
ggplot(df_pc, aes(x = PC1, y = PC2, col = Species)) +
  geom_point(aes(shape = Species), size = 2) + # draw points
  labs(title = "Iris clustering", 
       subtitle = "With principal components PC1 and PC2 as x and y axis", 
       caption = "source: iris") + 
  coord_cartesian(xlim = 1.2 * c(min(df_pc$PC1), max(df_pc$PC1)), 
                  ylim = 1.2 * c(min(df_pc$PC2), max(df_pc$PC2))) + # change axis limits 
  geom_encircle(data = df_pc_vir) + # draw circles 
  geom_encircle(data = df_pc_set) +
  geom_encircle(data = df_pc_ver)
```

![](/public/img/2022-06-22-visualization-summary/clustering-1.png)

<div style="margin-bottom:100px;"></div>

# 공간 (Spatial)

## 구글 맵 (Google map)

`ggmap` 패키지는 Google 지도 API와 상호 작용하여 구글 맵에 있는 장소의 좌표(위도 및 경도)를 얻는 기능을 제공한다. `geocode()`를 통해서 장소의 좌표를 얻을 수 있고 `qmap()`을 통해서 지도를 불러들일 수 있다. 가져 올 지도의 유형은 `maptype` 값을 어떻게 설정하는지에 따라서 달라진다. `zoom` 기능을 통해서 지도를 확대 혹은 축소할 수 있다(기본값은 10이고 3부터 21까지 가능하다).

```r
# load package and data
library(ggplot2) 
library(ggmap) 
library(ggalt) 

# google API register
register_google(key = "AIzaSyBjDkoYysOVCCGK-evX8uq2CSv-Q33V1hI") # type your api key

# get Seoul's coordinates 
seoul <- geocode("seoul") # get longitude and latitude 

# get the map
seoul_ggl_sat_map <- qmap("seoul", zoom = 12, source = "google", maptype = "satellite") # Google Satellite Map
seoul_ggl_road_map <- qmap("seoul", zoom = 12, source = "google", maptype = "roadmap") # Google Road Map
seoul_ggl_hybrid_map <- qmap("seoul", zoom = 12, source = "google", maptype = "hybrid") # Google Hybrid Map

seoul_places <- c("성신여자대학교", "성균관대학교", "연세대학교", "이화여자대학교", "홍익대학교") 
places_loc <- geocode(seoul_places) # get longitudes and latitudes 
places_loc$place <- seoul_places

# plot Google Road Map
seoul_ggl_road_map + 
  geom_point(aes(x = lon, y = lat), 
             data = places_loc, 
             alpha = 0.7, 
             size = 7, 
             color = "tomato") + 
  geom_text(aes(label = place), data = places_loc) + 
  geom_encircle(aes(x = lon, y = lat), 
                data = places_loc, 
                size = 2, 
                color = "blue")
```

![](/public/img/2022-06-22-visualization-summary/spatial1-1.png)

```r
# plot Google Hybrid Map
seoul_ggl_hybrid_map + 
  geom_point(aes(x = lon, y = lat), 
             data = places_loc, 
             alpha = 0.7, 
             size = 7, 
             color = "tomato") + 
  geom_text(aes(label = place), 
            data = places_loc, 
            colour = "white", 
            fontface = "bold") + 
  geom_encircle(aes(x = lon, y = lat), 
                data = places_loc, 
                size = 2, 
                color = "blue")
```

![](/public/img/2022-06-22-visualization-summary/spatial2-1.png)