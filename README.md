# python-package-example

[![codecov](https://codecov.io/gh/vinzenzhalhammer/python-package-example/graph/badge.svg?token=NTKMDKVS30)](https://codecov.io/gh/vinzenzhalhammer/python-package-example)

An example Python package that demonstrates:

- Writing and testing code with `pytest`
- Using GitHub Actions for continuous integration
- Building and publishing the package to **TestPyPI**

This is a follow-up to the [pytest-ci-example](https://github.com/vinzenzhalhammer/pytest-ci-example) repo.

### Installation (from TestPyPI)

```bash
pip install --index-url https://test.pypi.org/simple/ python-package-example
```
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