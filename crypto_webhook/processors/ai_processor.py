import os
import logging
from openai import OpenAI
from typing import Optional, Dict, Any
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class AIProcessor:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API 키가 없습니다. (.env 파일을 확인하세요)")
        
        self.client = OpenAI(api_key=api_key)

    async def analyze_content(self, content: str) -> Optional[str]:
        """
        OpenAI를 사용하여 컨텐츠 분석
        """
        try:
            if not content:
                logger.warning("분석할 컨텐츠가 없습니다.")
                return None

            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "암호화폐 뉴스 분석가로서 다음 내용을 분석해주세요."},
                    {"role": "user", "content": content}
                ],
                temperature=0.7,
                max_tokens=500
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"AI 분석 중 오류: {str(e)}")
            return None

    async def summarize_news(self, news_text: str) -> Optional[str]:
        """
        뉴스 내용 요약
        """
        try:
            if not news_text:
                logger.warning("요약할 뉴스가 없습니다.")
                return None

            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "다음 뉴스를 간단히 요약해주세요."},
                    {"role": "user", "content": news_text}
                ],
                temperature=0.5,
                max_tokens=200
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"뉴스 요약 중 오류: {str(e)}")
            return None
