import asyncio # asyncio 임포트

async def say(message, delay):
    print(f"'{message}' 출력 대기 중 ({delay}초)")
    await asyncio.sleep(delay)  # 비동기적으로 delay 만큼 대기
    print(message)

async def main():
    print("비동기 함수 실행 시작")
    await say("첫번째 메시지", 1)
    await say("두번째 메시지", 2)
    print("비동기 함수 실행 완료")

asyncio.run(main())