#!/bin/bash
# Create local network
docker network create ws_bridge
# run paulius service
cd PauliausService
docker-compose up --build --force-recreate -d
# run main service
cd ..
docker-compose up --build --force-recreate -d
