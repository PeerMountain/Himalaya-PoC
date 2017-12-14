#!/bin/sh

echo "Build Images"
docker-compose build
echo "Push gateway"
docker push meteoro.dxmarkets.com:5000/himalaya_gateway:latest
echo "Push teleferic"
docker push meteoro.dxmarkets.com:5000/himalaya_teleferic:latest