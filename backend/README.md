# Django backend

REST backend using `django-rest-framework`.
Currently has a basic setup, following <https://www.django-rest-framework.org/tutorial/quickstart/>.

## TODO

- [ ] Does this need `django cors headers?`
- [ ] `gunicorn` ( + `nginx`) as web server?

## Project Setup

### Dependency management

The project uses [Poetry](https://python-poetry.org/) for dependency management, and to export a `requirements.txt` for use with other tools, e.g. venv. Another good solution is [Pipenv](https://pipenv.pypa.io/en/latest/). But you can use the venv

Make sure to create a virtual environment, before installing dependencies, see <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>

On Windows:
```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```

On Unix:
``` sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Or using `Poetry`:

``` sh
poetry install
```

If you change dependencies in the `pyproject.toml` (or with `poetry add/remove/update`) you'll need to re-export the `requirements.txt`.
``` sh
poetry export --output requirements.txt
```

## Starting the Django dev server

Don't forget to [activate the python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/). When using `poetry` you can use `poetry shell` instead to enter the environment or prepend `poetry run COMMAND` to execute `COMMAND` in the environment.

`python3 manage.py runserver 8000` starts the dev server and allows access the API endpoint on `localhost:8000`.

`django-rest-framework` provides a browsable API, listing all available endpoints.
You can create a superuser to browse the API webinterface using `python3 manage.py createsuperuser`.
