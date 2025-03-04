import asyncio

async def task(task_id, delay):
    print(f"Task {task_id} 시작 (대기 {delay}초)")
    await asyncio.sleep(delay)
    print(f"Task {task_id} 완료")
    return f"결과 {task_id}"

async def main():
    tasks = [task(i, i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print("모든 작업 완료:", results)

asyncio.run(main())
