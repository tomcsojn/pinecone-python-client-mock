from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=1.3.4","typing-extensions>=3.7.4","numpy"]

setup(
    name="pinecone_python_client_mock",
    version="0.0.0",
    author="Tamás Majszlinger",
    author_email="tomcsojn@gmail.com",
    description="pinecone python client mocking class for testing purposes",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tomcsojn/pinecone-python-client-mock",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)