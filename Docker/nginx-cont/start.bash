git pull origin
docker build -t nginx-image .
docker run --name nginx-cont --rm -p 8080:8080 nginx-image 
#docker run -p {your_local_port}:8080 {your image}.
