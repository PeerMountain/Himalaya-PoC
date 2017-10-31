#!/bin/sh

docker-compose build

docker push meteoro.dxmarkets.com:5000/himalaya_gateway:latest

docker push meteoro.dxmarkets.com:5000/himalaya_teleferic:latest