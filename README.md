## Digital-Twin-py

Python utilities and services for Digital Twin project.


### Content

* `dt.http` - HTTP clients, adapters and default settings for services communication


### Usage

Install package via e.g. `pip`:
```
pip install git+https://github.com/Kolo-naukowe-IDS-AGH/digital-twin-py
```

Optionally you can specify version of the `dt` package using tag:
```
pip install git+https://github.com/Kolo-naukowe-IDS-AGH/digital-twin-py@2022.04.01.01
```

## Development

Install python (3.10.2 specified in `.python-version` file) and create virtual environment e.g. via `pyenv`:
```
pyenv install 3.10.2 dt
pyenv activate dt
```

Next, install all dependencies:

```
pip install requirements-all.txt
```

Then, install `pre-commit` git hook:
```
pre-commit install
```
Optional you can run manually pre-commit against all the files:
```
pre-commit run --all-files
```

Create `feature` branch for your changes and don't forget about bumping package version in `setup.py` file.
