# 2DB_test


Clone this repo 

in derictory add file 
.env
```script
SECRET_KEY='c+-xzhb(j+s4@f0-1k49m#n)t=u153xl))yj!u*jzyclhrz9zw'
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 [::1]
DB_NAME=django_db
DB_USER=kostya12362
DB_PASS=ostapenko123
DB_HOST=db
DB_PORT=5432
```


.env.db
POSTGRES_USER=kostya12362
POSTGRES_PASSWORD=ostapenko123
POSTGRES_DB=django_db

docker-compose -f docker-compose.yml up -d --build

docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput

docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear

http://localhost/swagger/

AWS run all 
