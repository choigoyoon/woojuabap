import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

class NewsCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    async def fetch_news(self, url: str) -> dict:
        """뉴스 기사 크롤링"""
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 제목 추출
            title = soup.title.string if soup.title else "제목 없음"
            
            # 본문 추출
            content = ""
            article = soup.find(['article', 'main', 'div'], 
                              class_=['article_content', 'article-body'])
            if article:
                paragraphs = article.find_all('p')
                content = '\n'.join(p.text.strip() for p in paragraphs)
            
            return {
                "title": title,
                "content": content,
                "url": url
            }
            
        except Exception as e:
            logger.error(f"크롤링 중 오류 발생: {str(e)}")
            raise 