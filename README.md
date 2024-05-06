# Description of the "Social Network Services" Application

This repository contains a solution for creating a social network consisting of four main services:

1. **auth_service**: A service for user authentication and authorization.
2. **social_service**: A service for publishing posts in the social network.
3. **notify_service**: A service for sending push notifications to users.
4. **chat_service**: A service for user communication in chat.

## Dependencies

To run the project, you need to install the following dependencies:

- **Redis**: Used like broker.
- **PostgreSQL**: Used for storing user data, chat messages, and other essential information.

## Project Structure

- **auth_service**: Contains code and configurations for the authentication and authorization service.
- **social_service**: Includes code and settings for the social network post publication service.
- **notify_service**: Contains code and settings for the push notification service.
- **chat_service**: Contains code and configurations for the chat service.
- **ws_client.html**: An HTML page for testing chat between users via WebSocket.
- **soc_net_back**: PostgreSQL database backup file.

## Installation and Running Instructions

1. Install and configure Redis and PostgreSQL on your server.
2. Download the source code of each service into the corresponding directories.
3. Install all dependencies for each service using the package manager of your programming language (e.g., pip for Python).
4. Create a PostgreSQL database and import the backup from the `soc_net_back` file.
5. Configure the settings for each service according to your requirements.
6. Run each service in your runtime environment (e.g., Docker, virtualenv).
7. Open the `ws_client.html` file in a web browser to test chat between users.


