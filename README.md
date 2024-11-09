# Sseudam Backend

## Description

FastAPI로 구축된 Sseudam의 서버입니다.


### Built with

* [![FastAPI]][FastAPI-url]


## Prerequisites

- 가상환경 생성

```shell
 python3 -m venv .venv
```

- 가상환경 활성화

```shell
source ./.venv/bin/activate
```

- 패키지 설치

```shell
pip install -r requirements.txt
```


## Usage

### 서버 실행

```shell
uvicorn app.main:app --reload
```

<http://localhost:8000>에 접속합니다.


## API

http://localhost:8000/docs


<!-- MARKDOWN LINKS & IMAGES -->
[FastAPI]: https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/