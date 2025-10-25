# Flask Matrix Calculator

A simple Flask web application that provides basic mathematical operations through a REST API, with a focus on multiplication operations. The application is containerized using Docker and includes comprehensive CI/CD workflows using GitHub Actions.

## Features

- Basic mathematical operations (currently multiplication)
- Health check endpoint
- API information endpoint
- Docker support
- Comprehensive test suite
- CI/CD pipeline with matrix testing strategy

## API Endpoints

- `GET /` - Home endpoint, returns basic service information
- `GET /health` - Health check endpoint
- `GET /api/info` - Returns API information and available endpoints
- `GET /api/multiply/<num1>/<num2>` - Multiplies two numbers and returns the result

## Requirements

- Python 3.9 or higher
- Flask 3.0.0
- pytest 7.4.0

## Running Locally

1. Install dependencies:
