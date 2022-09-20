from setuptools import setup, find_packages

__author__ = "Paul Kuehne"
__email__ = "paul.kuehne@barkhauseninstitut.org"
__version__ = "0.0.3"


setup(
    name="mmw",
    version=__version__,
    description="Python API to comunicate with mmW system",
    author=__author__,
    author_email=__email__,
    url="",
    packages=["mmw", "bi_wrapper"],
    install_requires=["numpy", "zmq", "matplotlib"],
)
