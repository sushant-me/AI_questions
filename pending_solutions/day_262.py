import asyncio

async def fetch_data(url):
    # Simulate fetching data from a URL
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = ['https://example.com', 'https://example.com/data', 'https://example.com/info']
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Run the async main function
asyncio.run(main())