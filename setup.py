import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="submarine_api",
    version="0.0.1",
    author="Will Clark",
    author_email="will8clark@gmail.com",
    description="Python bindings for Submarine Swap API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/willcl-ark/submarine_swaps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="submarine swaps api",
    install_requires=[],
    python_requires='>=3.7',
)
