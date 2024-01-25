import asyncio
import time

'''
Requirements_
- Build a Request class
    - get() - to fetch the details of the url provided
    - get_url_data - holds the mapping of url and data
- Build a BringAPI Data class (async)
    - fetch_api_data() - make API call
    - process_fetched_data() - process fetched data
'''

class Request:
    def __init__(self):
        self.directory = {
            "url_1": "data-1",
            "url_2": "data-2",
            "url_3": "data-3",
            "url_4": "data-4",
        }

    async def http_get(self, url):
        return await asyncio.to_thread(self.get, url)

    def get(self, url):
        time.sleep(5)
        return self.get_url_data(url)

    def get_url_data(self, url):
        return self.directory.get(url)


class BringAPIData:
    def __init__(self):
        self.request = Request()

    async def make_api_call(self, url):
        print("fetching API data")
        data = await self.request.http_get(url)
        print("Done fetching API data")
        return data

    async def fetch_api_data(self, url):
        data = await self.make_api_call(url)
        self.process_fetched_data(data)

    def process_fetched_data(self, data):
        print(f"Data is being processed - {data}")

async def main():
    urls = ["url_1", "url_2", "url_3", "url_4"]
    bringData = BringAPIData()
    await asyncio.gather(*[bringData.fetch_api_data(url) for url in urls])

if __name__ == "__main__":
    asyncio.run(main())




