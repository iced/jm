from setuptools import setup

setup(
    name="jm",
    version="0.1.1",
    author="Andrew Kirilenko",
    author_email="iced@gojuno.com",
    maintainer="Andrew Kirilenko",
    maintainer_email="iced@gojuno.com",
    description="Jupyter Maps",
    url="https://github.com/iced/jm",
    packages=["jm", "jm.sources", "jm.layers"],
    package_data = {"": ["js/*"]},
    install_requires=(
        "pystache"
    )
)
