FROM python:3.10-slim

# 기본 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리
WORKDIR /opt/airflow

# requirements.txt 복사
COPY requirements.txt .

# Python 패키지 설치 (Airflow 포함)
RUN pip install --no-cache-dir -r requirements.txt

# Airflow 홈 설정
ENV AIRFLOW_HOME=/opt/airflow