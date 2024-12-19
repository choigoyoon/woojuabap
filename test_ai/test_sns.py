import asyncio
from crypto_webhook.collectors.sns_collector import SNSCollector
from crypto_webhook.utils.logger import setup_logger
import signal

async def main():
    # 로거 설정
    logger = setup_logger()
    logger.info("크립토 웹훅 시작")
    
    try:
        collector = SNSCollector()
        posts = await collector.collect()
        logger.info(f"수집된 포스트 수: {len(posts)}")
        
    except KeyboardInterrupt:
        logger.info("사용자에 의해 중단됨")
    except Exception as e:
        logger.error(f"실행 중 오류 발생: {str(e)}")
    finally:
        logger.info("모든 처리 완료!")

def handle_interrupt(signum, frame):
    raise KeyboardInterrupt()

if __name__ == "__main__":
    # Ctrl+C 핸들러 등록
    signal.signal(signal.SIGINT, handle_interrupt)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n프로그램이 안전하게 종료되었습니다.")