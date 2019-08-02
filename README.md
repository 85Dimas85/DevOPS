docker run -d -p 8080:80 nginx
docker ps
curl http://127.0.0.1:8080

docker run alpine

cd DevOPS/
git remote add origin git@github.com:85Dimas85/DevOPS.git
vi README.md
git add README.md
git commit
git push origin
git push --set-upstream origin master
git pull
