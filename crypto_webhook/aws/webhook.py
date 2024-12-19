import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class WebhookSender:
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        
    async def send_telegram(self, message: str) -> bool:
        """텔레그램으로 메시지 전송"""
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            payload = {
                "chat_id": self.chat_id,
                "text": message,
                "parse_mode": "HTML"
            }
            
            response = requests.post(url, json=payload)
            response.raise_for_status()
            logger.info("텔레그램 메시지 전송 성공")
            return True
            
        except Exception as e:
            logger.error(f"텔레그램 전송 실패: {str(e)}")
            return False