import setuptools

with open("README.md", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="poctools",
    version="0.0.1",
    author="itmeng",
    author_email="yanitmeng@gmail.net",
    description="poc common tool library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yanmengfei/poctools",
    packages=setuptools.find_packages()
)
