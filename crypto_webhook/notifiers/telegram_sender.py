import os
import logging
import aiohttp
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class TelegramSender:
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        
        if not self.bot_token or not self.chat_id:
            raise ValueError("Telegram 설정이 없습니다. (.env 파일을 확인하세요)")
            
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"

    async def send_message(self, message: str) -> bool:
        """텔레그램으로 메시지 전송"""
        try:
            url = f"{self.base_url}/sendMessage"
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json={
                    "chat_id": self.chat_id,
                    "text": message,
                    "parse_mode": "HTML"
                }) as response:
                    if response.status == 200:
                        logger.info("텔레그램 메시지 전송 성공")
                        return True
                    else:
                        response_text = await response.text()
                        logger.error(f"텔레그램 메시지 전송 실패: {response_text}")
                        return False
                
        except Exception as e:
            logger.error(f"텔레그램 전송 중 오류: {str(e)}")
            return False
