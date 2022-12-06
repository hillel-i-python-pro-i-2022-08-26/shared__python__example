import asyncio
import itertools
from typing import TypeAlias

# import urllib.parse
import aiohttp
import bs4

T_URL: TypeAlias = str
T_TEXT: TypeAlias = str


async def get_urls_from_text(text: T_TEXT) -> list[T_URL]:
    soup = bs4.BeautifulSoup(markup=text, features="html.parser")
    urls = []
    for link_element in soup.find_all("a"):
        url = link_element.get("href")
        urls.append(url)

    return list(set(urls))


async def make_request(url: T_URL, session: aiohttp.ClientSession) -> T_TEXT:
    async with session.get(url) as response:
        return await response.text()


async def make_requests(urls: list[T_URL]) -> list[T_TEXT]:
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(url, session) for url in urls]
        return await asyncio.gather(*tasks)


async def main():
    urls_input = [
        "https://example.com",
        "https://www.djangoproject.com/",
    ]

    texts = await make_requests(urls=urls_input)

    urls_output = sorted(set(itertools.chain(*(await asyncio.gather(*[get_urls_from_text(text) for text in texts])))))

    print(urls_output)


if __name__ == "__main__":
    asyncio.run(main())
