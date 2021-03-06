import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pagilist",
    version="0.0.1",
    author="jersobh",
    author_email="jersobh@gmail.com",
    description="List pagination by page or limit,offset",
    long_description="Simple module to paginate lists using page or
limit/offset. Source code available at
[Github](https://github.com/jersobh/pagilist).",
    long_description_content_type="text/markdown",
    url="https://github.com/jersobh/pagilist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
