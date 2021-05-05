from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='checkblock_deepsort',
    description='checkblock_deepsort',
    long_description=readme,
    license='Not open source',
    url='https://github.com/pxlbrain/checkblock_deepsort/',
    version='0.0.1',
    install_requires=requirements,
    tests_require=['pytest'],
    packages=['deep_sort_pytorch', 'deep_sort_pytorch.deep_sort', 'deep_sort_pytorch.deep_sort.deep',
              'deep_sort_pytorch.deep_sort.sort', 'deep_sort_pytorch.utils'],
    keywords=['checkblock_deepsort'],
    python_requires='~=3.8'
)
