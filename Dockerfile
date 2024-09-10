# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory inside the Docker container
WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set Poetry in PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy Poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Install dependencies without installing the project itself
RUN poetry install --no-root

# Copy the entire project directory into the container
COPY . .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Command to run when the container starts
CMD ["poetry", "run", "python", "-m", "app"]
