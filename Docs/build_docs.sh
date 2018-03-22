#!/bin/bash
rm ./build/* -Rf
graphdoc -e http://teleferic:8000/teleferic -o ./build/now --force
chmod 777 -R ./build
mv ./build/now/* ./build