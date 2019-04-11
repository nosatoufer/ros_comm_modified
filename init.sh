#!/bin/bash
#Pull from the repo and move the necessary files into the ros installation

git pull
cp -r ./ros_comm_modified/dist-packages/* /opt/ros/melodic/lib/python2.7/dist-packages