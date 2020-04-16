import asyncio



async def first_prog():
    while True:
        print('Первая программа')
        await asyncio.sleep(1.0)


loop = asyncio.get_event_loop()
loop.run_until_complete(first_prog())
loop.close()
