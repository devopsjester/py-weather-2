"""
Weather CLI - A simple weather application that shows current weather conditions
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py_weather_2",
    version="2.0.0",
    author="Weather CLI Contributors",
    author_email="your.email@example.com",
    description="A CLI weather application using free APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devopsjester/py-weather-2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0.0",
        "requests>=2.0.0",
    ],
    python_requires=">=3.8",  # Updated to match our CI matrix
    entry_points={
        "console_scripts": [
            "weather=py_weather_2.cli.main:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
    project_urls={
        "Bug Reports": "https://github.com/devopsjester/py-weather-2/issues",
        "Source": "https://github.com/devopsjester/py-weather-2",
    },
)