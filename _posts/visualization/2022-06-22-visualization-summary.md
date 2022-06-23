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
- 하나의 시각화에 정보가 과부하 되지 않는 것

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

두 변수 사이의 관계 특성을 이해하고자 할 때마다 항상 첫 번째로 떠올릴 수 있는 것은 산점도다.
`geom_point()`를 사용하여 기본적인 산점도를 그리고 `geom_smooth()`를 통해서 스무딩 선을 표현할 수 있다.

```r
options(scipen = 999) # turn-off scientific notation like 1e+48
library(ggplot2)
theme_set(theme_bw()) # pre-set the bw theme.
data("midwest", package = "ggplot2")

# scatter plot with smooth plot
ggplot(midwest, aes(x = area, y = poptotal)) + 
  geom_point(aes(col = state, size = popdensity)) + 
  geom_smooth(method = "loess", se = FALSE) + 
  coord_cartesian(xlim = c(0, 0.1), ylim = c(0, 500000)) +
  labs(x = "area", 
       y = "population", 
       title = "Scatterplot", 
       subtitle = "Area vs. population", 
       caption = "source: midwest")
```

![](/public/img/2022-06-22-visualization-summary/scatter_plot-1.png)

## 지터 플롯 (Jitter plot)

지터는 데이터 값에 약간의 노이즈를 추가하는 방법을 말한다. 노이즈를 추가하면 데이터 값이 조금씩 움직여서 같은 값을 가지는 데이터가 그래프에 여러 번 겹쳐셔 표시되는 현상을 막아준다. `geom_jitter()`를 이용하여 시각화할 수 있다. `geom_point()`와 `geom_jitter()` 둘 다 산점도라는 점에서 공통점이 있지만 점을 어느 위치에 출력하는지에서 차이가 있다.

```r
# load package and data
library(ggplot2)
library(gridExtra)
theme_set(theme_bw()) # pre-set the bw theme.
data(mpg, package = "ggplot2")

g <- ggplot(mpg, aes(cty, hwy))

# scatter plot
point <- g + geom_point() + 
  labs(title = "Scatterplot with overlapping points", 
       subtitle = "City vs. highway mileage")

# jitter plot
jitter <- g + geom_jitter(width = 0.5, size = 1) +
  labs(title = "Jittered points",
       subtitle = "City vs. highway mileage")

grid.arrange(point, jitter, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/jitter_plot-1.png)

## 버블 차트 (Bubble chart)

산점도를 사용하면 두 개의 연속형 변수 간의 관계를 비교할 수 있지만 버블 차트는 x축, y축의 연속형 변수 이외에도 다음 변수들의 관계를 파악할 수 있다.

- 범주형 변수를 통한 색상 표시
- 연속형 변수를 통한 크기 표시

```r
# load package and data
library(ggplot2)
theme_set(theme_bw()) # pre-set the bw theme.
data(mpg, package = "ggplot2")
mpg_select <- mpg[mpg$manufacturer %in% c("audi", "ford", "honda", "hyundai"),]

# bubble chart
ggplot(mpg_select, aes(displ, cty)) +
  geom_jitter(aes(col = manufacturer, size = hwy)) +
  labs(title = "Bubble chart", 
       subtitle = "Displacement vs. city mileage")
```

![](/public/img/2022-06-22-visualization-summary/bubble_chart-1.png)

## 상관 관계 그래프 (Correlogram)

동일한 데이터 내에 존재하는 여러 개의 연속형 변수의 상관 관계를 확인할 수 있다. `ggcorplot` 패키지를 사용하여 편리하게 구현 가능하다.

```r
library(ggcorrplot)
library(ggplot2)
data(mtcars)

# correlation matrix
corr_matrix <- round(cor(mtcars), 1)

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

<div style="margin-bottom:100px;"></div>

# 편차 (Deviation)

고정된 값과 관련하여 여러 개의 범주형 변수 간의 차이를 비교 설명할 수 있다.

## 갈라지는 막대 그래프 (Diverging bar chart)

양수의 값과 음수의 값 모두 가질 수 있다. 기본적으로 `geom_bar()`에 몇 가지 요소를 추가하면 만들 수 있다. 아래에 나오는 두 가지 사항을 주의하자.

- `aes()` 안에 x와 y를 모두 넣어 줘야 하고 x 변수는 범주형 변수, y 변수는 연속형 변수여야 한다.
- `stat = "identity"`

```r
# load package and data
library(ggplot2)
theme_set(theme_bw())
data("mtcars")

mtcars$`car name` <- rownames(mtcars) # create new column for car names
mtcars$mpg_z <- round((mtcars$mpg - mean(mtcars$mpg)) / sd(mtcars$mpg), 2) # compute normalized mpg
mtcars$mpg_type <- ifelse(mtcars$mpg_z < 0, "below", "above") # above / below avg flag
mtcars <- mtcars[order(mtcars$mpg_z), ] # sort
mtcars$`car name` <- factor(mtcars$`car name`, levels = mtcars$`car name`) # convert to factor to retain sorted order in plot.

# diverging bar chart
ggplot(mtcars, aes(x = `car name`, y = mpg_z, label = mpg_z)) + 
  geom_bar(aes(fill = mpg_type), stat = "identity", width = 0.5) + 
  scale_fill_manual(name = "Mileage", labels = c("Above Average", "Below Average"), values = c("above" = "lightgoldenrod3", "below" = "lavender")) + 
  labs(title = "Diverging bar chart", subtitle = "Normalized mileage from mtcars") + 
  coord_flip()
```

![](/public/img/2022-06-22-visualization-summary/diverging_bar_chart-1.png)

## 롤리팝 차트 (Diverging lollipop chart)

모양이 좀 더 모던한 것을 제외하고, 위의 diverging bar chart와 거의 동일한 정보 전달의 기능을 수행한다. `geom_point()`와 `geom_segment()`를 사용하여 표현할 수 있다.

```r
# diverging lollipop chart
ggplot(mtcars, aes(x = `car name`, y = mpg_z, label = mpg_z)) + 
  geom_point(stat = "identity", fill = "black", size = 8) + 
  geom_segment(aes(x = `car name`, xend = `car name`, y = 0, yend = mpg_z), color = "black") +
  geom_text(color = "white", size = 3) +
  labs(title = "Diverging lollipop chart", subtitle = "Normalized mileage from mtcars") + 
  ylim(-2.5, 2.5) + 
  coord_flip()
```

![](/public/img/2022-06-22-visualization-summary/diverging_lollipop_chart-1.png)

## 영역 차트 (Area chart)

영역 차트는 일반적으로 특정 기준과 비교하여 특정 지표(예: 주식의 수익률)가 수행되는 방식을 시각화하는 데 사용된다. `geom_area()`를 사용한다.

```r
# load package and data
library(ggplot2)
library(quantmod)
library(lubridate)
data("economics", package = "ggplot2")

# compute percent returns
economics$returns_perc <- c(0, diff(economics$psavert)/economics$psavert[-length(economics$psavert)])

# create break points and labels for axis ticks
brks <- economics$date[seq(1, length(economics$date), 12)]
lbls <- year(economics$date[seq(1, length(economics$date), 12)])

# area chart
ggplot(economics[1:100,], aes(x = date, y = returns_perc)) +
  geom_area() + 
  scale_x_date(breaks = brks, labels = lbls) +
  theme(axis.text.x = element_text(angle = 90)) +
  labs(y = "percent returns",
       title = "Area chart", 
       subtitle = "Perent returns for personal savings",
       caption = "source: economics")
```

![](/public/img/2022-06-22-visualization-summary/area_chart-1.png)

<div style="margin-bottom:100px;"></div>

# 순위 (Ranking)

여러 항목의 위치 또는 성능을 서로 비교하는 데 사용되는 시각화 방법이다. 실제 값보다 항목간 순위 비교가 중요하다고 생각될 때 많이 쓰인다.

## 순위 막대그래프 (Ordered bar chart)

순위 막대 그래프는 y축 변수에 의해 순서가 지정된 막대그래프라고 생각하면 된다. 다음과 같은 변수들의 순위를 표현할 때 유용하다고 볼 수 있다. `aes()` 내에서 축을 지정할 때 `reorder()`를 사용하면 된다.

- x축이 범주형 변수 일 때
- y축이 연속형 변수이고 이를 기준으로 정렬하고 싶을 때

```r
library(dplyr)
library(ggplot2)
theme_set(theme_bw()) 

# ordered bar chart
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mileage = mean(cty)) %>% 
  ggplot(aes(reorder(x = manufacturer, -mileage), y = mileage)) +
  geom_bar(stat = "identity", width = 0.5, fill = "tomato3") + 
  labs(x = "manufacturer",
       title = "Ordered bar chart", 
       subtitle = "manufacturer vs. avg. mileage", 
       caption = "source: mpg") + 
  theme(axis.text.x = element_text(angle = 65, vjust = 0.6))
```

![](/public/img/2022-06-22-visualization-summary/ordered_bar_chart-1.png)

## 점 그래프 (Dot plot)

점 그래프는 순위 막대그래프와 매우 유사하지만 선이없고 수평 위치로 뒤집힌다. 실제 값과 관련하여 항목간 서로 얼마나 멀리 떨어져 있는지에 대해 더 강조된다.

```r
library(ggplot2)
library(scales)
theme_set(theme_classic())

# dot plot
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mileage = mean(cty)) %>%
  ggplot(aes(reorder(x = manufacturer, -mileage), y = mileage)) +
  geom_point(col = "tomato2", size = 3) + # Draw points
  geom_segment(aes(x = manufacturer, 
                   xend = manufacturer, 
                   y = min(mileage), 
                   yend = max(mileage)), 
               linetype = "dashed", 
               size = 0.1) + # Draw dashed lines 
  labs(x = "manufacturer",
       title = "Dot plot", 
       subtitle = "manufacturer vs. avg. mileage", 
       caption = "source: mpg") + 
  coord_flip()
```

![](/public/img/2022-06-22-visualization-summary/dot_plot-1.png)

## 슬로프 차트 (Slope chart)

슬로프 차트는 두 시점 사이의 순위를 비교하는 훌륭한 방법이 된다. 사실 슬로프 차트를 구성하는 내장 함수가 없기 때문에 직접 코드를 커스터마이징 할 수 있어야 한다.

```r
library(ggplot2)
library(scales)
theme_set(theme_classic()) 
df <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/gdppercap.csv")
colnames(df) <- c("continent", "1952", "1957")
left_label <- paste(df$continent, round(df$`1952`), sep = ", ")
right_label <- paste(df$continent, round(df$`1957`), sep = ", ")
df$class <- ifelse((df$`1957` - df$`1952`) < 0, "red", "green")

# slope chart
p <- ggplot(df) + 
  geom_segment(aes(x = 1, xend = 2, y = `1952`, yend = `1957`, col = class), size = 0.75, show.legend = FALSE) + 
  geom_vline(xintercept = 1, linetype = "dashed", size = 0.1) + 
  geom_vline(xintercept = 2, linetype = "dashed", size = 0.1) + 
  scale_color_manual(labels = c("Up", "Down"), values = c("green" = "#00ba38", "red" = "#f8766d")) + # color of lines 
  labs(x = "", y = "mean GDP per Cap") + # Axis labels
  xlim(0.5, 02.5) + ylim(0, (1.1 * (max(df$`1952`, df$`1957`)))) # X and Y axis limits 

# add texts
p <- p + geom_text(label = left_label, y = df$`1952`, x = rep(1, nrow(df)), hjust = 1.1, size = 3.5) 
p <- p + geom_text(label = right_label, y = df$`1957`, x = rep(2, nrow(df)), hjust = -0.1, size = 3.5) 
p <- p + geom_text(label = "Time 1(1952)", x = 1, y = 1.1 * (max(df$`1952`, df$`1957`)), hjust = 1.2, size = 4) # title 
p <- p + geom_text(label = "Time 2(1957)", x = 2, y = 1.1 * (max(df$`1952`, df$`1957`)), hjust = -0.1, size = 4) # title 

# minify theme
p + theme(panel.background = element_blank(), 
          panel.grid = element_blank(), 
          axis.ticks = element_blank(), 
          axis.text.x = element_blank(), 
          panel.border = element_blank(), 
          plot.margin = unit(c(1, 2, 1, 2), "cm"))
```

![](/public/img/2022-06-22-visualization-summary/slope_chart-1.png)

## 덤벨 차트 (Dumbbell chart)

덤벨 차트는 다음과 같은 경우에 유용한 도구이다.

- 두 시점 사이의 상대적 위치(성장 및 감소)를 시각화 할 때
- 두 범주형 변수 사이의 거리를 비교할 때 (y변수가 범주형 변수가 된다)

```r
library(ggplot2)
library(ggalt)
theme_set(theme_classic())
health <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/health.csv")
health$Area <- factor(health$Area, levels = as.character(health$Area)) # for right ordering of the dumbells 

# dumbbell chart
ggplot(health, aes(x = pct_2013, xend = pct_2014, y = Area, group = Area)) +
  geom_dumbbell(color = "skyblue", size = 0.75, colour_x = "blue") +
  scale_x_continuous(label = percent) + 
  labs(title = "Dumbbell chart", 
       subtitle = "Percent change: 2013 vs. 2014",
       x = "", 
       y = "", 
       caption = "source: https://github.com/hrbrmstr/ggalt") + 
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.background = element_rect(fill = "#f7f7f7"),
        panel.background = element_rect(fill = "#f7f7f7"),
        panel.grid.minor = element_blank(), 
        panel.grid.major.y = element_blank(), 
        panel.grid.major.x = element_line(),
        axis.ticks = element_blank(), 
        legend.position = "top",
        panel.border = element_blank())
```

![](/public/img/2022-06-22-visualization-summary/dumbbell_chart-1.png)

<div style="margin-bottom:100px;"></div>

# 분포 (Distribution)

많은 데이터 포인트가 존재할 때, 데이터 포인트가 어디에 어떻게 분포되어 있는지 파악하고 싶을 때 사용된다.

## 히스토그램 (Histogram)

연속형 변수에 대해서 구간별 빈도 수를 보여준다. `geom_histogram()`을 통해서 구현할 수 있으며 `bins` 혹은 `binwidth`를 통해 구간의 범위를 조정할 수 있다.

```r
library(ggplot2)
library(gridExtra)
library(RColorBrewer)
theme_set(theme_classic())

# histogram
g <- ggplot(mpg, aes(hwy)) + 
  scale_fill_brewer(palette = "BrBG")

binwidth <- g + geom_histogram(aes(fill = class), binwidth = 0.7, col = "black", size = 0.1) + # change binwidth
  labs(title = "Histogram with auto binning", 
       subtitle = "Highway mileage across vehicle classes")

bin <- g + geom_histogram(aes(fill = class), bins = 8, col = "black", size = 0.1) + # change number of bins 
  labs(title = "Histogram with fixed bins", 
       subtitle = "Highway mileage across vehicle classes")

grid.arrange(binwidth, bin, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/histogram-1.png)

## 밀도 그래프 (Density plot)

위에서 봤듯이, 히스토그램은 막대를 그리는 구간인 bin의 너비를 어떻게 잡는지에 따라 전혀 다른 모양이 될 수 있다는 단점이 있다. `goem_density()`로 그리는 밀도 그래프는 막대의 너비를 가정하지 않고 모든 점에서 데이터의 밀도, 즉 확률밀도함수를 추정한다.

```r
library(ggplot2)
theme_set(theme_classic())

# density plot
ggplot(mpg, aes(cty)) + 
  geom_density(aes(fill = factor(cyl)), alpha = 0.8) + 
  labs(x = "city mileage",
       title = "Density plot", 
       subtitle = "City mileage grouped by number of cylinders", 
       fill = "# cylinders",
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/density_plot-1.png)

## 상자 그림 (Box plot)

상자 그림 역시 분포를 보여주는 훌륭한 도구가 된다. 또한 여러 그룹 내의 분포를 중앙값, 범위 및 이상치 (있는 경우)와 함께 표시 할 수도 있다. `geom_boxplot()`을 이용하여 표현하고 `varwidth = TRUE`는 상자의 너비가 데이터 수에 비례하도록 조정하는 기능을 한다.

```r
library(ggplot2)
theme_set(theme_classic())

# box plot
ggplot(mpg, aes(class, hwy)) + 
  geom_boxplot(varwidth = TRUE, fill = "olivedrab4") + 
  labs(x = "class of vehicle", 
       y = "highway mileage",
       title = "Box plot", 
       subtitle = "Highway mileage grouped by class of vehicle", 
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/box_plot-1.png)

## 바이올린 플롯 (Violin plot)

바이올린 그림은 상자 그림과 비슷하지만 그룹 내 밀도를 보여준다. 하지만 상자 그림처럼 보여줄 수 있는 정보가 많지 않다. `geom_violin()`을 사용하여 그릴 수 있다.

```r
library(ggplot2)
theme_set(theme_bw())

# violin plot
ggplot(mpg, aes(class, hwy)) + 
  geom_violin(fill = "mediumseagreen") + 
  labs(x = "class of vehicle", 
       y = "highway mileage",
       title = "Violin plot", 
       subtitle = "Highway mileage vs. class of vehicle", 
       caption = "source: mpg")
```

![](/public/img/2022-06-22-visualization-summary/violin_plot-1.png)

## 인구 피라미드 (Population pyramid)

인구 피라미드는 특정 범주에 속하는 인구 수 또는 인구 비율을 시각화하는 독특한 방법을 제공한다. 아래 보이는 피라미드 그림은 이메일 마케팅 캠페인의 각 단계에서 유지되는 사용자 수의 훌륭한 예시다. `geom_bar()`를 변형시켜서 만들 수 있다.

```r
library(ggplot2)
library(ggthemes)
options(scipen = 999) # turns-off scientific notations like 1e+40
email_campaign_funnel <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/email_campaign_funnel.csv")

# x axis breaks and labels
brks <- seq(-15000000, 15000000, 5000000)
lbls = paste0(as.character(c(seq(15, 0, -5), seq(5, 15, 5))), "m") 

# population pyramid
ggplot(email_campaign_funnel, aes(x = Stage, y = Users, fill = Gender)) + # fill column
  geom_bar(stat = "identity", width = 0.6) + # draw the bars 
  scale_y_continuous(breaks = brks, labels = lbls) + # breaks and labels 
  coord_flip() + # flip axes 
  labs(title = "Email campaign funnel") + 
  theme_tufte() + # tufte theme from ggfortify 
  theme(plot.title = element_text(hjust = 0.5), 
        axis.ticks = element_blank()) + # center plot title
  scale_fill_brewer(palette = "Dark2") # color palette
```

![](/public/img/2022-06-22-visualization-summary/population_pyramid-1.png)

<div style="margin-bottom:100px;"></div>

# 구성 (Composition)

전체에서 여러 개의 범주가 각각 차지하는 비중이 얼마나 되는지를 표현하고 싶을 때 적절한 시각화 방법이 된다.

## 막대 그래프 (Bar chart)

구성을 표현하는 가장 기본적인 그래프로 `geom_bar()`로 구현할 수 있다. 아래의 두 가지 사항만 주의하면 된다.

- x축은 범주형 변수, y축은 연속형 변수로 설정
- `stat = "identity"`로 설정

```r
library(ggplot2)
library(dplyr)
theme_set(theme_classic())

# bar chart 
mpg %>% 
  group_by(manufacturer, class) %>% 
  summarise(N = n()) %>% 
  ggplot(aes(x = manufacturer, y = N)) + 
  geom_bar(aes(fill = class), stat = "identity", width = 0.5) + 
  theme(axis.text.x = element_text(angle = 65, vjust = 0.6)) + 
  labs(title = "Category wise bar chart", 
       subtitle = "Manufacturer of vehicles")
```

![](/public/img/2022-06-22-visualization-summary/bar_chart-1.png)

## 와플 차트 (Waffle chart)

와플 차트는 범주형 변수의 범주 구성을 보여주는 좋은 방법이다. `geom_tile()`을 통해서 표현할 수 있다.

```r
library(RColorBrewer)

# prepare data
waff_data <- mpg$class # categorical data
nrows <- 10
df <- expand.grid(y = 1:nrows, x = 1:nrows)
waff_table <- round(table(waff_data) * ((nrows * nrows) / (length(waff_data)))) 
df$category <- factor(rep(names(waff_table), waff_table)) 
# NOTE: if sum(waff_table) is not 100 (i.e. nrows^2), it will need adjustment to make the sum to 100. 

# waffle chart
ggplot(df, aes(x = x, y = y, fill = category)) + 
  geom_tile(color = "black", size = 0.5) + 
  scale_x_continuous(expand = c(0, 0)) + 
  scale_y_continuous(expand = c(0, 0)) +
  scale_fill_brewer(palette = "Set3") + 
  labs(title = "Waffle chart", 
       subtitle = "Class of vehicles", 
       caption = "source: mpg") + 
  theme(plot.title = element_text(size = rel(1.2)), 
        axis.text = element_blank(),
        axis.title = element_blank(), 
        axis.ticks = element_blank(), 
        legend.title = element_blank())
```

![](/public/img/2022-06-22-visualization-summary/waffle_chart-1.png)

## 원형 차트 (Pie chart)

구성을 보여주는 전형적인 방법인 원형 차트는 전달된 정보의 관점에서 와플 차트와 거의 동일하다. `geom_bar()`와 `coord_polar()을` 활용하여 구현할 수 있다.

```r
library(dplyr)
library(forcats)
library(ggplot2)
library(ggrepel)

# prepare data
df <- mpg %>% 
  group_by(class) %>% 
  summarize(cnt = n()) %>% 
  mutate(prop = round((cnt / sum(cnt)) * 100, 1)) %>% 
  arrange(prop)

text_df <- df %>% 
    mutate(csum = rev(cumsum(rev(prop))), 
         pos = prop/2 + lead(csum, 1),
         pos = if_else(is.na(pos), prop/2, pos))

# pie chart
df %>% 
  ggplot(aes(x = "", y = prop, fill = fct_inorder(class))) +
  geom_bar(color = "black", stat = "identity") +
  coord_polar(theta = "y", start = 0) +
  geom_label_repel(data = text_df,
                   aes(y = pos, label = paste0(prop, "%")),
                   size = 4.5, nudge_x = 1, show.legend = FALSE) +
  guides(fill = guide_legend(reverse = TRUE)) +
  theme(axis.line = element_blank(), 
        axis.text = element_blank(), 
        plot.title = element_text(hjust = 0.5)) +
  labs(x = "", 
       y = "", 
       title = "Pie chart of class", 
       fill = "class") + 
  scale_fill_brewer(palette = "Pastel1")
```

![](/public/img/2022-06-22-visualization-summary/pie_chart-1.png)

## 트리맵 (TreeMap)

트리맵은 중첩된 사각형을 사용하여 계층적 데이터를 표시하는 좋은 방법이다. 트리 맵을 만들려면 `treemapify` 패키지의 `treemapify()`를 사용하여 데이터를 원하는 형식으로 변환해야한다. 고려해야 할 중요 사항은 다음과 같다.

- 트리맵의 영역(넓이)을 묘사할 수 있는 변수가 존재해야 한다. (`area`, `label`)
- 트리맵안의 색을 채울 수 있는 변수가 존재해야 한다. (`fill`)
- 각 트리들을 묶을 수 있는 부모 그룹이 존재해야 한다. (`subgroup`)

```r
library(ggplot2)
library(treemapify)
library(ggplotify)
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

<div style="margin-bottom:100px;"></div>

# 변화 (Change)

## 시계열 그래프 (Time series plot)

시간의 흐름에 따른 특정 값의 변화를 표현할 때 주로 활용된다. 

### Time series plot from a time series object (ts)

`ggfortify` 패키지를 사용하면 자동으로 시계열 객체(ts)를 시계열 그래프로 표현할 수 있다.

```r
library(ggplot2)
library(ggfortify)
theme_set(theme_classic())
data("AirPassengers")

autoplot(AirPassengers) + 
  labs(title = "Air passengers") + 
  theme(plot.title = element_text(hjust = 0.5))
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_ts-1.png)

### Time series plot from a time dataframe

시계열 객체가 아닌 데이터프레임 형태일때에는 `geom_line()`을을 사용하여 시계열 그래프로 표현할 수 있다. x축의 구간은 자동으로 설정된다.

```r
library(ggplot2)
theme_set(theme_classic())

ggplot(economics, aes(x = date)) + 
  geom_line(aes(y = returns_perc)) + 
  labs(y = "returns %",
       title = "Time series chart",
       subtitle = "Returns percentage", 
       caption = "source: economics")
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_df-1.png)

### Time series plot for a yearly or monthly time series

`scale_x_date()`로 x축을 원하는 시간 간격 설정할 수 있다.

```r
library(ggplot2)
library(gridExtra)
library(lubridate)
theme_set(theme_bw())
economics_m <- economics[1:24, ] 
economics_y <- economics[1:90, ]

# labels and breaks for x axis text
lbls <- paste0(month.abb[month(economics_m$date)], " ", year(economics_m$date)) 
brks <- economics_m$date 

# monthly time series plot
monthly <- ggplot(economics_m, aes(x = date)) + 
  geom_line(aes(y = returns_perc)) + 
  labs(y = "Returns %", title = "Monthly time series") + 
  scale_x_date(labels = lbls, breaks = brks) + # change to monthly ticks and labels
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5), # rotate x axis text
        panel.grid.minor = element_blank()) # turn off minor grid

# labels and breaks for x axis text
brks <- economics_y$date[seq(1, length(economics_y$date), 12)]
lbls <- year(brks)

# yearly time series 
yearly <- ggplot(economics_y, aes(x = date)) + 
  geom_line(aes(y = returns_perc)) + 
  labs(y = "Returns %", title = "Yearly time series") + 
  scale_x_date(labels = lbls, breaks = brks) + # change to monthly ticks and labels
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5), # rotate x axis text
        panel.grid.minor = element_blank()) # turn off minor grid

grid.arrange(monthly, yearly, ncol = 2)
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_ym-1.png)

### Time series plot from a multiple columns of dataframe

두 개 이상의 그룹별 시간 흐름의 변화를 나타내고 싶을때 아래와 같이 표현할 수 있다. `geom_line()` 안의 `aes(col)`을 설정하면 된다.

```r
library(ggplot2)
library(lubridate)
theme_set(theme_bw())
data("economics_long")
df <- economics_long[economics_long$variable %in% c("psavert", "uempmed"), ] 
df <- df[year(df$date) %in% c(1967:1981), ] 

# labels and breaks for x axis text 
brks <- df$date[seq(1, length(df$date), 12)] 
lbls <- year(brks) 

# time series plot 
ggplot(df, aes(x = date)) + 
  geom_line(aes(y = value, col = variable)) + 
  labs(y = "Returns %", 
       title = "Time series of returns percentage",
       caption = "source: economics", color=NULL) + 
  scale_x_date(labels = lbls, breaks = brks) + # change to monthly ticks and labels 
  scale_color_manual(labels = c("psavert", "uempmed"), values = c("psavert" = "#00ba38", "uempmed" = "#f8766d")) + # line color 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, size = 8), # rotate x axis text 
        panel.grid.minor = element_blank()) # turn off minor grid 
```

![](/public/img/2022-06-22-visualization-summary/ts_plot_mc-1.png)

## 캘린더 히트맵 (Calender heatmap)

실제 캘린더 자체에서 표현하는 방식으로 주가와 같은 값의 변동, 특히 최고 및 최저를 확인할 때에는 캘린더 히트 맵이 훌륭한 도구가 된다. 실제 값 자체보다는 시간에 따른 값의 변화를 강조한다. `geom_tile()`와 `facet_grid` 기능을 통해 구현할 수 있지만 그래프로 구현하기 전에 캘린더 히트맵에 맞는 데이터의 형태를 갖추는 것이 더욱 중요한 작업이다.

```r
library(plyr)
library(ggplot2)
library(scales) 
library(zoo)
df <- read.csv("https://raw.githubusercontent.com/selva86/datasets/master/yahoo.csv")
df$date <- as.Date(df$date) 
df <- df[df$year >= 2012,] 

# create month and week 
df$yearmonth <- as.yearmon(df$date)
df$yearmonthf <- factor(df$yearmonth) 
df <- ddply(df, .(yearmonthf), transform, monthweek = 1 + week - min(week)) # compute week number of month 
df <- df[, c("year", "yearmonthf", "monthf", "week", "monthweek", "weekdayf", "VIX.Close")]

# calender heatmap
ggplot(df, aes(monthweek, weekdayf, fill = VIX.Close)) + 
  geom_tile(colour = "white") + 
  facet_grid(year ~ monthf) + 
  scale_fill_gradient(low = "blue", high = "red") + 
  labs(x = "Week of month", 
       y = "", 
       title = "Calendar heatmap", 
       subtitle = "Yahoo closing price", 
       fill = "Close")
```

![](/public/img/2022-06-22-visualization-summary/calender_heatmap-1.png)

## 슬로프 차트 (Slope chart)

슬로프 차트는 값의 변화와 범주간 순위를 시각화하기에 훌륭한 도구가 된다. 변화 시점이 두 개 이상이면서 너무 많지 않을 때 적합하다. 슬로프 차트에 알맞은 데이터 형태를 만드는 과정이 중요하다.

```r
theme_set(theme_classic()) 
source_df <- read.csv("https://raw.githubusercontent.com/jkeirstead/r-slopegraph/master/cancer_survival_rates.csv") 

# define functions. source: https://github.com/jkeirstead/r-slopegraph 
tufte_sort <- function(df, x = "year", y = "value", group = "group", method = "tufte", min.space = 0.05) { 
  # first rename the columns for consistency 
  ids <- match(c(x, y, group), names(df)) 
  df <- df[, ids] 
  names(df) <- c("x", "y", "group") 
  
  # expand grid to ensure every combination has a defined value 
  tmp <- expand.grid(x = unique(df$x), group = unique(df$group)) 
  tmp <- merge(df, tmp, all.y = TRUE) 
  df <- mutate(tmp, y = ifelse(is.na(y), 0, y)) 
  
  # cast into a matrix shape and arrange by first column 
  require(reshape2) 
  tmp <- dcast(df, group ~ x, value.var = "y") 
  ord <- order(tmp[, 2]) 
  tmp <- tmp[ord,] 
  min.space <- min.space * diff(range(tmp[, -1])) 
  yshift <- numeric(nrow(tmp)) 
  
  # start at "bottom" row 
  # repeat for rest of the rows until you hit the top 
  for (i in 2:nrow(tmp)) { 
    # shift subsequent row up by equal space so gap between 
    # two entries is >= minimum 
    mat <- as.matrix(tmp[(i-1):i, -1]) 
    d.min <- min(diff(mat)) 
    yshift[i] <- ifelse(d.min < min.space, min.space - d.min, 0) 
    } 
  
  tmp <- cbind(tmp, yshift = cumsum(yshift)) 
  scale <- 1
  tmp <- melt(tmp, id = c("group", "yshift"), variable.name = "x", value.name = "y") 
  # store these gaps in a separate variable so that they can be scaled ypos = a*yshift + y 
  tmp <- transform(tmp, ypos = y + scale * yshift) 
  return(tmp) 
  } 

plot_slope_chart <- function(df) { 
  ylabs <- subset(df, x == head(x, 1))$group 
  yvals <- subset(df, x == head(x, 1))$ypos 
  gg <- ggplot(df, aes(x = x, y = ypos)) + 
    geom_line(aes(group = group), colour = "grey80") + 
    geom_point(colour = "white", size = 8) + 
    geom_text(aes(label = y)) + 
    scale_y_continuous(name = "", breaks = yvals, labels = ylabs) 
  return(gg)
  } 

# prepare data 
df <- tufte_sort(source_df, x = "year", y = "value", group = "group", method = "tufte", min.space = 0.05)
df <- transform(df, x = factor(x, levels = c(5, 10, 15, 20), labels = c("5 years", "10 years", "15 years", "20 years")), y = round(y)) 

# slope chart 
plot_slope_chart(df) + 
  labs(title = "Estimates of % survival rates") + 
  theme(axis.title = element_blank(), 
        axis.ticks = element_blank(), 
        plot.title = element_text(hjust = 0.5, face = "bold"), 
        axis.text = element_text(face="bold"))
```

![](/public/img/2022-06-22-visualization-summary/slope_chart_ts-1.png)

## 계절성 차트 (Seasonal plot)

시계열 객체(ts, xts)를 사용하는 경우에 계절의 경향성을 시계열 그래프에 나타낼 수 있다. `ggseasonplot()`로 구현할 수 있다.

```r
library(ggplot2)
library(gridExtra)
library(forecast) 
theme_set(theme_classic()) 

# subset data 
nottem_small <- window(nottem, start = c(1920, 1), end = c(1925, 12)) # subset a smaller time window 

# seasonal plot 
airpassenger <- ggseasonplot(AirPassengers) + labs(title = "Seasonal plot: International airline passengers") 
nottem <- ggseasonplot(nottem_small) + labs(title = "Seasonal plot: Air temperatures at nottingham castle")

grid.arrange(airpassenger, nottem, ncol=2)
```

![](/public/img/2022-06-22-visualization-summary/seasonal_plot-1.png)

<div style="margin-bottom:100px;"></div>

# 군집 (Clustering)

소속집단을 모르는(unlabeled) 데이터들을 서로 동질적인 집단으로 분류하는 방법이다. 군집 분석은 데이터들 사이의 유사성에 근거하여 한 군집 안에 있는 데이터들은 유사하고, 다른 군집에 있는 데이터와는 서로 다르게 군집을 형성한다. 초기 데이터를 탐색할 때에도 매우 유용한 시각화 도구 중 하나이다.

## 계층적 덴드로그램 (Hierarchical Dendrogram)

계층적 군집방법은 각 개체 하나하나를 군집으로 두고 매 단계에서 가장 근접한 2개의 군집들을 하나의 군집으로 병합하는 과정을 말한다. 이러한 군집화 과정을 간략하게 표현한 도표가 바로 덴드로그램이다. `hclust()`를 통해 계층적 군집분석을 수행하고 `ggdendro` 패키지의 `ggdendrogram()`을 통해 덴드로그램을 나타낼 수 있다.

```r
library(ggplot2) 
library(ggdendro) 
theme_set(theme_bw()) 

hc <- hclust(dist(USArrests), "ave") # hierarchical clustering 

# hierarchical dendrogram
ggdendrogram(hc, rotate = TRUE, size = 2)
```

![](/public/img/2022-06-22-visualization-summary/hierarchical_dendrogram-1.png)

## 비계층적 군집분석 (Clustering)

분할 군집으로도 불리는 비계층적 군집분석에서는 먼저 군집의 갯수 K를 정한 후 데이터를 무작위로 K개의 군으로 배정한 후 배정된 군집의 중심으로부터의 거리를 계산한다. 각 군집들의 중심을 다시 설정하고 마찬가지로 거리를 계산한다. 거리가 더이상 작아지지 않을때까지 반복하게 된다. 군집이 설정된 후, 데이터의 변수가 많을 경우에는 주성분인 PC1과 PC2를 x축과 y축으로 사용하여 산점도로 표현한다. `geom_encircle()`을 통하여 그룹을 표시할 수 있다.

```r
library(ggplot2) 
library(ggalt) 
library(ggfortify) 
theme_set(theme_classic()) 

# compute data with principal components 
df <- iris[c(1, 2, 3, 4)] 
pca_mod <- prcomp(df, center = TRUE) # compute principal components

# dataframe of principal components
df_pc <- data.frame(pca_mod$x, Species = iris$Species) # dataframe of principal components 
df_pc_vir <- df_pc[df_pc$Species == "virginica",] # df for 'virginica'
df_pc_set <- df_pc[df_pc$Species == "setosa",] # df for 'setosa'
df_pc_ver <- df_pc[df_pc$Species == "versicolor",] # df for 'versicolor' 

# clustering
ggplot(df_pc, aes(PC1, PC2, col = Species)) +
  geom_point(aes(shape = Species), size = 2) + # draw points
  labs(title = "Iris clustering", 
       subtitle = "With principal components PC1 and PC2 as x and y axis", 
       caption = "source: iris") + 
  coord_cartesian(xlim = 1.2 * c(min(df_pc$PC1), max(df_pc$PC1)), 
                  ylim = 1.2 * c(min(df_pc$PC2), max(df_pc$PC2))) + # change axis limits 
  geom_encircle(data = df_pc_vir, aes(x = PC1, y = PC2)) + # draw circles 
  geom_encircle(data = df_pc_set, aes(x = PC1, y = PC2)) +
  geom_encircle(data = df_pc_ver, aes(x = PC1, y = PC2))
```

![](/public/img/2022-06-22-visualization-summary/clustering-1.png)

<div style="margin-bottom:100px;"></div>

# 공간 (Spatial)

`ggmap` 패키지는 Google 지도 API와 상호 작용하고 그리려는 장소의 좌표(위도 및 경도)를 얻는 기능을 제공한다. `geocode()`를 통해서 장소의 좌표를 얻을 수 있고 `qmap()`을을 통해서 지도를 불러들일 수 있다. 가져 올 지도의 유형은 `maptype` 값을 어떻게 설정하는지에 따라서 달라진다. `zoom` 기능을 통해서 지도를 확대 혹은 축소할 수 있다(기본값은 10이고 3부터 21까지 가능하다).

```r
library(ggplot2) 
library(ggmap) 
library(ggalt) 

# google API register 
register_google(key = "AIzaSyBjDkoYysOVCCGK-evX8uq2CSv-Q33V1hI")  # type your api key

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