# Lunarfit (Working Title?)


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Lunarfit (Working Title?)](#lunarfit-working-title)
    - [Local dev servers](#local-dev-servers)
        - [First run - Database setup](#first-run---database-setup)
        - [Create a superuser](#create-a-superuser)
    - [Browse the API-Documentation](#browse-the-api-documentation)
        - [OpenAPI 3 Schema](#openapi-3-schema)

<!-- markdown-toc end -->

## Local dev servers

You can set up the backend including the database using [Docker](https://docs.docker.com/engine/install/) and the `docker-compose.yml`.

``` sh
docker compose up -detach --build
```

> ⚠️ The `--build` flag makes sure you stay up-to-date, if there are changes in the backend dependencies, `--detach` hides the containers output.

You can stop and remove the containers using `docker compose down`.
There are also `start` `stop` and `restart` commands, which will keep the containers state.
You should prefer to rebuild them with the `up --build` command instead, as it takes care of running database migrations for you.
In case the containers are running, `up` removes and rebuilds them as necessary.

Adding the `-v` flag to `docker compose down` will remove the persistent database volume, deleting you database state, so you can start from scratch. 

The backend is accessible at port 8000. You can access the API endpoint documentation at <localhost:8000>, see [Browse the API-Documentation](#browse-the-api-documentation). For more information look at the backend `Readme` and `Dockerfile`.

> 🙊 The frontend service is currently disabled, as it needs adjustments for the Quasar CLI. `docker compose up` will only start the backend

>>>
You can limit the services that run by specifying `frontend` or `backend`.
Note that `backend` will start `db` as well.
You can use a local frontend dev server, and only run the backend in a container.
>>>

### First run - Database setup

> ℹ️ This should not be necessary anymore, as the container will try to generate and apply migrations every time you run it with `docker compose up --build`.

The first time you run this will take a while, because it downloads and installs all the images and dependencies.

After that you need to initialize the backend database with. Also necessary if you change backend models.

``` sh
docker compose exec backend python manage.py migrate
```

### Create a superuser

A superuser can be useful to browse the API or if you work on admin stuff.

If you need a superuser, run:
``` sh
docker compose exec backend python manage.py createsuperuser
```

You only need to do this the first time, since the database creates a persistent volume.

Adding the `-v` flag to `docker compose down` will remove the persistent database volume. In case there is trouble. After that you will need to repeat the database setup. If you work on Django models, you can `makemigrations` and `migrate` while the containers are running.

### Getting help

If something is not working, have a look at the logs! If you can't figure it out from there, create an issue with the log output.

There are different ways to do that:

You can monitor the containers output directly by omitting the `-d` or `--detach` flag, or use Docker Desktop to inspect them.
If you use VSCode there is an extension that can interact with containers as well.

From the command-line you can use:
``` sh
docker logs CONTAINERNAME [--follow]
```

## Browse the API-Documentation

The backend's API is automatically documented and browsable in different ways.
When the backend server is running (in dev mode) the standard Django-Rest-Framework view on the API is available at the server root: <http://localhost:8000>
This page enables you to send HTTP requests to the running server and actually use the API.

You can log in with an existing user and view the API with the permissions of that user. For example logging in with a normal user account, you can only update or delete that specific user's data.
If you set up a [superuser](#create-a-superuser) you can browse, update, delete all the available records and create new ones with the privileges of a database admin, through the available endpoints.

### OpenAPI 3 Schema

The backend automatically generates an API schema using [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/index.html).
You can download the schema as YAML from `/api/schema`, to use with any tool you like.
It is also possible to generate schema through the [CLI](https://drf-spectacular.readthedocs.io/en/latest/readme.html#take-it-for-a-spin).

The simplest way is to browse the API Schema in a [Swagger UI](https://swagger.io/tools/swagger-ui/) or [Redoc](https://redocly.github.io/redoc/) frontend. These are available in the backend at [/api/schema/swagger-ui](http://localhost:8000/api/schema/swagger-ui/) and [/api/schema/redoc/](http://localhost:8000/api/schema/redoc/), without any additional setup.
