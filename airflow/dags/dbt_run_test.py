from __future__ import annotations
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
import subprocess
import os

# dbt 프로젝트 설정
DBT_PROJECT_DIR = '/opt/airflow/dbt'
DBT_PROFILE = 'coreload_proj'


@task
def run_dbt_model():
    # 환경 변수 확인 및 출력
    print("=== Environment Variables ===")
    for key in ['REDSHIFT_HOST', 'REDSHIFT_PORT', 'REDSHIFT_DB', 'REDSHIFT_USER', 'REDSHIFT_PASSWORD']:
        value = os.getenv(key)
        if value:
            print(f"{key}: {'***' if 'PASSWORD' in key else value}")
        else:
            print(f"{key}: NOT SET")
    
    if not os.getenv('REDSHIFT_HOST'):
        raise ValueError("REDSHIFT_HOST environment variable is not set.")
    
    print("\n=== Running dbt command ===")
    dbt_command = [
        "dbt",
        "run",
        "--profile", DBT_PROFILE,
        "--project-dir", DBT_PROJECT_DIR,
        "--profiles-dir", DBT_PROJECT_DIR,
        "--select", "stg_sample"
    ]
    
    print(f"Command: {' '.join(dbt_command)}")
    
    try:
        result = subprocess.run(
            dbt_command,
            check=True, 
            capture_output=True,
            text=True,
            cwd=DBT_PROJECT_DIR  # 작업 디렉토리 명시
        )
        print("\n=== dbt STDOUT ===")
        print(result.stdout)
        if result.stderr:
            print("\n=== dbt STDERR ===")
            print(result.stderr)
        
    except subprocess.CalledProcessError as e:
        print("\n=== dbt FAILED ===")
        print(f"Return code: {e.returncode}")
        print("\n=== STDOUT ===")
        print(e.stdout)
        print("\n=== STDERR ===")
        print(e.stderr)
        raise


with DAG(
    dag_id="dbt_run_test",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["dbt", "redshift", "test"]
) as dag:

    run_dbt_model()