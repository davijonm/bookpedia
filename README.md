# Project in development

**A "bookpedia" app builded with django and postgres**

## Steps to run the project

**Add variable to env file**

`$ Fill the .env file`

**Build docker image and mount the container**

`$ docker compose build && docker compose up `

**Acess the bash of the container to pull migrations**

`$ docker compose exec web sh `

**Pull migrations**

`$ python manage.py makemigrations `

**Make migrations**

`$ python manage.py migrate `

**Use this script to populate the database**

`$ python manage.py populardb `



