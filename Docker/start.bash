git pull origin
docker build -t git-image .
docker run --rm --name git-cont git-image 
