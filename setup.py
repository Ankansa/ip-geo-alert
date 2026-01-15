from setuptools import setup, find_packages

setup(
    name="ip-geo-alert",
    version="0.1.0",
    description="IP geolocation alert package with FastAPI support",
    author="Ankan Sarkar",
    packages=find_packages(),
    install_requires=["requests", "fastapi"],
    python_requires=">=3.9",
)
