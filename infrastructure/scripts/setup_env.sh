#!/bin/bash

# Python 가상환경 설정
python -m venv .venv
source .venv/bin/activate

# 의존성 패키지 설치
pip install -r requirements.txt

# 로그 디렉토리 생성
mkdir -p logs

# 환경 변수 파일 생성
if [ ! -f .env ]; then
    cp .env.example .env
    echo "환경 변수 파일이 생성되었습니다. .env 파일을 수정해주세요."
fi 