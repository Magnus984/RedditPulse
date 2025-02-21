# Reddit Pulse

## Introduction

This project is a social monitoring tool integrated with the telex platform. It fetches popular reddit posts hourly and sends a notification when specific topics that have been selected trend. It leverages FastAPI to create a robust API for handling requests and integrates with Reddit to fetch trending posts based on specified keywords.

## Features

- **FastAPI Integration**: Initializes a FastAPI application with CORS middleware and includes the API router for handling requests.
- **Reddit API Integration**: Fetches trending Reddit posts based on keywords and sends notifications to a specified return URL.
- **Configuration Management**: Utilizes Pydantic for defining application settings, including project name, version, and Reddit API credentials.

## Folder Structure
. ├── .gitignore ├── api │ └── routes │ ├── init.py │ ├── integration.py │ └── posts.py ├── core │ ├── auth.py │ └── config.py ├── main.py ├── requirements.txt └── tests ├── init.py └── test_app.py
- **api/routes**: Contains route definitions for the API.
  - `integration.py`: Returns integration details in JSON format, including app description and key features.
  - `posts.py`: Defines an API endpoint that processes a payload to fetch trending Reddit posts.
- **core**: Core functionalities of the application.
  - `auth.py`: Handles authentication logic.
  - `config.py`: Manages configuration settings using Pydantic.
- **main.py**: Entry point of the application, initializing the FastAPI app.
- **tests**: Contains test cases for the application.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the application using `uvicorn main:app --reload`.

## Deployment

The application is deployed at [URL](https://redditpulse.onrender.com).

## Contribution

We welcome contributions! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.