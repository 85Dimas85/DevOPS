#!/bin/bash
#remove all images with <none> in tag
#remove without --force option
docker rmi $(docker images | grep none | awk '{ printf $3" "}')
