# Pull base image, see https://hub.docker.com/_/python/
FROM python:3.12-bookworm

# Set environment variables, see https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
# Don't copy project, instead use volumes, so hot-reloading works
# COPY . .
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

COPY ./entrypoint.sh .
CMD [ "./entrypoint.sh" ]
