git pull origin
docker build -t git-image .
docker run  -v /home/dimas/DevOPS/Docker/git-cont/docker_dir:/git_repo git-image 
