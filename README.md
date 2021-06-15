# Notifications System 

## Installation

run `docker-compose build`

run `docker-compose up`

## Run Tests

`docker exec -it notification-system_app_1 bash -c "pytest"`

`docker exec -it notification-system_send-notification_1 sh -c "npm run test"`



## Available APIs And Documentation

http://localhost:8000/docs

## Usage

Send notification to user or group of users with many providers of notification
witch is [fcm,sms,email]

# Use these apis

- send `POST` request to  `/api/users` to create user
- send `GET` request to `/api/users` to get users ids
- send `POST` request to  `/api/notifications` to create a notification
- send `GET` request to  `/api/notifications` to get notifications


In the console you will see logs of notifications
