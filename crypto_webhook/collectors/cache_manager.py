import sqlite3
import time
from typing import Optional
import logging

logger = logging.getLogger('crypto_webhook')

class CacheManager:
    def __init__(self, db_path: str, expire_time: int = 3600):
        """
        캐시 매니저 초기화
        :param db_path: SQLite DB 파일 경로
        :param expire_time: 캐시 만료 시간 (초)
        """
        self.db_path = db_path
        self.expire_time = expire_time
        self._init_db()

    def _init_db(self):
        """데이터베이스 초기화"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS cache (
                        key TEXT PRIMARY KEY,
                        timestamp INTEGER
                    )
                ''')
                conn.commit()
                logger.debug(f"캐시 DB 초기화 완료: {self.db_path}")
        except Exception as e:
            logger.error(f"캐시 DB 초기화 실패: {str(e)}")
            raise

    def is_cached(self, key: str) -> bool:
        """
        키가 캐시에 있고 만료되지 않았는지 확인
        :param key: 확인할 키
        :return: 캐시 존재 여부
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT timestamp FROM cache WHERE key = ?', (key,))
                result = cursor.fetchone()
                
                if result:
                    timestamp = result[0]
                    return (time.time() - timestamp) < self.expire_time
                return False
        except Exception as e:
            logger.error(f"캐시 확인 실패: {str(e)}")
            return False

    def add(self, key: str):
        """
        캐시에 키 추가
        :param key: 추가할 키
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO cache (key, timestamp)
                    VALUES (?, ?)
                ''', (key, int(time.time())))
                conn.commit()
                logger.debug(f"캐시 추가: {key}")
        except Exception as e:
            logger.error(f"캐시 추가 실패: {str(e)}")

    def remove(self, key: str):
        """
        캐시에서 키 제거
        :param key: 제거할 키
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM cache WHERE key = ?', (key,))
                conn.commit()
                logger.debug(f"캐시 제거: {key}")
        except Exception as e:
            logger.error(f"캐시 제거 실패: {str(e)}")

    def clear_expired(self):
        """만료된 캐시 항목 제거"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                expire_timestamp = int(time.time()) - self.expire_time
                cursor.execute('DELETE FROM cache WHERE timestamp < ?', (expire_timestamp,))
                conn.commit()
                logger.debug("만료된 캐시 제거 완료")
        except Exception as e:
            logger.error(f"만료 캐시 제거 실패: {str(e)}") 