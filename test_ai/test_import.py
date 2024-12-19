# test_import.py
try:
    from crypto_webhook.collectors.sns_collector import SNSCollector
    print("임포트 성공!")
    collector = SNSCollector()
    print("인스턴스 생성 성공!")
except Exception as e:
    print(f"오류 발생: {str(e)}")