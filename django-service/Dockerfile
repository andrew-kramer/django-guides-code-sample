# syntax=docker/dockerfile:1
FROM python:3

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set environment variable
ENV APP_HOME=/home/app/web

# Create the "app" user
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

# Create the directory
RUN mkdir -p $APP_HOME/staticfiles

# Set as the working directory
WORKDIR $APP_HOME

# Install netcat and update all packages
RUN apt-get update && apt-get install -y netcat

# Upgrade pip
RUN pip install --upgrade pip

# Change file ownership
RUN chown -R app:app $APP_HOME

# Set current user to "app" user
USER app:app

# Copy the requirements.txt file.
COPY --chown=app:app requirements.txt $APP_HOME

# Install the requirements.
RUN pip install --user -r requirements.txt

# Copy the rest of the code.
COPY --chown=app:app * $APP_HOME

# Set application entrypoint
ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]