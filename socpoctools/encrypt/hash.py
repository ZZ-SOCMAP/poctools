import hashlib


def md5(string: str):
    return hashlib.md5(string.encode(encoding="utf-8")).hexdigest()
