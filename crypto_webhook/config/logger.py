import os
import logging
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv

load_dotenv()

# 로그 디렉토리 생성
log_dir = os.path.dirname(os.getenv('LOG_FILE', 'logs/crypto_webhook.log'))
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 로거 설정
logger = logging.getLogger('crypto_webhook')
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

# 로그 포맷 설정
class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] = record.created
        log_record['level'] = record.levelname

# 파일 핸들러 설정 (로그 로테이션 포함)
file_handler = RotatingFileHandler(
    os.getenv('LOG_FILE', 'logs/crypto_webhook.log'),
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5
)
file_handler.setFormatter(CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s'))
logger.addHandler(file_handler)

# 콘솔 핸들러 설정
console_handler = logging.StreamHandler()
console_handler.setFormatter(CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s'))
logger.addHandler(console_handler) 