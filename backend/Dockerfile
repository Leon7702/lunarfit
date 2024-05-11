# Pull base image, see https://hub.docker.com/_/python/
FROM python:3.12-alpine

# Set environment variables, see https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Don't copy project, instead use volumes, so hot-reloading works
# COPY . .
# Run the dev server on 0.0.0.0 to make it accessible outside the container
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
