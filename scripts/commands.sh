#!/bin/sh
set -e

echo "Coletando arquivos estáticos"
sleep 2
python manage.py collectstatic --noinput

echo "Preparando migrações para os modelos"
sleep 2
python manage.py makemigrations --noinput

echo "Migrando modelos"
sleep 2
python manage.py migrate --noinput

echo "Iniciando servidor"
sleep 2
python manage.py runserver 0.0.0.0:8000