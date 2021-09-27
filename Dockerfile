FROM python:3.9.0

WORKDIR /home/

RUN echo 'asgeww'

RUN git clone https://github.com/chogoal/Web2.git

WORKDIR /home/Web2/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=project02.settings.deploy && python manage.py migrate --settings=project02.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=project02.settings.deploy project02.wsgi --bind 0.0.0.0:8000"]
