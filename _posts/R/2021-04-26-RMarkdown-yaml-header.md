---
title: "[RMarkdown] YAML Header"
categories: 
    - RMarkdown
tags:
    - R
    - RMarkdown
    - YAML Header
toc: true
toc_sticky: true
toc_label: "목차"
---
## YAML Header

**R Markdown 소개** 포스트에서 R Markdown의 세 가지 구성 요소는 YAML Header, Markdown Text, R Code Chunk라고 언급을 했습니다.  
그리고 **R Markdown - Markdown** 포스트에서 Markdown Text에 대해, **R Markdown - R Code Chunk** 포스트에서 R Code Chunk에 대해 설명했습니다.  
이번 포스트에는 R Markdown의 세 가지 구성 요소 중 하나이자 <u>Rmd 파일을 Knit하여 나오는 보고서에 대한 세부 사항을 조절</u>하는 **YAML Header**에 대해 알아보겠습니다.  
YAML Header는 <u>YAML 형식으로 된 Header</u>를 의미하는데 먼저 YAML에 대해 간단하게 소개하겠습니다.

## YAML (YAML Ain’t Markup Language)

### 정의 및 개념

**YAML**은 <u>데이터 직렬화 형식</u>들 중 하나입니다.  
_데이터 직렬화 형식_이란 <u>데이터를 한 눈에 봐도 읽기 쉽게 저장하는 형식</u>으로서 Markdown과 같이 문서를 작성하기 위한 마크업 언어보다 더 간단한 형태를 가지고 있습니다.  
그리고 YAML은 원래 **Yet Another Markup Language** 의 축약어였지만 현재는 **YAML Ain't Markup Language** 를 의미합니다.  
참고로 YAML은 야믈이라고 읽습니다.

### 예시

**YAML Ain't Markup Language,** 이 단어들에서 알 수 있듯이 YAML의 본딧말에 YAML이라는 단어가 또 들어가는 _재귀적인 이름_을 가지고 있습니다.  
그래서 YAML이라는 용어와 그 의미를 처음 보면 도대체 무슨 말을 전달하려는 건지 한 번에 알기 힘듭니다.  
따라서 예시를 통해 YAML을 이해해 보겠습니다. 

#### 1. 기본적으로 `key: value` 와 같이 사전(dictionary)식으로 데이터를 표현합니다.

(YAML 예시)  

저(통남)에 대한 간단한 소개를 YAML 형식으로 작성했습니다.

```
name: 통남
major: 통계학
hobby: 산책
```

위 YAML 예시를 JSON 형식으로 쓰면 다음과 같습니다.

(JSON 예시)

```
{
	"name": "통남"
	"major": "통계학"
	"hobby": "산책"
}
```

#### 2. YAML에서 목록은 Markdown의 목록과 유사하게 글머리 기호 `-` 를 사용하여 작성합니다. 
단, 들여쓰기에 유의해야 합니다. 또한, Python의 리스트 형식과 같은 방법으로 한 줄로 작성할 수 있습니다.  

(YAML 예시)

```
name: 통남
major: 통계학
hobby: 
	- 산책
	- 운동
```

또는

```
name: 통남
major: 통계학
hobby: [산책, 운동]
```

위 YAML 예시를 JSON 형식으로 쓰면 다음과 같습니다.  

(JSON 예시)

```
{
	"name": "통남"
	"major": "통계학"
	"hobby": ["산책", "운동"]
}
```

#### 3. 들여쓰기를 사용해 하위의 사전(dictionary) 구조를 만듭니다.

(YAML 예시)

```
name: 통남
major:
	first_major: 수학
	second_major: 통계학
hobby: [산책, 운동]
```

위 YAML 예시를 JSON 형식으로 쓰면 다음과 같습니다.  

(JSON 예시)

```
{
	"name": "통남"
	"major": {
		"first_major": "수학",
		"second_major": "통계학"
	}
	"hobby": ["산책", "운동"]
}
```

### 특징

- 데이터 직렬화 형식들 중에서 제일 직관적
    + 데이터 직렬화 형식: CSV, JSON, TOML, XML, YAML
- 들여쓰기를 사용해 구조체를 만듦
- YAML 파일의 확장자는 `.yaml` 또는 `.yml`

이제부터 본격적으로 **YAML Header**에 대해 알아보겠습니다.  
RStudio의 상단 탭에 있는 *File > New File > R Markdown* 에서 OK를 클릭하면 기본적인 내용이 들어 있는 Rmd 파일이 생성되는데, 그 파일의 제일 상단에 있는 YAML Header는 아래와 같습니다. 

(YAML Header 예시)

```
---
title: "R Markdown tutorial"
author: "Tong Nam"
date: "2020 11 20"
output: html_document
---
```

(출력 결과)

보고서의 제일 상단에 아래 그림과 같이 출력됩니다.  

![yaml_header](/assets/images/yaml_header.png)

## 대표적인 key

YAML Header에 사용되는 대표적인 key를 알아보겠습니다.  
위 YAML Header 예시에서 볼 수 있듯이 `title`, `author`, `date`, `output` 이렇게 4 개의 key가 대표적입니다.

### title

보고서의 제목에 해당하는 key.

### author

보고서 작성자에 해당하는 key.

### date

보고서 작성 날짜에 해당하는 key.  
**R Markdown - R Code Chunk** 포스트에서 소개한 **인라인 Code Chunk**를 사용하여 보고서에 Knit할 때의 날짜가 적용되게 할 수 있습니다.  
즉, 위 YAML Header 예시에서 `date: "2020 11 20"` 대신 ``date: "`r Sys.Date()`"`` 를 작성합니다.

### output

보고서의 출력 형식을 지정하는 key.  
`output` key에 올 수 있는 value는 엄청 다양하므로 추후에 별도의 포스트로 작성하겠습니다.  
RStudio에서 기본으로 제공하는 출력 형식은 `html_document`, `html_notebook`, `pdf_document`, `word_document` 입니다. 

- `html_document` : 결과물이 `.html` 형식
- `html_notebook` : 결과물이 `.nb.html` 형식
- `pdf_document` : 결과물이 `.pdf` 형식
- `word_document` : 결과물이 `.docx` 형식

---

## 참고

- [R for Data Science](https://r4ds.had.co.nz/)
- [https://ko.wikipedia.org/wiki/YAML](https://ko.wikipedia.org/wiki/YAML)