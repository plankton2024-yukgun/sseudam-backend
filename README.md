# Sseudam Backend

## Description

FastAPI로 구축된 쓰담의 서버입니다.


### Built with

* [![FastAPI]][FastAPI-url]
* [![Amazon-S3]][Amazon-S3-url]
* [![Amazon-RDS]][Amazon-RDS-url]
* [![Railway]][Railway-url]

### Architecture
![backend-architecture](/assets/sseudam-backend-architecture.png)


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
[Amazon-S3]: https://img.shields.io/badge/amazons3-569A31?style=for-the-badge&logo=amazons3&logoColor=white
[Amazon-S3-url]: https://aws.amazon.com/ko/s3/
[Amazon-RDS]: https://img.shields.io/badge/amazonrds-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white
[Amazon-RDS-url]: https://aws.amazon.com/ko/rds/
[Railway]: https://img.shields.io/badge/railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white
[Railway-url]: https://railway.app/
