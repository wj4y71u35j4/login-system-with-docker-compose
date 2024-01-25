# User Authentication System

This project is a simple user authentication system built with Flask, MySQL, and Docker Compose. It provides basic functionalities for users to sign up and sign in.

## Description

The application is structured into three main components:

- **Flask App**: A Python web application using the Flask framework. It handles HTTP requests for user authentication, interacts with the MySQL database, and serves HTML pages for the UI.
- **MySQL Database**: Used for storing user account information securely. Passwords are hashed before storage.
- **Docker Compose**: Orchestrates the Flask application and MySQL database, ensuring easy setup and deployment.

### Features

- **Sign Up**: Users can create a new account. The system stores their username and hashed password in the database.
- **Sign In**: Users can log in using their credentials. The system validates these against the database entries.

## Getting Started

### Dependencies

- Docker and Docker Compose should be installed on your system.
- Internet connection to pull necessary Docker images.
- A modern web browser.

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Running the Application

1. Start the application with Docker Compose:

    ```bash
    docker-compose up --build
    ```

    This command builds the Docker images and starts the containers.

2. Access the application:

    - **Sign Up Page**: Open `http://localhost:5000/` in your web browser to create a new user.
    - **Sign In Page**: Navigate to `http://localhost:5000/signin_page` to log in with an existing user.

### Stopping the Application

To stop and remove the containers, use:

```bash
docker-compose down
```

## Troubleshooting

If you encounter issues with the application not running correctly, consider the following steps:

- Ensure Docker and Docker Compose are correctly installed and running.
- Check the Docker logs for error messages or warnings.
- For browser issues, try clearing the cache or using a different browser.

## Authors

Sung Tao, Wu 
Contact: sungtaowu@gmail.com

## Version History

- 0.1 - Initial Release

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation
- Docker and Docker Compose documentation
- MySQL official guides
