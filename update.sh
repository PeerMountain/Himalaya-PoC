#!/bin/sh

echo "##teamcity[blockOpened name='update_gateway']"
docker service update himalaya_dev_gateway --with-registry-auth --update-order start-first --detach=false
echo "##teamcity[blockClosed name='update_gateway']"

echo "##teamcity[blockOpened name='update_teleferic']"
docker service update himalaya_dev_teleferic --with-registry-auth --update-order start-first --detach=false
echo "##teamcity[blockClosed name='update_teleferic']"

echo "##teamcity[blockOpened name='update_pgdb']"
docker service update himalaya_dev_pgdb --with-registry-auth --update-order start-first --detach=false
echo "##teamcity[blockClosed name='update_gateway']"