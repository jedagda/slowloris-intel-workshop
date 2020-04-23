#!/bin/bash

# This path is relative to the location of docker-compose.yml
WEB_APP_PATH=$PWD/volumes/public_html
WEB_DESTINATION_PATH=/var/www/html


DB_PATH=$PWD/volumes/public_html
DB_DESTINATION_PATH=/var/lib/mysql

echo WEB_APP_PATH=$WEB_APP_PATH >> .env
echo WEB_DESTINATION_PATH=$WEB_DESTINATION_PATH >> .env