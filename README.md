# BibleVerseApp

## Overview

BibleVerseApp is a simple Python Flask application that allows users to request specific Bible verses through a web interface. The application consists of a frontend and a backend.

## Architecture

### Frontend

The frontend is a single HTML page (`index.html`) that contains a form for users to input the Bible chapter and verse they are interested in. Upon submission, the form data is sent to the backend for processing.

### Backend

The backend is built using Flask and consists of two main parts:

1. **Initialization (`__init__.py`)**: Initializes the Flask application.
2. **Routes (`routes.py`)**: Defines the application routes.

#### Routes

- `GET /`: Serves the main page with the form.
- `POST /`: Handles the form submission and redirects to the result page.
- `GET /result`: Displays the fetched Bible verse.

## Directory Structure

\`\`\`plaintext
BibleVerseApp/
├── .devcontainer/
│   └── devcontainer.json
├── Dockerfile
├── README.md
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       ├── index.html
│       └── result.html
└── run.py
\`\`\`

### Files

- `.devcontainer/devcontainer.json`: Configuration for the development container.
- `Dockerfile`: Docker configuration for the application.
- `README.md`: Documentation for the project.
- `app/`: Contains the Flask application.
  - `__init__.py`: Initializes the Flask application.
  - `routes.py`: Defines the routes for the application.
  - `templates/`: HTML templates for the frontend.
    - `index.html`: The main page with the form.
    - `result.html`: The page that displays the fetched Bible verse.
- `run.py`: Entry point to run the Flask application.
