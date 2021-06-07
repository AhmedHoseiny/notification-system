# Notifications System 

## Installation

run `docker-compose up`

## Run Tests

`docker exec -it notification-system_app_1 bash -c "pytest"`


## Available APIs And Docs

http://localhost:8000/docs

## Usage

Send notification to user or group of users with many providers of notification
witch is [fcm,sms,email]

#Use these apis

- send `POST` request to  `/api/users` to create user
- send `GET` request to `/api/users` to get users ids
- send `POST` request to  `/api/notifications` to create a notification
- send `GET` request to  `/api/notifications` to get notifications

The background task fired to send notification across multiple providers

In the console you will see logs of notifications
