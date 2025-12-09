import requests

from .classes.BaseHttpTarget import BaseHttpTarget


class GlobalProtect(BaseHttpTarget):
    NAME = "GlobalProtect"
    DESCRIPTION = "Palo Alto GlobalProtect"

    def __init__(self, host, port, timeout, fireprox):
        self.timeout = timeout
        self.url = f"https://{host}:{port}/global-protect/login.esp"

        if fireprox:
            self.url = f"https://{fireprox}/fireprox/+webvpn+/index.html"

        self.cookies = {"SESSID": "1"}

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
			      "Content-Type": "application/x-www-form-urlencoded",
			      "Content-Length": "124",
			      "Origin": "https://{host}",
			      "Referer": "https://{host}/global-protect/login.esp",
			      "Upgrade-Insecure-Requests": "1",
			      "Sec-Fetch-Dest": "document",
			      "Sec-Fetch-Mode": "navigate",
			      "Sec-Fetch-Site": "same-origin",
			      "Sec-Fetch-User": "?1",
			      "Priority": "u=0, i",
			      "Te": "trailers",
			      "Connection": "keep-alive"
        }

        self.data = {
            "prot": "https:",
            "server": "{host}",
            "inputStr": "",
            "action": "getsoftware",
            "user": "",
            "passwd": "",
            "new-passwd": "",
            "confirm-new-passwd": "",
            "ok": "Log In"
        }

    """
        # proxy settings
        self.http_proxy  = 'http://127.0.0.1:8080'
        self.https_proxy = 'http://127.0.0.1:8080'
        self.ftp_proxy   = 'http://127.0.0.1:8080'

        self.proxyDict = {
              'http'  : self.http_proxy,
              'https' : self.https_proxy,
              'ftp'   : self.ftp_proxy
        }
    """

    def set_username(self, username):
        self.data["user"] = username
        self.username = username

    def set_password(self, password):
        self.data["passwd"] = password
        self.password = password

    def login(self, username, password):
        # set data
        self.set_username(username)
        self.set_password(password)
        # post the request
        response = requests.post(
            self.url,
            headers=self.headers,
            cookies=self.cookies,
            data=self.data,
            timeout=self.timeout,
            verify=False,
        )  # , proxies=self.proxyDict)
        return response
