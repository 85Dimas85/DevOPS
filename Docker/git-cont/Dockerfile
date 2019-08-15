FROM alpine:latest

RUN apk update && apk upgrade && apk add git
RUN mkdir /git_repo 

RUN adduser -D -u 1000 -G nobody dimas 
RUN chown dimas -R /git_repo
WORKDIR /git_repo

USER dimas
ENTRYPOINT ["git", "clone"] 

#Light repo, can be overwriten in comandline argument
CMD ["https://github.com/jlord/hello.git"]
