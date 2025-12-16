#!/usr/bin/env bash
set -o errexit

cd "$(dirname "$0")"

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=Administrador
export DJANGO_SUPERUSER_EMAIL=admin@admin.com
export DJANGO_SUPERUSER_PASSWORD=Artotska157

python manage.py createsuperuser --noinput || true