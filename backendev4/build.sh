#comportamiento render
set -o errexit

#dependencias del rpyecto
pip install -r requirements.txt


python manage.py collectstatic --no-input


python manage.py migrate
#creando el super user altiro pq sino pide suscripcion de pago
export DJANGO_SUPERUSER_USERNAME=Administrador
export DJANGO_SUPERUSER_EMAIL=admin@admin.com
export DJANGO_SUPERUSER_PASSWORD=Artotska157

python manage.py createsuperuser --noinput || true