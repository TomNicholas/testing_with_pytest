import os
from setuptools import setup

opts = dict(name='pytest_example',
            requires=['xarray'])


if __name__ == '__main__':
    setup(**opts)
