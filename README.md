# 2DB_test

Clone this repo 

In folder "task_api" add files </br>
.env
```script
SECRET_KEY=<YOUR SECRET KEY>
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 [::1] <if you use AWS EC2 Public IPv4 address>
DB_NAME=<NAME OF YOUR DATABASE if you use AWS RDS add DB name>
DB_USER=<DATABASE USERNAME if you use AWS RDS add Master username>
DB_PASS=<DATABASE PASSWORD, if you use AWS RDS add DB password>
DB_HOST=db <if you use AWS RDS add Endpoint>
DB_PORT=5432
```


.env.db
```script
POSTGRES_USER=<DATABASE USERNAME if you use AWS RDS add Master username>
POSTGRES_PASSWORD=<DATABASE PASSWORD, if you use AWS RDS add DB password>
POSTGRES_DB=<NAME OF YOUR DATABASE if you use AWS RDS add DB name>
```

```bash
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```
[http://localhost/swagger/](http://localhost/swagger/) <br />
 <br />
You can see the public project at the link below<br />
[AWS RDS and EC2](http://3.21.33.138/swagger/)
