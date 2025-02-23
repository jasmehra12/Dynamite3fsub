from bot import Bot
import asyncio
import aiohttp
URL = "https://rolling-nikkie-drxyhacker12-3c8942d4.koyeb.app/"
async def ping():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(URL) as response:
                    print(f"Pinged server, status: {response.status}")
            except Exception as e:
                print(f"{e}")
            await asyncio.sleep(600)
loop = asyncio.get_event_loop()
loop.create_task(ping())
Bot().run()
