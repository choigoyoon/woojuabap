import pytest
import pytest_asyncio
from crypto_webhook.notifiers.telegram_sender import TelegramSender
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.asyncio
class TestTelegramSender:
    @pytest_asyncio.fixture
    async def sender(self):
        """TelegramSender 인스턴스 생성"""
        sender = TelegramSender()
        yield sender

    async def test_initialization(self, sender):
        """초기화 테스트"""
        assert sender.bot_token is not None, "봇 토큰이 없습니다"
        assert sender.chat_id is not None, "채팅 ID가 없습니다"
        assert isinstance(sender.base_url, str), "base_url이 올바르지 않습니다"

    async def test_simple_message(self, sender):
        """단순 메시지 전송 테스트"""
        message = "🤖 단순 테스트 메시지"
        result = await sender.send_message(message)
        assert result is True, "메시지 전송 실패"

    async def test_formatted_message(self, sender):
        """포맷된 메시지 전송 테스트"""
        formatted_msg = """
🔔 *테스트 알림*
- 제목: 테스트
- 내용: 포맷 테스트
"""
        result = await sender.send_message(formatted_msg)
        assert result is True, "포맷된 메시지 전송 실패"

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 