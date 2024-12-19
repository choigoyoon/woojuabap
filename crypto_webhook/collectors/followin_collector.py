import aiohttp
import asyncio
from datetime import datetime
import logging
from typing import List, Dict, Optional
import os
from bs4 import BeautifulSoup
from crypto_webhook.collectors.cache_manager import CacheManager  # 절대 경로로 수정
# 또는
from woojuabap.crypto_webhook.collectors.cache_manager import CacheManager  # 상대 경로로 수정
import yaml
from dotenv import load_dotenv
# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG 레벨로 변경
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('crypto_webhook')

class FollowinCollector:
    def __init__(self):
        try:
            # 환경 변수 로드
            load_dotenv()
            
            logger.debug("FollowinCollector 초기화 시작")
            
            # Followin 카테고리 설정
            self.categories = {
                'home': {
                    'name': '홈',
                    'url': 'https://followin.io/ko'
                },
                'news': {
                    'name': '뉴스',
                    'url': 'https://followin.io/ko/news'
                },
                'market': {
                    'name': '시장',
                    'url': 'https://followin.io/ko/market'
                }
            }

            # HTTP 헤더 설정
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
            }

            # 캐시 디렉토리 생성
            current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cache_dir = os.path.join(current_dir, 'cache')
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
                logger.debug(f"캐시 디렉토리 생성: {cache_dir}")

            # 캐시 매니저 초기화
            cache_file = os.path.join(cache_dir, 'followin_cache.db')
            self.cache = CacheManager(cache_file, 3600)
            logger.debug(f"캐시 매니저 초기화 완료: {cache_file}")

            logger.debug("FollowinCollector 초기화 완료")
            
        except Exception as e:
            logger.error(f"FollowinCollector 초기화 중 오류: {str(e)}")
            raise

    async def collect_by_category(self, category_id: str) -> List[Dict]:
        """카테고리별 정보 수집"""
        try:
            category = self.categories[category_id]
            url = category['url']
            logger.debug(f"{category['name']} 카테고리 수집 시작: {url}")
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    if response.status != 200:
                        logger.error(f"{category['name']} 카테고리 접근 실패: {response.status}")
                        return []
                    
                    html = await response.text()
                    logger.debug(f"{category['name']} HTML 데이터 수집 완료")
                    
                    # 테스트를 위해 간단한 결과 반환
                    return [{
                        'category': category['name'],
                        'url': url,
                        'timestamp': datetime.now().isoformat()
                    }]
                    
        except Exception as e:
            logger.error(f"{category_id} 카테고리 수집 중 오류: {str(e)}")
            return []

    async def run(self) -> Dict[str, List[Dict]]:
        """전체 수집 프로세스 실행"""
        try:
            logger.info("Followin 데이터 수집 시작")
            all_data = {}
            
            for category_id in self.categories:
                logger.debug(f"{self.categories[category_id]['name']} 카테고리 처리 시작")
                items = await self.collect_by_category(category_id)
                
                if items:
                    all_data[category_id] = items
                    logger.info(f"{self.categories[category_id]['name']} 카테고리: {len(items)}개 항목 수집")
                
                await asyncio.sleep(2)  # 카테고리 간 딜레이
            
            logger.info(f"전체 수집 완료. 총 {len(all_data)} 카테고리")
            return all_data
            
        except Exception as e:
            logger.error(f"수집 프로세스 실행 중 오류: {str(e)}")
            return {}