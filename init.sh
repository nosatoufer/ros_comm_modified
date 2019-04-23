#!/bin/bash
#Pull from the repo and move the necessary files into the ros installation

git pull
cp -r ./dist-packages/* /opt/ros/melodic/lib/python2.7/dist-packages

source /opt/ros/melodic/setup.sh
