from setuptools import setup, find_packages
from os import path


setup(
    name='node2vec',  # Required
    version='1.0',  # Required
    description='forked node2vec for Python 3',  # Optional
    url='https://github.com/WeConnect/node2vec',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=['networkx', 'numpy', 'gensim'],  # Optional
    package_data={  # Optional
        '': ['*.emb', '*.edgelist'],
    }
)
