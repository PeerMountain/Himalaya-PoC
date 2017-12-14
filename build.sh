#!/bin/sh

echo "##teamcity[compilationStarted compiler='image_builder']"
docker-compose -f docker-compose.prod.yml build
echo "##teamcity[compilationFinished compiler='image_builder']"

echo "##teamcity[blockOpened name='image_push']"
docker-compose -f docker-compose.prod.yml push
echo "##teamcity[blockClosed name='image_push']"