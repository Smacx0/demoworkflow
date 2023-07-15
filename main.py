import os
import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig(
    filename='application.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "--SECRET--"


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}, Running on: {os.uname().version}")

    r = requests.get('https://api.github.com/zen')
    if r.status_code == 200:
        logger.info(f'Today\'s zen: {r.text}\n')