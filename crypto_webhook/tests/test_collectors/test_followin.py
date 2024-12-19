import asyncio
import logging
import os
import sys

# 절대 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def main():
    try:
        print("=== Followin 크롤러 테스트 시작 ===")
        print(f"BASE_DIR: {BASE_DIR}")
        print(f"현재 디렉토리: {os.getcwd()}")
        
        # collectors 패키지 import 테스트
        print("\nImport 시도...")
        from collectors.followin_collector import FollowinCollector  # 상대 경로로 수정
        print("Import 성공!")
        
        # 크롤러 인스턴스 생성
        print("\n크롤러 인스턴스 생성 시도...")
        collector = FollowinCollector()
        print("인스턴스 생성 성공!")
        
        # 데이터 수집 실행
        print("\n데이터 수집 시작...")
        results = await collector.run()
        
        # 결과 출력
        print("\n=== 수집 결과 ===")
        if not results:
            print("수집된 데이터가 없습니다.")
        else:
            for category_id, items in results.items():
                category_name = collector.categories[category_id]['name']
                print(f"\n=== {category_name} ===")
                print(f"수집된 항목: {len(items)}개")
                
                for item in items[:3]:
                    print("-" * 50)
                    print(f"URL: {item.get('url')}")
                    print(f"시간: {item.get('timestamp')}")
                    
    except ImportError as e:
        print(f"\nImport 오류: {str(e)}")
        print("현재 Python 경로:")
        for path in sys.path:
            print(f"  - {path}")
    except Exception as e:
        print(f"\n실행 중 오류 발생: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"예상치 못한 오류 발생: {str(e)}")
        import traceback
        traceback.print_exc()