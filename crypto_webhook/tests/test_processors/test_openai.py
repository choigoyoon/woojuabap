import os
from dotenv import load_dotenv
from openai import OpenAI  # 새로운 import 방식
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def test_openai():
    try:
        # API 키 확인
        api_key = os.getenv("OPENAI_API_KEY")
        print(f"API 키 존재 여부: {'있음' if api_key else '없음'}")
        print(f"API 키 길이: {len(api_key) if api_key else 0}")
        
        # 새로운 방식으로 클라이언트 초기화
        client = OpenAI(api_key=api_key)
        
        # 새로운 방식으로 API 호출
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Can you hear me?"}
            ]
        )
        
        print("\nAPI 응답:")
        print(response.choices[0].message.content)
        print("\n테스트 성공!")
        
    except Exception as e:
        print(f"\n오류 발생: {str(e)}")

if __name__ == "__main__":
    test_openai() 