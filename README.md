# python-package-example
[![codecov](https://codecov.io/gh/vinzenzhalhammer/python-package-example/graph/badge.svg?token=NTKMDKVS30)](https://codecov.io/gh/vinzenzhalhammer/python-package-example)

A minimal example how to build and publish a python package to TestPyPI with GitHub actions.
The repository is structured in the following way
```
python-package-example/
├── .github/
│   └── workflows/
│       └── publish.yml         ← GitHub Action for TestPyPI
├── examples/                   
│   ├── __init__.py
│   └── util.py
├── tests/
│   └── test_util.py
├── pyproject.toml              PEP 517 build config
├── setup.py                    Package config
├── README.md
├── LICENSE
├── pytest.ini
├── requirements.txt
```