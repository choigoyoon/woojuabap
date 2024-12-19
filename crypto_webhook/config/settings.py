import os
from dotenv import load_dotenv
from pathlib import Path

# .env 파일 로드
load_dotenv()

# 기본 설정
class Settings:
    # 프로젝트 기본 설정
    APP_NAME = os.getenv("APP_NAME", "crypto_webhook")
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # API 키
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CRYPTOPANIC_TOKEN = os.getenv("CRYPTOPANIC_TOKEN")
    COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
    NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

    # Telegram 설정
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # Gmail 설정
    GMAIL_USER = os.getenv("GMAIL_USER")
    GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

    # 로깅 설정
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/crypto_webhook.log")

    # API 엔드포인트
    TELEGRAM_API_BASE = "https://api.telegram.org/bot{token}"
    CRYPTOPANIC_API_BASE = "https://cryptopanic.com/api/v1"
    COINGECKO_API_BASE = "https://api.coingecko.com/api/v3"

    def validate(self):
        """필수 설정 값 검증"""
        required_settings = [
            ("TELEGRAM_BOT_TOKEN", self.TELEGRAM_BOT_TOKEN),
            ("TELEGRAM_CHAT_ID", self.TELEGRAM_CHAT_ID),
            ("OPENAI_API_KEY", self.OPENAI_API_KEY),
            ("GMAIL_USER", self.GMAIL_USER),
            ("GMAIL_APP_PASSWORD", self.GMAIL_APP_PASSWORD)
        ]

        missing = [name for name, value in required_settings if not value]
        
        if missing:
            raise ValueError(f"Missing required settings: {', '.join(missing)}")

# 전역 설정 객체 생성
settings = Settings()
