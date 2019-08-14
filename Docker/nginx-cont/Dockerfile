FROM nginx:latest
RUN apt update -y && apt upgrade -y 
ADD docker_dir/nginx-conf/nginx.conf 	/etc/nginx/nginx.conf
ADD docker_dir/nginx-conf/conf.d/ 	/etc/nginx/conf.d/
RUN mkdir /nginx-data
ADD docker_dir/nginx-data/ 		/nginx-data/
#RUN mkdir /git_repo 
#WORKDIR /git_repo
#ENTRYPOINT ["git", "clone"] 
#CMD ["https://github.com/85Dimas85/DevOPS.git"]
