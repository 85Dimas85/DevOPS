git pull origin
docker build -t git-image .
docker run  -v $(pwd)/docker_dir:/git_repo git-image https://github.com/jlord/hello.git 
