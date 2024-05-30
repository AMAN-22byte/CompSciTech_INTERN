# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install RabbitMQ dependencies
RUN apt-get update && \
    apt-get install -y gnupg2 curl apt-transport-https && \
    curl -fsSL https://packages.erlang-solutions.com/erlang-solutions_2.0_all.deb -o erlang-solutions.deb && \
    dpkg -i erlang-solutions.deb && \
    apt-get update && \
    apt-get install -y erlang && \
    curl -fsSL https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/gpg.key | apt-key add - && \
    curl -fsSL https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/deb/debian/dists/buster/main/binary-amd64/Packages | tee /etc/apt/sources.list.d/rabbitmq.list && \
    apt-get update && \
    apt-get install -y rabbitmq-server

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000 5672 15672

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=calcy_final.settings
ENV PYTHONUNBUFFERED 1

# Copy and start RabbitMQ configuration (optional)
COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Run RabbitMQ and Django server
CMD service rabbitmq-server start && python manage.py runserver 0.0.0.0:8000
