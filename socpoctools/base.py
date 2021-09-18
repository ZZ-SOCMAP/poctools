import abc
import logging
from typing import Union

import requests
import urllib3

urllib3.disable_warnings()


class Socpoc(metaclass=abc.ABCMeta):
    log_level = logging.INFO

    def __init__(self) -> None:
        self.logger = logging.Logger("SOCPOC", level=logging.INFO)
        self.mode = 'common'
        self.name = "BasePoc"
        self.example = ""
        self.session = requests.Session()
        self.session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
        self.session.verify = False

    def set_loglevel(self, level: Union[int, str]) -> None:
        self.logger.setLevel(level)

    def set_headers(self, headers: dict = None):
        if headers is not None:
            self.session.headers = headers

    def request(self, url: str, method: str = 'get', timeout: int = 10, **kwargs) -> requests.Response:
        try:
            resp = self.session.request(method, url, timeout=timeout, **kwargs)
        except requests.exceptions.RequestException as e:
            self.logger.warning(f'Run Poc[{self.name}] => {url} Error:\n\t{e}')
            resp = None
        return resp

    def get(self, url: str, **kwargs) -> requests.Response:
        return self.request(url, method='get', **kwargs)

    def post(self, url: str, **kwargs) -> requests.Response:
        return self.request(url, method='post', **kwargs)

    def put(self, url: str, **kwargs) -> requests.Response:
        return self.request(url, method='put', **kwargs)

    def head(self, url: str, **kwargs) -> requests.Response:
        return self.request(url, method='head', **kwargs)

    @abc.abstractmethod
    def verify(self, url):
        pass

    def run(self, url):
        self.logger.info(f'testing {url} with {self.name}')
        return self.verify(url)
