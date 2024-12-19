import requests
import json

def test_webhook():
    # 웹훅 URL
    webhook_url = "https://mmfk2bp66c.execute-api.ap-northeast-2.amazonaws.com/prod/webhook"
    
    # 테스트할 URL들
    test_urls = [
        "https://www.google.com",
        "https://www.naver.com",
        "https://www.amazon.com"
    ]
    
    for test_url in test_urls:
        print(f"\nTesting with URL: {test_url}")
        
        # 요청 데이터 준비
        data = {
            "url": test_url
        }
        
        try:
            # POST 요청 보내기
            response = requests.post(webhook_url, json=data)
            
            # 응답 출력
            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    test_webhook()