import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_directories():
    """필요한 디렉토리 생성"""
    directories = [
        'crypto_webhook/aws',
        'crypto_webhook/collectors',
        'crypto_webhook/config',
        'crypto_webhook/notifiers',
        'crypto_webhook/processors',
        'crypto_webhook/tests/test_aws',
        'crypto_webhook/tests/test_collectors',
        'crypto_webhook/tests/test_notifiers',
        'crypto_webhook/tests/test_processors',
        'logs',
        'infrastructure'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        logger.info(f"디렉토리 생성: {directory}")

def create_env_file():
    """환경 변수 파일 생성"""
    if not os.path.exists('.env'):
        with open('.env.example', 'r', encoding='utf-8') as example:
            with open('.env', 'w', encoding='utf-8') as env:
                env.write(example.read())
        logger.info(".env 파일이 생성되었습니다.")

def main():
    """프로젝트 초기 설정"""
    try:
        setup_directories()
        create_env_file()
        logger.info("프로젝트 설정이 완료되었습니다!")
        
    except Exception as e:
        logger.error(f"설정 중 오류 발생: {str(e)}")

if __name__ == "__main__":
    main()