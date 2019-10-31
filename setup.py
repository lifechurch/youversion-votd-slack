import os

from setuptools import setup

VERSION = '0.0.1'

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name), encoding='utf-8').read()

setup(
    name="yv-votd-slack",
    description="YouVersion Verse Of The Day Slackbot",
    license="Apache License, Version 2.0",
    url="https://github.com/lifechurch/youversion-votd-slack",
    packages=['votd', 'tests'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=[
        'youversion',
        'slackclient',
        'certifi'
    ]
)
