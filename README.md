# 2DB_test


Clone this repo 

in derictory add file 
.env
```script
SECRET_KEY=<YOUR SECRET KEY>
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 [::1]
DB_NAME=<NAME OF YOUR DATABASE>
DB_USER=<DATABASE USERNAME>
DB_PASS=<DATABASE PASSWORD>
DB_HOST=db
DB_PORT=5432
```


.env.db
```script
POSTGRES_USER=<DATABASE USERNAME>
POSTGRES_PASSWORD=<DATABASE PASSWORD>
POSTGRES_DB=<NAME OF YOUR DATABASE>
```

```bash
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```
[http://localhost/swagger/](http://localhost/swagger/)
AWS run all 
