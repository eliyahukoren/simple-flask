# Deploy Flask image to heroku

Youtube [video_1](https://www.youtube.com/watch?v=eN1EG4-V3Yg)
Youtube [video_2](https://www.youtube.com/watch?v=4axmcEZTE7M)
Dockerhub [youtube](https://www.youtube.com/watch?v=EIHY_CY5J0k)

## Steps:
Docker Compose
1. docker-compose --build up
2. heroku container:push web
3. heroku container:release web -a eli-flask-simple-app
4. heroku run bash


### Heroku documentation:
[Local Development With Docker Compose](https://devcenter.heroku.com/articles/local-development-with-docker-compose#pushing-your-containers-to-heroku
)
[Heroku yml file](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)


>Automatic deploy from github enabled

>Git:

```
git remote set-url origin https://github.com/eliyahukoren/simple-flask.git
git remote set-url origin https://git.heroku.com/eli-flask-simple-app.git
```

Dockerhub:
```
docker tag main-backend:latest elik0ren/simple-flask-repo
docker images
docker push elik0ren/simple-flask-repo
```
