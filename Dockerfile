ARG PYTHON_VERSION=3.11

# Stage 1: Build the dependencies

FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Build the application

FROM python:${PYTHON_VERSION}-slim

WORKDIR /app    

# Copy the dependencies from the builder stage
COPY --from=builder /root/.local /root/.local

# Copy the application code
COPY app.py .
COPY test_app.py .

# Set the environment variable
ENV PATH="/root/.local/bin:$PATH"

LABEL python_version=${PYTHON_VERSION}

# Expose the port
EXPOSE 8000

# Set the entrypoint
CMD ["python", "app.py"]