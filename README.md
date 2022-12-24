# AWholeS

<!-- Badges here -->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<!-- Make sure this matches the description in pyproject.toml -->
A project to review the security posture in AWS

## Python package

See [AWholeS](AWholeS) or checkout the PyPi package [here](https://pypi.org/project/AWholeS/)

### Installation

```bash
pip install AWholeS
```

### Usage

```bash
# As a script:
python -m AWholeS
```

```python
# As a dependency:
from AWholeS.ec2 import show_all_available_regions

if __name__ == '__main__':
    show_all_available_regions()
```

## Other stuff

### CloudFormation templates

See [this folder](cloudformation_templates)

### List of tools

See [Tools](docs/tools)
