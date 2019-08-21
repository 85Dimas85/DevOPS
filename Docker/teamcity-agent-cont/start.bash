for i in {1..3}
do
  mkdir -p $(pwd)/docker_dir/conf$i
  docker run -it --rm -d -e SERVER_URL="192.168.233.129:8111" \
  --name teamcity-agent-cont$i \
  -v $(pwd)/docker_dir/conf$i:/data/teamcity_agent/conf  \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jetbrains/teamcity-agent
done
