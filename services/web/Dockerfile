FROM python:3.7

WORKDIR /usr/src/app



EXPOSE 5000
EXPOSE 3031

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN export FLASK_APP=project/__init__.py

CMD ["uwsgi", "--socket", "127.0.0.1:3031", \ 
    "--callable", "app", \ 
    "--processes", "4", \
    "--threads", "2", \
    "--mount", "/app=manage:app"]