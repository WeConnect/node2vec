from setuptools import setup, find_packages
from os import path


setup(
    name='node2vec',
    version='1.0',
    description='libraries for building embed-able graph walks',
    url='https://github.com/WeConnect/node2vec',
    package_dir={'node2vec': 'src'},
    packages=['node2vec'],
    install_requires=['networkx', 'numpy', 'gensim'],
    package_data={
        '': ['*.emb', '*.edgelist'],
    }
)
