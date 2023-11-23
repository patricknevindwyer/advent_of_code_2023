from setuptools import setup, find_packages

with open("requirements.txt", "r") as raw:
    reqs = raw.read().splitlines()

setup(
    name='aoc-2023',
    version='0.0',
    description='Solving Advent of Code 2023',
    author='Patrick Dwyer',
    author_email='patricknevindwyer@gmail.com',
    packages=find_packages(include=['aoc', 'aoc.*']),
    install_requires=reqs,
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['aoc=aoc.entry:main']
    }
)