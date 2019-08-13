FROM alpine:latest
RUN apk update
RUN apk upgrade
RUN apk add git
RUN git clone https://github.com/85Dimas85/DevOPS.git
ENTRYPOINT ["sh", "-c", "echo $HOME"] 
#CMD ["-c"]
