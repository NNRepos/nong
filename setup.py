from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nong-nnrepos",
    version="0.2",
    author="NN",
    description="a neural-network based pong game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NNRepos/nong",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        "pygame>=1.9",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.7',
    entry_points={
        'console_scripts': ['nong=src.main:main']
    },
)
