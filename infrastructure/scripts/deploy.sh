#!/bin/bash

# 환경 변수 확인
if [ -z "$ENVIRONMENT" ]; then
    echo "ENVIRONMENT 변수가 설정되지 않았습니다."
    exit 1
fi

# Docker 이미지 빌드
docker-compose -f infrastructure/docker/docker-compose.yml build

# Docker 컨테이너 실행
docker-compose -f infrastructure/docker/docker-compose.yml up -d 