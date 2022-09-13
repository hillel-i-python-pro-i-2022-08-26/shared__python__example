import logging

import requests

from requests_example.init_logging import init_logging


def get_core_logger():
    return logging.getLogger("core")


# aiohttp


def main():
    logger = get_core_logger()

    url = "https://example.com"

    logger.info(f"{url=}")

    # response = requests.get(url=url)
    with requests.Session() as session:
        response = session.get(url)

        logger.info(f"response status: {response.status_code}")
        logger.info(f"response text: {response.text}")

    # url = 'https://example.com/path/path2/?arg=123&arg2=12#anchor'
    # response = requests.get(url=url, params={'arg': 123, 'arg2': 12})

    print()


if __name__ == "__main__":
    init_logging()
    main()
