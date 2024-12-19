import json
import logging
from datetime import datetime

# 로깅 설정
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_test_news():
    """테스트용 뉴스 데이터"""
    return [
        {
            "source": "Test News 1",
            "title": "테스트 뉴스 제목 1",
            "url": "https://example.com/news1"
        },
        {
            "source": "Test News 2",
            "title": "테스트 뉴스 제목 2",
            "url": "https://example.com/news2"
        }
    ]

def main(event, context):
    """메인 핸들러"""
    try:
        logger.info("테스트 뉴스 수집 시작")
        
        # 테스트 뉴스 데이터 가져오기
        news = get_test_news()
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "timestamp": datetime.now().isoformat(),
                "news": news
            }, ensure_ascii=False)
        }
        
    except Exception as e:
        logger.error(f"실행 중 오류: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}, ensure_ascii=False)
        }
