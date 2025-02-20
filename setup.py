"""
Weather CLI - A simple weather application that shows current weather conditions
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="weather-cli",
    version="0.1.0",
    author="Your Name",
    description="A CLI weather application using free APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "requests>=2.0.0",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "weather=weather:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)