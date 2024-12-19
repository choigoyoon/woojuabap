# Crypto News Collector
원본 저장소: https://github.com/choigoyoon/woojuabap.git

암호화폐 관련 뉴스와 트윗을 수집하여 텔레그램으로 전송하는 봇

## 기능
- 트위터 계정 모니터링
- CryptoPanic 뉴스 수집
- AI 기반 내용 요약
- 텔레그램 실시간 알림
- 중복 내용 필터링
- Gmail을 통한 알림 발송
- AWS Lambda/EC2 지원
- Docker 컨테이너화 지원

## 설치
```bash
git clone https://github.com/choigoyoon/woojuabap.git
cd woojuabap
pip install -r requirements.txt
```

## 환경 설정
`.env` 파일 생성:
```
CRYPTOPANIC_TOKEN=your_token
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
OPENAI_API_KEY=your_openai_key
GMAIL_USER=your_gmail
GMAIL_APP_PASSWORD=your_app_password
```

## 실행 방법

### 로컬 실행
```bash
python test_sns.py  # SNS 모니터링
python crypto_webhook/main.py  # 전체 시스템
```

### Docker 실행
```bash
docker-compose -f infrastructure/docker/docker-compose.yml up -d
```

### 테스트 실행
```bash
pytest
```

## 프로젝트 구조
```
woojuabap/
├── crypto_webhook/        # 메인 패키지
│   ├── aws/              # AWS 관련 코드
│   │   ├── lambda_handler.py
│   │   └── webhook.py
│   │
│   ├── collectors/       # 데이터 수집
│   │   ├── cache_manager.py
│   │   ├── crawler.py
│   │   └── followin_collector.py
│   │
│   ├── config/          # 설정 관리
│   │   ├── logger.py
│   │   └── settings.py
│   │
│   ├── notifiers/       # 알림 발송
│   │   ├── gmail_sender.py
│   │   └── telegram_sender.py
│   │
│   ├── processors/      # 데이터 처리
│   │   └── ai_processor.py
│   │
│   └── tests/          # 테스트 코드
│
├── infrastructure/      # 인프라 관련
│   ├── docker/         # Docker 설정
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   │
│   ├── aws/           # AWS 인프라 설정
│   │   ├── lambda/
│   │   └── ec2/
│   │
│   └── scripts/       # 유틸리티 스크립트
│       ├── deploy.sh
│       └── setup_env.sh
│
├── test_ai/           # AI 테스트
│   ├── test_import.py
│   ├── test_news.py
│   ├── test_sns.py
│   └── test_webhook.py
│
├── screenshots/       # 스크린샷
├── .env              # 환경 변수
├── .env.example      # 환경 변수 예제
├── .gitignore       # Git 제외 파일
├── main.py          # 메인 실행 파일
├── pytest.ini       # Pytest 설정
├── requirements.txt  # 의존성 패키지
├── setup.py         # 패키지 설정
└── setup_project.py # 프로젝트 초기 설정
```

## 주요 구성 요소

### AWS Lambda
- 웹훅 엔드포인트 처리
- 실시간 데이터 수집

### 데이터 수집기
- 뉴스 크롤러
- SNS 데이터 수집기
- 캐시 매니저

### 알림 시스템
- Telegram 봇
- Gmail 발송

### AI 처리
- OpenAI GPT-4 통합
- 컨텐츠 분석 및 요약

## 배포

### Docker 배포
```bash
chmod +x infrastructure/scripts/deploy.sh
ENVIRONMENT=production ./infrastructure/scripts/deploy.sh
```

### AWS Lambda 배포
```bash
# Lambda 함수 패키지 생성
zip -r lambda_function.zip crypto_webhook/aws/lambda_handler.py

# AWS CLI를 통한 배포
aws lambda update-function-code --function-name crypto-webhook \
    --zip-file fileb://lambda_function.zip
```

## 기술 스택
- Python (99.5%)
- HCL/Terraform (0.5%)
- Docker
- AWS (Lambda, EC2)
- OpenAI GPT-4