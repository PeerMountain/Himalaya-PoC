#!/bin/sh

echo "##teamcity[compilationStarted compiler='image_builder']"
docker-compose build
echo "##teamcity[compilationFinished compiler='image_builder']"

echo "##teamcity[blockOpened name='push-himalaya_gateway']"
docker push meteoro.dxmarkets.com:5000/himalaya_gateway:latest
echo "##teamcity[blockClosed name='push-himalaya_gateway']"

echo "##teamcity[blockOpened name='push-himalaya_teleferic']"
docker push meteoro.dxmarkets.com:5000/himalaya_teleferic:latest
echo "##teamcity[blockClosed name='push-himalaya_teleferic']"