---
title: "[RStudio] 기본 개념"
categories: 
    - RStudio
tags:
    - R
    - RStudio
toc: true
toc_sticky: true
toc_label: "목차"
---

![RStudiologo](https://d33wubrfki0l68.cloudfront.net/62bcc8535a06077094ca3c29c383e37ad7334311/a263f/assets/img/logo.svg)

## 소개

1. R과 RStudio의 차이
    - **R**은 프로그래밍 언어
        + RGui는 단순한 인터페이스를 가진 R 코드 실행 프로그램
            * (참고) RGui는 R 설치 시 기본으로 제공하는 코드 실행 프로그램
    - **RStudio**는 R에 특화된 코드 작성 도구
        + RGui보다 보기 좋은 인터페이스를 가짐
        + 편리한 단축키 제공
        + 다른 프로그램과 연동 가능 - Git/SVN
2. 장점
    - 사용자 친화적인 인터페이스 제공
    - RStudio 사용법에 숙달되면 편리하게 코딩을 할 수 있음
    - **RStudio Server** 제공
        + 서버에서 코딩할 수 있음 → 다른 컴퓨터에도 나의 코드를 작업을 할 수 있음
    - **R Markdown** 지원
        + RStudio에서 보고서 형식의 파일을 만들 수 있음
    - **프로젝트** 관리
        + 여기서 프로젝트는 작업할 때 파일들을 관리하는 단위를 뜻함
        + 프로젝트로 R 소스 코드 파일들을 묶어서 관리할 수 있음
    - **Git**과 연동 가능
        + 소스 코드의 변경 사항을 관리할 수 있음

3. 단점

- 많은 기능을 담고 있기 때문에 프로그램 크기가 큼
    + RGui나 다른 에디터에 비해 설치 공간과 메모리를 많이 차지함
- R 문법 뿐만 아니라 RStudio 사용법에 대한 공부도 해야 함
- R Markdown을 지원하지만 보고서 형식의 파일을 만드려면 **knit**라는 과정을 거쳐야 하기 때문에 Jupyter Notebook처럼 즉각적인 보고서를 작성하지 못함

## 주의 사항

- R 설치 후 RStudio 설치해야 함
- 사용자 이름(계정 이름)이 한글인 경우 패키지 설치 시 에러가 발생할 수 있음
- 다운로드 경로에 한글이나 공백이 있는 경우 여러 에러가 발생할 수 있음

## 대표적인 단축키

RStudio 사용자에게 도움되는 단축키를 소개합니다.

#### 1. Ctrl + Shift + N

- 새 **Script** 창을 생성하는 단축키
    + Script는 코드를 작성하는 공간을 말함
    + R Script의 경우 Script에서 코드 작성 뿐만 아니라 코드 실행도 할 수 있음

#### 2. Ctrl + Enter / Alt + Enter

- **Ctrl + Enter**: 해당하는 줄의 코드를 실행 후 다음 줄에 커서 이동
- **Alt + Enter**: 해당하는 줄의 코드를 실행 (커서 이동 X)

#### 3. Alt + -

- **Assignment operator**(`<-`)를 삽입하는 단축키

#### 4. Ctrl + Shift + M

- **Pipe operator**(`%>%`)를 삽입하는 단축키
    + Pipe operator에 대한 설명은 `magrittr` 패키지 관련 포스팅에서 하겠음

#### 5. Ctrl + Shift + C

- 해당하는 줄을 **주석** 처리하는 단축키
- 여러 줄을 드래그하여 `ctrl + shift + c` 누르면 드래그된 줄 전부를 주석 처리할 수 있음
- 다시 한 번 누르면 주석 해제됨

#### 6. Ctrl + Shift + R

- **Section**을 삽입하는 단축키
    + Section은 Script 안에서 구역을 나누는 단위를 말함
    + Section에 대한 자세한 설명은 R 문법에 대한 포스팅에서 하겠음

#### 7. Ctrl + Shift + H

- **작업 경로**(working directory)를 설정하는 단축키
- 작업 경로 설정은 `setwd()` 함수를 사용하여 할 수도 있고 `ctrl + shift + h` 를 눌러 마우스로 직접 경로를 설정할 수도 있음
    + 작업 경로에 대한 자세한 설명은 R 문법에 대한 포스팅에서 하겠음