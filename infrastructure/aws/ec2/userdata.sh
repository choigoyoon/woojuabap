#!/bin/bash

# 시스템 업데이트
yum update -y

# Docker 설치
yum install -y docker
service docker start
usermod -a -G docker ec2-user

# Docker Compose 설치
curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# 애플리케이션 설정
mkdir -p /app
cd /app

# 환경 변수 설정
touch .env
echo "TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}" >> .env
echo "OPENAI_API_KEY=${OPENAI_API_KEY}" >> .env 