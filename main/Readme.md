"""
Install on heroku
"""

https://devcenter.heroku.com/articles/local-development-with-docker-compose#pushing-your-containers-to-heroku

https://devcenter.heroku.com/articles/build-docker-images-heroku-yml




Docker Compose
1. docker-compose --build up
2. heroku container:push web
3. heroku container:release web -a eli-flask-simple-app
4. heroku run bash

Automatic deploy from github enabled