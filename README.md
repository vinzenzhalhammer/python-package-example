# pytest-ci-example
[![codecov](https://codecov.io/gh/vinzenzhalhammer/pytest-ci-example/graph/badge.svg?token=T5N0755ZAD)](https://codecov.io/gh/vinzenzhalhammer/pytest-ci-example)

A minimal example how to integrate pytest with github actions.
The repository is structured in the following way
```
pytest-ci-example/
├── .github/
│   └── workflows/
│       └── pytest-ci.yml
├── examples/
│   ├── __init__.py
│   └── util.py
├── tests/
│   └── test_util.py
├── pytest.ini
├── requirements.txt
```