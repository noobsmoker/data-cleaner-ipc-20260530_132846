from setuptools import setup, find_packages

setup(
    name="data-cleaner-ipc-20260530_132846",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'data=data:main',
        ],
    },
)
