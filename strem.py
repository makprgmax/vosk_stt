import asyncio
import httpx

async def fetch_data():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://example.com")
        print(r.status_code)

async def main():
    await asyncio.gather(fetch_data(), fetch_data(), fetch_data())

asyncio.run(main())
