import logging
from logging import getLogger

import requests


def make_request():
    url = "http://localhost:8000"
    logging.basicConfig(level=logging.INFO)

    logger = getLogger()

    with requests.Session() as session:
        for _ in range(4):
            with session.get(url) as response:
                logger.info(response.headers)

    # for _ in range(4):
    #     with requests.get(url) as response:
    #         logger.info(response.headers)


if __name__ == "__main__":
    make_request()
