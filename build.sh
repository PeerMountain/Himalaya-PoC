#!/bin/sh

echo "##teamcity[<Build Images> status='starting']"
docker-compose build
echo "##teamcity[<Build Images> status='end']"
echo "##teamcity[<Push Image> image='himalaya_gateway' status='starting']"
docker push meteoro.dxmarkets.com:5000/himalaya_gateway:latest
echo "##teamcity[<Push Image> image='himalaya_gateway' status='end']"
echo "##teamcity[<Push Image> image='himalaya_teleferic' status='starting']"
docker push meteoro.dxmarkets.com:5000/himalaya_teleferic:latest
echo "##teamcity[<Push Image> image='himalaya_teleferic' status='end']"