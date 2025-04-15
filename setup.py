from setuptools import setup, find_packages

setup(
    name="python-package-example-vh",
    version="0.0.4",
    author="Vinzenz Halhammer",
    author_email="info@vinzenzhalhammer.com",
    description="A minimal example how to build and publish a python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vinzenzhalhammer/python-package-example",
    packages=find_packages(include=["python_package_example", "python_package_example.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
