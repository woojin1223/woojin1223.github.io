---
title: "R로 구현하는 비계층적 군집 분석"
categories: 시각화
tags: [R, ggplot2, 군집 분석]
---

<div style="margin-bottom:100px;"></div>

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