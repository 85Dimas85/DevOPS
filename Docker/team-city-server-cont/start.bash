docker run --rm -it --name teamcity-server-instance  \
 -v $(pwd)/docker_dir/data:/data/teamcity_server/datadir \
 -v $(pwd)/docker_dir/logs:/opt/teamcity/logs  \
 -p 8111:8111 \
 jetbrains/teamcity-server
