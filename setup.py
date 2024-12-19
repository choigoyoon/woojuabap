from setuptools import setup, find_packages

setup(
    name="crypto_webhook",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'aiohttp',
        'python-dotenv',
        'openai',
        'pytest',
        'pytest-asyncio'
    ]
) 