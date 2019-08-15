docker run -it --rm -e SERVER_URL="192.168.233.129:8111" \
 -v $(pwd)/docker_dir/conf:/data/teamcity_agent/conf  \
 -v /var/run/docker.sock:/var/run/docker.sock \
 jetbrains/teamcity-agent

