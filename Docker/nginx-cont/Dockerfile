FROM alpine:latest
RUN apk update && apk upgrade && apk add git
RUN mkdir /git_repo 
WORKDIR /git_repo
ENTRYPOINT ["git", "clone"] 
CMD ["https://github.com/85Dimas85/DevOPS.git"]
