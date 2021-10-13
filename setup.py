from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Siva Nagendra",
    description="A small package for dvc tensorflow pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SivaNagendra-sn/DVC_Tensorflow",
    author_email="sivanagendra.paruchuri@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3" ,
    ]
)