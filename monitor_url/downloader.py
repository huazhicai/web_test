import requests
from retrying import retry
from config.conf import cm
from utils.logger import log


@retry(stop_max_attempt_number=3, wait_random_min=3000, wait_random_max=9000)
def _get_request(url):
    log.info(url)
    response = requests.get(url, headers=cm.HEADER, timeout=10, verify=False)
    if response.status_code != 200:
        raise Exception('unexpected status_code %s ' % response.status_code)
    return response


def get_request(url, exc_info=False):
    try:
        return _get_request(url)
    except Exception as e:
        log.error(f'{url}\n{e}', exc_info=exc_info)
        return None


