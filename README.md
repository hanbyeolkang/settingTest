# settingTest
환경 설정 테스트용

## 실행 방법
### 1. 환경 변수 설정 파일 .env 생성
sample.env 파일을 참고하여 같은 위치에 .env 파일 생성 (수동 작업)

### 2. 이미지 빌드
    docker compose build

### 3. 서비스 실행
    docker compose up -d

### 4. Airflow 초기 설정
airflow-init 실행 완료 후, airflow-webserver가 실행 되면 설정 \
your-username, your-password 변경해서 사용

    docker compose exec airflow-webserver airflow users create \
        --username your-username \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com \
        --password your-password