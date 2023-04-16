from setuptools import find_packages, setup

setup(
    name='application',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'fastapi',
        "uvicorn[standard]"
    ],
    version='0.1.0',
    description='APP test samsung AI',
    author='Samsung team',
    license='',
)