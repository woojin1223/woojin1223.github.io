---
title: "시각화 정리"
categories: 시각화
tags: R
---

# 시각화를 해야 하는 이유

- 효과적인 정보 전달
- 정확한 분석을 위한 탐색적 데이터 분석

# 효과적인 시각화란 무엇인가?

- 사실을 왜곡하지 않고 올바른 정보를 전달하는 것
- 단순하지만 필요한 정보가 모두 담겨있는 것
- 정보 전달의 목적을 해치지 않는 적절한 미적 요소를 추가하는 것
- 하나의 시각화에 정보가 과부하 되지 않는 것

# 여덟 가지의 대표적인 시각화 유형

1. 상관관계 (Correlation)
2. 편차 (Deviation)
3. 순위 (Ranking)
4. 분포 (Distribution)
5. 구성 (Composition)
6. 변화 (Change)
7. 군집 (Clustering)
8. 공간 (Spatial)

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
  labs(title = "Scatterplot", 
       subtitle = "area vs. population", 
       x = "area", 
       y = "population", 
       caption = "source: midwest")
```

![](/public/img/2022-06-22-visualization-summary/unnamed-chunk-1-1.png)