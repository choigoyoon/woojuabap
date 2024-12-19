import asyncio
import logging
from crypto_webhook.collectors import FollowinCollector
from crypto_webhook.notifiers import TelegramSender
from crypto_webhook.processors import AIProcessor
from crypto_webhook.config import setup_logger

logger = setup_logger()

async def main():
    """메인 실행 함수"""
    try:
        collector = FollowinCollector()
        telegram = TelegramSender()
        ai_processor = AIProcessor()
        
        # 데이터 수집 및 처리
        data = await collector.collect_data()
        if data:
            # AI 분석
            analysis = await ai_processor.analyze_content(str(data))
            if analysis:
                # 텔레그램 전송
                await telegram.send_message(analysis)
                
    except Exception as e:
        logger.error(f"실행 중 오류 발생: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())