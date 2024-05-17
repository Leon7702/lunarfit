---
title: Lunarfit (Working Title?)
author: [Jonas Trenkler]
date: 2024-05-11
lang: en-US
keywords: []
---

# Lunarfit (Working Title?)

## Local dev servers

You can set up the backend including the database using [Docker](https://docs.docker.com/engine/install/) and the `docker-compose.yml`.

``` sh
docker compose up -d --build
```

You can stop and remove the containers using `docker compose down`. There are also `start` `stop` and `restart` commands, which will keep the containers state. You probably don't need these here. In case the containers are running the `up` command takes care of removing and rebuilding them.

The backend is accessible at port 8000. You can access the API endpoint documentation at <localhost:8000>. For more information look at the backend `Readme` and `Dockerfile`.

The containers start in detached mode. If you need to monitor their output you can ommit the `d` flag, attach to the containers output using `docker attach [CONTAINERNAME]` or use Docker Desktop to inspect them. If you use VSCode there is an extension that can interact with containers as well.

> 🙊 The frontend service is currently disabled, as it needs adjustments for the Quasar CLI. `docker compose up` will only start the backend

>>>
The frontend is accessible at port 5173 (standard vite dev port).
You can limit the services that run by specifying `frontend` or `backend`.
Note that `backend` will start `db` as well.
This way you can use a local frontend dev server, but still have a working backend.
>>>

### First run - Database setup

The first time you run this will take a while, because it downloads and installs all the images and dependencies.

After that you need to initialize the backend database with. Also necessary if you change backend models.

``` sh
docker compose exec backend python manage.py migrate
```

If you need a superuser for the database run:
``` sh
docker compose exec backend python manage.py createsuperuser
```

You only need to do this the first time, since the database creates a persistent volume.

 Adding the `-v` flag to `docker compose down` will remove the persistent database volume. In case there is trouble. After that you will need to repeat the database setup. If you work on Django models, you can `makemigrations` and `migrate` while the containers are running.
