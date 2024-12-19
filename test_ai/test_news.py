import pytest
import pytest_asyncio
import asyncio
from datetime import datetime, timedelta
from crypto_webhook.collectors.news_collector import NewsCollector
from crypto_webhook.utils.logger import setup_logger

logger = setup_logger()

@pytest_asyncio.fixture
async def news_collector():
    collector = NewsCollector()
    yield collector

@pytest.mark.asyncio
async def test_news_collection(news_collector):
    """뉴스 수집 테스트"""
    result = await news_collector.collect_data()
    
    # 기본 검증
    assert isinstance(result, list), "결과는 리스트여야 합니다"
    assert len(result) > 0, "최소 1개 이상의 뉴스가 있어야 합니다"
    
    # 첫 번째 뉴스 아이템 검증
    news = result[0]
    assert isinstance(news, dict), "뉴스 아이템은 딕셔너리여야 합니다"
    assert "title" in news, "뉴스에는 제목이 있어야 합니다"
    assert "content" in news, "뉴스에는 내용이 있어야 합니다"
    assert "timestamp" in news, "뉴스에는 타임스탬프가 있어야 합니다"
    
    # 타임스탬프 검증
    timestamp = datetime.fromisoformat(news['timestamp'])
    assert isinstance(timestamp, datetime), "타임스탬프는 ISO 형식이어야 합니다"
    assert timestamp <= datetime.now(), "타임스탬프는 현재 시간보다 이전이어야 합니다"
    assert timestamp >= datetime.now() - timedelta(minutes=5), "타임스탬프는 5분 이내여야 합니다"

@pytest.mark.asyncio
async def test_empty_news_collection(news_collector, monkeypatch):
    """에러 상황에서의 뉴스 수집 테스트"""
    # collect_data 메서드를 모의(mock)하여 빈 리스트 반환
    async def mock_collect():
        return []
    
    monkeypatch.setattr(news_collector, "collect_data", mock_collect)
    result = await news_collector.collect_data()
    
    assert isinstance(result, list), "에러 상황에서도 리스트를 반환해야 합니다"
    assert len(result) == 0, "에러 상황에서는 빈 리스트를 반환해야 합니다"