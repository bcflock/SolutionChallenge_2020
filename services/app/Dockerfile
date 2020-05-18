FROM python:3.7

WORKDIR /usr/src/project

EXPOSE 5000
EXPOSE 3031

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN export FLASK_APP=project

CMD ["uwsgi", "--http", ":3031", \ 
    "--callable", "app", \ 
    "--processes", "4", \
    "--threads", "2", \
    "--mount", "/app=wsgi:app"]

    #works when run through compose