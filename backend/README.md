# Django backend

REST backend using `django-rest-framework`.
Currently has a basic setup, following <https://www.django-rest-framework.org/tutorial/quickstart/>.

## TODO

- [ ] Does this need `django cors headers?`
- [ ] `gunicorn` ( + `nginx`) as web server?

## Project Setup

### Dependency management

The project uses `poetry` for dependency management, and to export a `requirements.txt` for use with other tools, e.g. venv etc.

``` sh
poetry export --output requirements.txt
```

Make sure to create a virtual environment, before installing dependencies, see https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

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


## Starting the Django dev server

`python3 manage.py runserver 8000` and access the API endpoints on `localhost:8000`.
`django-rest-framework` provides a browsable API, listing all available endpoints.

