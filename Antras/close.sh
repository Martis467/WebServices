#!/bin/bash
echo "Stopping services"
docker stop main_service
docker stop paulius_service
echo "Removing local network"
docker network rm ws_bridge
echo "Clearing empty images"
docker rmi $(docker images --filter dangling=true -q --no-trunc)
echo "Done"